"use client";

import React from "react";
import Link from "next/link";

interface ComparisonErrorProps {
  title?: string;
  message?: string;
  onRetry?: () => void;
}

export function ComparisonError({
  title = "Could not load comparison packages",
  message = "One or more travel packages could not be retrieved from the server.",
  onRetry,
}: ComparisonErrorProps) {
  return (
    <div className="max-w-xl mx-auto py-16 px-4 text-center">
      <div className="w-14 h-14 mx-auto rounded-2xl bg-[#FFF4EC] border border-[#FF8A4C]/30 flex items-center justify-center text-[#FF8A4C] mb-4 shadow-sm">
        <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
        </svg>
      </div>

      <h2 className="text-xl font-bold text-[#12304A] tracking-tight">{title}</h2>
      <p className="mt-2 text-sm text-[#5B7185] max-w-md mx-auto">{message}</p>

      <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
        {onRetry && (
          <button
            onClick={onRetry}
            className="px-4 py-2 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-xs sm:text-sm transition-colors shadow-sm"
          >
            Try Again
          </button>
        )}
        <Link
          href="/packages"
          className="px-4 py-2 rounded-xl bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] font-bold text-xs sm:text-sm transition-colors shadow-xs"
        >
          Browse Packages
        </Link>
      </div>
    </div>
  );
}
