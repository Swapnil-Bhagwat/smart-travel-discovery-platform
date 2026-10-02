"use client";

import React from "react";
import Link from "next/link";

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  totalItems: number;
  itemsPerPage: number;
  createPageHref: (page: number) => string;
  onPageClick?: (page: number) => void;
}

/**
 * Generates an array of page numbers and ellipsis markers for clean pagination display.
 */
export function getPaginationRange(
  currentPage: number,
  totalPages: number
): (number | string)[] {
  if (totalPages <= 7) {
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }

  // Near the start: 1, 2, 3, 4, 5, '...', totalPages
  if (currentPage <= 4) {
    return [1, 2, 3, 4, 5, "...", totalPages];
  }

  // Near the end: 1, '...', totalPages-4, totalPages-3, totalPages-2, totalPages-1, totalPages
  if (currentPage >= totalPages - 3) {
    return [
      1,
      "...",
      totalPages - 4,
      totalPages - 3,
      totalPages - 2,
      totalPages - 1,
      totalPages,
    ];
  }

  // In the middle: 1, '...', current-1, current, current+1, '...', totalPages
  return [1, "...", currentPage - 1, currentPage, currentPage + 1, "...", totalPages];
}

export function Pagination({
  currentPage,
  totalPages,
  totalItems,
  itemsPerPage,
  createPageHref,
  onPageClick,
}: PaginationProps) {
  if (totalItems <= 0) {
    return null;
  }

  const startItem = (currentPage - 1) * itemsPerPage + 1;
  const endItem = Math.min(currentPage * itemsPerPage, totalItems);

  const range = getPaginationRange(currentPage, totalPages);

  const isFirstPage = currentPage <= 1;
  const isLastPage = currentPage >= totalPages;

  const handleClick = (e: React.MouseEvent, page: number) => {
    if (onPageClick) {
      onPageClick(page);
    }
  };

  return (
    <div className="flex flex-col sm:flex-row items-center justify-between gap-4 mt-12 pt-6 border-t border-[#DCEAF2]">
      {/* Result Count */}
      <div className="text-xs sm:text-sm text-[#5B7185] order-2 sm:order-1 text-center sm:text-left">
        Showing <span className="font-bold text-[#12304A]">{startItem}–{endItem}</span> of{" "}
        <span className="font-bold text-[#12304A]">{totalItems}</span> packages
        {totalPages > 1 && (
          <span className="text-xs text-[#8FA2B2] ml-1.5 hidden md:inline">
            (Page {currentPage} of {totalPages})
          </span>
        )}
      </div>

      {/* Pagination Controls */}
      {totalPages > 1 ? (
        <nav
          aria-label="Pagination Navigation"
          className="flex items-center gap-1 sm:gap-1.5 flex-wrap justify-center order-1 sm:order-2"
        >
          {/* Previous Button */}
          {isFirstPage ? (
            <button
              type="button"
              disabled
              aria-disabled="true"
              className="inline-flex items-center gap-1 px-3 py-2 rounded-lg text-xs font-semibold text-[#8FA2B2] bg-[#F1F6F9] border border-[#DCEAF2] cursor-not-allowed select-none opacity-60"
            >
              <svg
                className="w-3.5 h-3.5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
              <span>Previous</span>
            </button>
          ) : (
            <Link
              href={createPageHref(currentPage - 1)}
              onClick={(e) => handleClick(e, currentPage - 1)}
              className="inline-flex items-center gap-1 px-3 py-2 rounded-lg text-xs font-semibold text-[#12304A] bg-white hover:bg-[#EAF8FB] hover:text-[#0EA5C6] border border-[#DCEAF2] transition-colors shadow-xs"
              aria-label="Go to previous page"
            >
              <svg
                className="w-3.5 h-3.5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
              <span>Previous</span>
            </Link>
          )}

          {/* Numbered Page Buttons & Ellipses */}
          <div className="flex items-center gap-1 sm:gap-1.5">
            {range.map((item, index) => {
              if (item === "...") {
                return (
                  <span
                    key={`ellipsis-${index}`}
                    className="min-w-[32px] sm:min-w-[36px] h-8 sm:h-9 px-1 flex items-center justify-center text-xs font-semibold text-[#8FA2B2] select-none"
                    aria-hidden="true"
                  >
                    …
                  </span>
                );
              }

              const pageNum = Number(item);
              const isActive = pageNum === currentPage;

              if (isActive) {
                return (
                  <span
                    key={pageNum}
                    aria-current="page"
                    className="min-w-[32px] sm:min-w-[36px] h-8 sm:h-9 px-2 sm:px-3 flex items-center justify-center rounded-lg text-xs font-bold text-white bg-[#0EA5C6] shadow-xs select-none"
                  >
                    {pageNum}
                  </span>
                );
              }

              return (
                <Link
                  key={pageNum}
                  href={createPageHref(pageNum)}
                  onClick={(e) => handleClick(e, pageNum)}
                  className="min-w-[32px] sm:min-w-[36px] h-8 sm:h-9 px-2 sm:px-3 flex items-center justify-center rounded-lg text-xs font-semibold text-[#12304A] bg-white hover:bg-[#EAF8FB] hover:text-[#0EA5C6] border border-[#DCEAF2] transition-colors shadow-xs"
                  aria-label={`Go to page ${pageNum}`}
                >
                  {pageNum}
                </Link>
              );
            })}
          </div>

          {/* Next Button */}
          {isLastPage ? (
            <button
              type="button"
              disabled
              aria-disabled="true"
              className="inline-flex items-center gap-1 px-3 py-2 rounded-lg text-xs font-semibold text-[#8FA2B2] bg-[#F1F6F9] border border-[#DCEAF2] cursor-not-allowed select-none opacity-60"
            >
              <span>Next</span>
              <svg
                className="w-3.5 h-3.5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </button>
          ) : (
            <Link
              href={createPageHref(currentPage + 1)}
              onClick={(e) => handleClick(e, currentPage + 1)}
              className="inline-flex items-center gap-1 px-3 py-2 rounded-lg text-xs font-semibold text-[#12304A] bg-white hover:bg-[#EAF8FB] hover:text-[#0EA5C6] border border-[#DCEAF2] transition-colors shadow-xs"
              aria-label="Go to next page"
            >
              <span>Next</span>
              <svg
                className="w-3.5 h-3.5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </Link>
          )}
        </nav>
      ) : null}
    </div>
  );
}
