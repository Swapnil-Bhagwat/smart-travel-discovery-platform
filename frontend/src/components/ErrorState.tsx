import React from "react";
import Link from "next/link";

interface ErrorStateProps {
  title?: string;
  message?: string;
  onRetry?: () => void;
  showBackLink?: boolean;
}

export function ErrorState({
  title = "Something went wrong",
  message = "We encountered an issue while communicating with the travel backend.",
  onRetry,
  showBackLink = true,
}: ErrorStateProps) {
  return (
    <div className="rounded-2xl border border-rose-200 bg-white p-8 text-center max-w-lg mx-auto my-12 shadow-sm">
      <div className="w-12 h-12 rounded-full bg-rose-50 text-rose-500 mx-auto flex items-center justify-center mb-4">
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
        </svg>
      </div>

      <h3 className="text-lg font-bold text-[#12304A]">{title}</h3>
      <p className="mt-2 text-sm text-[#5B7185]">{message}</p>

      <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
        {onRetry && (
          <button
            onClick={onRetry}
            className="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-sm font-semibold transition-colors shadow-xs"
          >
            Try Again
          </button>
        )}
        {showBackLink && (
          <Link
            href="/"
            className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-[#12304A] text-sm font-semibold transition-colors"
          >
            Modify Search
          </Link>
        )}
      </div>
    </div>
  );
}
