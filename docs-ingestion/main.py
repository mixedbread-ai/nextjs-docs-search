import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
import re
from urllib.parse import urljoin
import os
from datetime import datetime
from collections import deque
import json


def safe_get_filename_from_url(url, page_title=None):
    """Generate filename dynamically from URL structure"""
    try:
        # Parse the URL to get the path
        if "/docs/" not in url:
            return "unknown.txt"

        # Extract path after /docs/
        path_part = url.split("/docs/", 1)[1].strip("/")

        # Handle main docs page
        if not path_part:
            if page_title and page_title.lower() not in [
                "nextjs documentation",
                "documentation",
            ]:
                return page_title.lower().replace(" ", "_").replace("-", "_") + ".txt"
            return "introduction.txt"

        # Convert path to filename: replace / and - with _, clean up
        filename = path_part.replace("/", "_").replace("-", "_")

        # Clean up multiple underscores and ensure .txt extension
        filename = re.sub(r"_+", "_", filename).strip("_")

        if not filename:
            return "index.txt"

        return filename + ".txt"

    except Exception:
        return "unknown.txt"


def safe_get_breadcrumb_from_url(url):
    """Generate breadcrumb dynamically from URL structure"""
    try:
        # Parse the URL to get the path
        if "/docs/" not in url:
            return "NextJS Documentation"

        # Extract path after /docs/
        path_part = url.split("/docs/", 1)[1].strip("/")

        # Handle main docs page
        if not path_part:
            return "NextJS Documentation"

        # Split path into parts and clean them up
        parts = [part for part in path_part.split("/") if part]

        if not parts:
            return "NextJS Documentation"

        # Convert each part to a readable format
        breadcrumb_parts = []
        for part in parts:
            # Replace hyphens with spaces and title case
            clean_part = part.replace("-", " ").title()
            breadcrumb_parts.append(clean_part)

        return " / ".join(breadcrumb_parts)

    except Exception:
        return "NextJS Documentation"


async def extract_metadata(crawler, url):
    """Extract metadata including breadcrumb and title from the page"""
    print(f"🔍 Extracting metadata from: {url}")

    # Try multiple selectors for different page types
    selectors_to_try = [
        "div.prose[data-docs='true']",
        "main",
        "article",
        ".content",
        "body",
    ]

    metadata_result = None
    for selector in selectors_to_try:
        try:
            config = CrawlerRunConfig(
                css_selector=selector,
                word_count_threshold=1,
            )
            result = await crawler.arun(url=url, config=config)
            if result.success and result.markdown and result.markdown.strip():
                metadata_result = result
                print(f"✓ Metadata extracted using selector: {selector}")
                break
        except Exception as e:
            print(f"⚠️  Selector '{selector}' failed: {e}")
            continue

    if not metadata_result:
        print(f"❌ Could not extract any content from {url}")
        return None

    # Extract page title
    page_title = "NextJS Documentation"
    try:
        title_pattern = r"^#\s+(.+)$"
        title_match = re.search(title_pattern, metadata_result.markdown, re.MULTILINE)
        if title_match:
            page_title = title_match.group(1).strip()
        else:
            # Try first non-empty line
            lines = [
                line.strip()
                for line in metadata_result.markdown.split("\n")
                if line.strip()
            ]
            if lines:
                first_line = lines[0].lstrip("#").strip()
                if first_line:
                    page_title = first_line
    except Exception as e:
        print(f"⚠️  Error extracting title: {e}")

    breadcrumb_path = safe_get_breadcrumb_from_url(url)
    filename = safe_get_filename_from_url(url, page_title)

    # URL title fallback
    url_title = "Unknown"
    try:
        parts = [p for p in url.split("/") if p and p not in ["http:", "https:"]]
        if parts:
            url_title = parts[-1].replace("-", " ").title()
    except:
        pass

    print(f"📖 Title: {page_title}")
    print(f"🗂️  Breadcrumb: {breadcrumb_path}")
    print(f"📁 Filename: {filename}")

    return {
        "page_title": page_title,
        "breadcrumb_path": breadcrumb_path,
        "url_title": url_title,
        "source_url": url,
        "filename": filename,
    }


