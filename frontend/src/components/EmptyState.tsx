import React from "react";
import Link from "next/link";

interface EmptyStateProps {
  title?: string;
  message?: string;
  actionText?: string;
  actionHref?: string;
}

export function EmptyState({
  title = "No results found",
  message = "No travel packages or destinations matched all of your selected requirements. Try adjusting your budget, trip duration, travel month, or interest.",
  actionText = "Change Search Filters",
  actionHref = "/",
}: EmptyStateProps) {
  return (
    <div className="rounded-2xl border border-[#DCEAF2] bg-white p-10 text-center max-w-xl mx-auto my-12 shadow-sm">
      <div className="w-14 h-14 rounded-full bg-[#EAF8FB] text-[#0EA5C6] mx-auto flex items-center justify-center mb-4">
        <svg
          className="w-7 h-7"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="1.5"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </div>

      <h3 className="text-xl font-bold text-[#12304A]">{title}</h3>
      <p className="mt-2 text-sm text-[#5B7185] leading-relaxed">{message}</p>

      <div className="mt-6">
        <Link
          href={actionHref}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-semibold text-sm transition-colors shadow-xs"
        >
          <svg
            className="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            />
          </svg>
          {actionText}
        </Link>
      </div>
    </div>
  );
}
