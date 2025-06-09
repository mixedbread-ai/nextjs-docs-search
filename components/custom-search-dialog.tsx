'use client';

import type { SharedProps } from 'fumadocs-ui/components/dialog/search';
import SearchDialog from 'fumadocs-ui/components/dialog/search-default';

export default function CustomSearchDialog(props: SharedProps) {
  return (
    <SearchDialog
      api="/api/vector-store"
      delayMs={200}
      {...props}
    />
  );
} 