def clean_markdown_links(text):
    """Remove markdown links but keep the link text"""
    try:
        # Pattern to match [text](url) and replace with just text
        link_pattern = r"\[([^\]]+)\]\([^)]+\)"
        cleaned_text = re.sub(link_pattern, r"\1", text)

        # Also remove standalone URLs
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]*'
        cleaned_text = re.sub(url_pattern, "", cleaned_text)

        return cleaned_text
    except:
        return text


async def discover_section_links(crawler, section_url):
    """Discover all links within a specific section, including deeply nested subroutes"""
    print(f"🔍 Discovering all links in section: {section_url}")

    section_links = set()
    to_explore = deque([section_url])
    explored = set()
    depth_map = {section_url: 0}  # Track depth of each URL
    max_depth = 0

    while to_explore:
        current_url = to_explore.popleft()
        if current_url in explored:
            continue

        explored.add(current_url)
        current_depth = depth_map.get(current_url, 0)
        max_depth = max(max_depth, current_depth)

        print(f"   🔗 Exploring (depth {current_depth}): {current_url}")

        try:
            config = CrawlerRunConfig(
                word_count_threshold=1,
                exclude_external_links=False,
            )

            result = await crawler.arun(url=current_url, config=config)
            if not result.success:
                print(f"   ⚠️  Failed to fetch: {current_url}")
                continue

        except Exception as e:
            print(f"   ⚠️  Error exploring {current_url}: {e}")
            continue

        # Extract links from this page
        page_links = set()

        # Get internal links from the crawl result
        if hasattr(result, "links") and result.links:
            internal_links = result.links.get("internal", [])
            for link in internal_links:
                try:
                    if isinstance(link, dict):
                        href = link.get("href", "")
                    else:
                        href = str(link)

                    if href.startswith("/"):
                        full_url = urljoin("https://nextjs.org", href)
                    elif href.startswith("https://nextjs.org"):
                        full_url = href
                    else:
                        continue

                    if "/docs/" in full_url and not full_url.endswith("#"):
                        clean_url = full_url.split("#")[0].split("?")[0].rstrip("/")

                        # Convert pages docs to app docs
                        if "/docs/pages/" in clean_url:
                            clean_url = clean_url.replace("/docs/pages/", "/docs/app/")

                        page_links.add(clean_url)

                except:
                    continue

        # Also extract from markdown content
        try:
            markdown_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", result.markdown)
            for text, href in markdown_links:
                try:
                    if href.startswith("/docs"):
                        full_url = urljoin("https://nextjs.org", href)
                        clean_url = full_url.split("#")[0].split("?")[0].rstrip("/")

                        # Convert pages docs to app docs
                        if "/docs/pages/" in clean_url:
                            clean_url = clean_url.replace("/docs/pages/", "/docs/app/")

                        page_links.add(clean_url)
                except:
                    continue
        except:
            pass

        # Filter links that belong to this section and add to exploration queue
        new_links_found = 0
        for link in page_links:
            if is_in_section(link, section_url):
                section_links.add(link)

                # Add to exploration queue if not already explored/queued
                if link not in explored and link not in [item for item in to_explore]:
                    to_explore.append(link)
                    depth_map[link] = current_depth + 1
                    new_links_found += 1

        if new_links_found > 0:
            print(f"   ➕ Found {new_links_found} new section links to explore")

    discovered_links = list(section_links)
    discovered_links.sort(key=lambda x: (depth_map.get(x, 0), len(x.split("/")), x))

    print(f"📋 Section discovery complete:")
    print(f"   📄 Total links found: {len(discovered_links)}")
    print(f"   📏 Maximum depth: {max_depth}")
    print(f"   🔗 Sample links by depth:")

    # Show sample links by depth
    by_depth = {}
    for link in discovered_links:
        depth = depth_map.get(link, 0)
        if depth not in by_depth:
            by_depth[depth] = []
        by_depth[depth].append(link)

    for depth in sorted(by_depth.keys()):
        links_at_depth = by_depth[depth]
        print(f"     Depth {depth}: {len(links_at_depth)} links")
        for link in links_at_depth[:3]:  # Show first 3 at each depth
            print(f"       - {link}")
        if len(links_at_depth) > 3:
            print(f"       ... and {len(links_at_depth) - 3} more")

    return discovered_links


