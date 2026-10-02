"use client";

import React from "react";

export function ComparisonLoading({ count = 3 }: { count?: number }) {
  const cols = Array.from({ length: Math.min(Math.max(count, 2), 3) });

  return (
    <div className="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-pulse">
      {/* Page Title skeleton */}
      <div className="mb-8">
        <div className="h-6 w-36 bg-slate-200 rounded-md mb-2" />
        <div className="h-9 w-72 bg-slate-200 rounded-lg mb-2" />
        <div className="h-4 w-96 bg-slate-100 rounded-md" />
      </div>

      {/* Table Card Skeleton */}
      <div className="bg-white rounded-2xl border border-[#DCEAF2] overflow-hidden shadow-sm">
        {/* Top header row */}
        <div className="grid grid-cols-1 sm:grid-cols-4 p-6 gap-4 border-b border-[#DCEAF2]">
          <div className="hidden sm:block">
            <div className="h-5 w-24 bg-slate-200 rounded mb-2" />
            <div className="h-4 w-32 bg-slate-100 rounded" />
          </div>
          {cols.map((_, i) => (
            <div key={i} className="space-y-3 p-4 rounded-xl border border-slate-100">
              <div className="h-36 w-full bg-slate-200 rounded-lg" />
              <div className="h-4 w-20 bg-slate-200 rounded" />
              <div className="h-5 w-40 bg-slate-200 rounded" />
              <div className="h-8 w-full bg-slate-200 rounded-lg" />
            </div>
          ))}
        </div>

        {/* Shimmer Rows */}
        <div className="p-6 space-y-4">
          {[1, 2, 3, 4, 5, 6].map((row) => (
            <div key={row} className="flex gap-4 items-center py-3 border-b border-slate-100">
              <div className="w-40 h-4 bg-slate-200 rounded shrink-0" />
              {cols.map((_, i) => (
                <div key={i} className="flex-1 h-4 bg-slate-100 rounded" />
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
