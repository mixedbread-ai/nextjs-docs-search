'use client';

import { RootProvider } from 'fumadocs-ui/provider';
import type { ReactNode } from 'react';
import CustomSearchDialog from './custom-search-dialog';

export function CustomRootProvider({ children }: { children: ReactNode }) {
  return (
    <RootProvider
      search={{
        SearchDialog: CustomSearchDialog,
        options: {
          api: '/api/vector-store',
        },
      }}
    >
      {children}
    </RootProvider>
  );
} 