def is_in_section(url, section_url):
    """Check if a URL belongs to a specific section - handles deeply nested paths"""
    # Main docs page
    if section_url.endswith("/docs") and url.endswith("/docs"):
        return True

    # For other sections, check if URL starts with the section path
    if not section_url.endswith("/docs"):
        section_path = section_url.replace("https://nextjs.org", "")
        url_path = url.replace("https://nextjs.org", "")

        # Make sure we're checking for exact path matches to avoid false positives
        # e.g., /docs/app/guides should not match /docs/app/guides-something-else
        return url_path.startswith(section_path + "/") or url_path == section_path

    return False


async def scrape_page(crawler, url, docs_dir):
    """Scrape a single page and save it"""
    print(f"📄 Scraping: {url}")

    try:
        # Extract metadata first
        metadata = await extract_metadata(crawler, url)
        if not metadata:
            return False

        # Try multiple selectors for content
        selectors_to_try = [
            "div.prose[data-docs='true']",
            "main",
            "article",
            ".content",
            "body",
        ]

        content_result = None
        for selector in selectors_to_try:
            try:
                config = CrawlerRunConfig(
                    css_selector=selector,
                    excluded_tags=["nav", "header", "footer", "button", "svg"],
                    excluded_selector="""
                        div[data-feedback-inline], 
                        nav[aria-label='pagination'],
                        .code-block_actions__yphRf,
                        .code-block_copyButton__uo5Yu,
                        .switcher_container__cVe_S,
                        button[aria-label],
                        svg,
                        .nextra-breadcrumb
                    """,
                    word_count_threshold=5,
                    exclude_external_links=True,
                )

                result = await crawler.arun(url=url, config=config)
                if result.success and result.markdown and result.markdown.strip():
                    content_result = result
                    print(f"✓ Content extracted using selector: {selector}")
                    break
            except Exception as e:
                print(f"⚠️  Content selector '{selector}' failed: {e}")
                continue

        if not content_result:
            print(f"❌ Failed to extract content")
            return False

        # Clean content
        cleaned_content = clean_markdown_links(content_result.markdown)

        # Skip if too little content
        if len(cleaned_content.strip()) < 50:
            print(
                f"⚠️  Skipping - insufficient content ({len(cleaned_content.strip())} chars)"
            )
            return False

        # Save file
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filepath = os.path.join(docs_dir, metadata["filename"])

        os.makedirs(
            os.path.dirname(filepath) if os.path.dirname(filepath) else docs_dir,
            exist_ok=True,
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: \"{metadata['page_title']}\"\n")
            f.write(f"path: \"{metadata['breadcrumb_path']}\"\n")
            f.write(f"source_url: \"{metadata['source_url']}\"\n")
            f.write(f'scraped_date: "{current_time}"\n')
            f.write(f"content_length: {len(cleaned_content)}\n")
            f.write("---\n\n")
            f.write(cleaned_content)

        print(f"✅ Saved: {filepath}")
        return True

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        import traceback

        traceback.print_exc()
        return False


