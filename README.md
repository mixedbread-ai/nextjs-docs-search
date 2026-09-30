# Next.js Documentation Search Demo

## Quick Demo Setup

### 1. Clone & Install

```bash
git clone <repo-url>
cd nextjs-docs-search
npm install
```

### 2. Install Mixedbread CLI

```bash
npm install -g @mixedbread/cli
```

### 3. Create a Store

```bash
# Set your API key
export MXBAI_API_KEY=your_api_key_here

# Create a store with a unique name
mxbai store create "your-store-name" --description "Demo documentation search"

# Get the store ID
mxbai store list
```

### 4. Environment Setup

Create `.env.local`:

```env
MXBAI_API_KEY=your_api_key_here
STORE_ID=your_store_id_here
```

### 5. Upload Content

```bash
# Upload all documentation files
mxbai store sync "your-store-name" "**/*.md" "content/**/*.md"
```

### 6. Test Sync

```bash
# Preview what would sync
npm run sync-content:dry-run

# Test automatic sync (only changed files)
npm run sync-content
```

### 7. Run Demo

```bash
npm run dev
```

Visit `http://localhost:3000` and test the semantic search.

## Deployment (Vercel)

When deployed, the build script automatically syncs content:

**package.json:**

```json
{
  "build": "next build && npm run sync-content"
}
```

**Environment Variables on Vercel:**

- `MXBAI_API_KEY`
- `STORE_ID`

The sync command uses hash-based change detection for efficient CI/CD deployment.

## Commands Reference

```bash
# Development
npm run dev                    # Start dev server
npm run build                 # Build + sync content

# Content Sync
npm run sync-content          # Sync changed files (CI optimized)
npm run sync-content:dry-run  # Preview changes
npm run sync-content:force    # Force sync all files

# Store Management
mxbai store list              # List stores
mxbai store get "your-store-name" # Get store details
```
