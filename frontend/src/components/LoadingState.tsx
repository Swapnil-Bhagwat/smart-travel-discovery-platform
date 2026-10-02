import React from "react";

export function LoadingSpinner({ message = "Searching travel packages..." }: { message?: string }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4 text-center">
      <div className="relative w-14 h-14">
        <div className="w-14 h-14 rounded-full border-4 border-[#DCEAF2] border-t-[#0EA5C6] animate-spin" />
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="w-3 h-3 rounded-full bg-[#0EA5C6] animate-ping" />
        </div>
      </div>
      <p className="mt-4 text-sm font-medium text-[#5B7185] animate-pulse">{message}</p>
    </div>
  );
}

export function DestinationCardsSkeleton({ count = 3 }: { count?: number }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-pulse">
      {Array.from({ length: count }).map((_, i) => (
        <div
          key={i}
          className="rounded-2xl bg-white border border-[#DCEAF2] overflow-hidden flex flex-col shadow-xs"
        >
          <div className="h-52 bg-slate-100 w-full" />
          <div className="p-6 space-y-4 flex-1 flex flex-col">
            <div className="h-6 bg-slate-100 rounded w-2/3" />
            <div className="h-4 bg-slate-100 rounded w-full" />
            <div className="h-4 bg-slate-100 rounded w-5/6" />
            <div className="mt-auto pt-4 border-t border-[#DCEAF2] flex justify-between">
              <div className="h-8 bg-slate-100 rounded w-1/3" />
              <div className="h-8 bg-slate-100 rounded w-1/3" />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export function PackageCardsSkeleton({ count = 3 }: { count?: number }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-pulse">
      {Array.from({ length: count }).map((_, i) => (
        <div
          key={i}
          className="rounded-2xl bg-white border border-[#DCEAF2] overflow-hidden flex flex-col shadow-xs"
        >
          <div className="h-48 bg-slate-100 w-full" />
          <div className="p-6 space-y-3 flex-1 flex flex-col">
            <div className="h-4 bg-slate-100 rounded w-1/3" />
            <div className="h-6 bg-slate-100 rounded w-3/4" />
            <div className="h-4 bg-slate-100 rounded w-1/2" />
            <div className="mt-auto pt-4 border-t border-[#DCEAF2] flex justify-between items-center">
              <div className="h-6 bg-slate-100 rounded w-1/3" />
              <div className="h-9 bg-slate-100 rounded w-28" />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