async def crawl_documentation(max_pages=200):
    """Crawl all NextJS documentation pages in structured order"""

    # Structured section order - each section will be completed before moving to next
    SECTIONS = [
        {
            "name": "Main Documentation",
            "url": "https://nextjs.org/docs",
        },
        {
            "name": "App Router - Getting Started",
            "url": "https://nextjs.org/docs/app/getting-started",
        },
        {
            "name": "App Router - Guides",
            "url": "https://nextjs.org/docs/app/guides",
        },
        {
            "name": "App Router - Building Your Application",
            "url": "https://nextjs.org/docs/app/building-your-application",
        },
        {
            "name": "App Router - Deep Dive",
            "url": "https://nextjs.org/docs/app/deep-dive",
        },
        {
            "name": "App Router - API Reference",
            "url": "https://nextjs.org/docs/app/api-reference",
        },
        {
            "name": "Architecture",
            "url": "https://nextjs.org/docs/architecture",
        },
        {
            "name": "Community",
            "url": "https://nextjs.org/docs/community",
        },
    ]

    docs_dir = "docs"
    os.makedirs(docs_dir, exist_ok=True)

    # Track visited URLs and failed URLs globally
    visited = set()
    failed = set()
    scraped_count = 0

    # Progress tracking
    progress_file = os.path.join(docs_dir, "_crawl_progress.json")

    async with AsyncWebCrawler() as crawler:
        print("🚀 Starting Structured App Router NextJS Documentation Crawler")
        print("📚 Handles deeply nested subroutes automatically")
        print(f"📁 Output directory: {docs_dir}")
        print(f"📚 Sections to process: {len(SECTIONS)}")
        for i, section in enumerate(SECTIONS, 1):
            print(f"   {i}. {section['name']}")
        if max_pages:
            print(f"📊 Max pages: {max_pages}")
        print("=" * 80)

        for section_idx, section in enumerate(SECTIONS, 1):
            if max_pages and scraped_count >= max_pages:
                print(f"📊 Reached max pages limit ({max_pages})")
                break

            print(f"\n🎯 SECTION {section_idx}/{len(SECTIONS)}: {section['name']}")
            print(f"🔗 URL: {section['url']}")
            print("-" * 60)

            # Discover all links in this section first (including deep nesting)
            section_links = await discover_section_links(crawler, section["url"])

            print(f"\n📄 Ready to scrape {len(section_links)} pages in this section")

            # Scrape all pages in this section
            section_scraped = 0
            section_failed = 0

            for link_idx, link in enumerate(section_links, 1):
                if max_pages and scraped_count >= max_pages:
                    print(f"📊 Reached max pages limit ({max_pages})")
                    break

                if link in visited:
                    continue

                visited.add(link)

                print(
                    f"\n📄 [{section_idx}.{link_idx}/{len(section_links)}] Scraping: {link}"
                )

                success = await scrape_page(crawler, link, docs_dir)

                if success:
                    scraped_count += 1
                    section_scraped += 1
                    print(
                        f"✅ Success! Total: {scraped_count}/{max_pages if max_pages else '∞'}"
                    )
                else:
                    failed.add(link)
                    section_failed += 1
                    print(f"❌ Failed!")

                # Save progress periodically
                if scraped_count % 10 == 0 and scraped_count > 0:
                    progress_data = {
                        "scraped_count": scraped_count,
                        "current_section": section["name"],
                        "section_progress": f"{section_idx}/{len(SECTIONS)}",
                        "visited": list(visited),
                        "failed": list(failed),
                        "last_updated": datetime.now().isoformat(),
                    }
                    with open(progress_file, "w") as f:
                        json.dump(progress_data, f, indent=2)
                    print(f"💾 Progress saved")

            # Section summary
            print(f"\n📊 Section {section_idx} Complete:")
            print(f"   ✅ Scraped: {section_scraped} pages")
            print(f"   ❌ Failed: {section_failed} pages")
            print(
                f"   📈 Total progress: {scraped_count}/{max_pages if max_pages else '∞'}"
            )

        # Final summary
        print("\n" + "=" * 80)
        print("🎉 Structured App Router Crawling Complete!")
        print(f"✅ Successfully scraped: {scraped_count} pages")
        print(f"❌ Failed to scrape: {len(failed)} pages")
        print(f"📁 Files saved in: {docs_dir}")

        # Show failed URLs by section
        if failed:
            print(f"\n❌ Failed URLs:")
            for url in list(failed)[:10]:
                print(f"   - {url}")
            if len(failed) > 10:
                print(f"   ... and {len(failed) - 10} more")

        # Save final progress
        final_progress = {
            "scraped_count": scraped_count,
            "visited": list(visited),
            "failed": list(failed),
            "sections": SECTIONS,
            "completed": True,
            "completion_time": datetime.now().isoformat(),
        }
        with open(progress_file, "w") as f:
            json.dump(final_progress, f, indent=2)


async def main():
    """Main function to run the documentation crawler"""

    # Configuration
    MAX_PAGES = 500

    print("NextJS Structured App Router Documentation Crawler")
    print("=" * 60)

    # Start crawling
    await crawl_documentation(MAX_PAGES)


if __name__ == "__main__":
    asyncio.run(main())
