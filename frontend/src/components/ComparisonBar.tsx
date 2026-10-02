"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useCompare } from "@/context/CompareContext";

export function ComparisonBar() {
  const pathname = usePathname();
  const {
    selectedPackages,
    travellersCount,
    warningMessage,
    removePackage,
    clearPackages,
    dismissWarning,
  } = useCompare();

  // Hide bar on the compare page itself or when 0 packages selected
  if (selectedPackages.length === 0 || pathname === "/compare") {
    return null;
  }

  const count = selectedPackages.length;
  const canCompare = count >= 2;
  const idsQuery = selectedPackages.map((p) => p.id).join(",");
  const compareHref = `/compare?ids=${idsQuery}&travellers=${travellersCount || 2}`;

  return (
    <aside
      aria-label="Package Comparison Dock"
      className="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-[#DCEAF2] shadow-2xl transition-all duration-300 animate-in slide-in-from-bottom-4"
    >
      {/* Toast / Warning Banner */}
      {warningMessage && (
        <div className="bg-[#FFF4EC] border-b border-[#FF8A4C]/30 px-4 py-2 flex items-center justify-between text-xs text-[#12304A]">
          <div className="flex items-center gap-2 font-semibold text-[#FF8A4C]">
            <svg className="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <span>{warningMessage}</span>
          </div>
          <button
            onClick={dismissWarning}
            className="text-[#5B7185] hover:text-[#12304A] text-xs font-bold px-1.5 py-0.5"
            aria-label="Dismiss warning"
          >
            ✕
          </button>
        </div>
      )}

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-3.5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 sm:gap-4">
          {/* Left: Count & Chips */}
          <div className="flex flex-1 items-center gap-3 overflow-hidden">
            <div className="shrink-0 flex items-center gap-2">
              <span className="w-7 h-7 rounded-lg bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2] flex items-center justify-center font-bold text-xs">
                {count}/3
              </span>
              <span className="text-xs font-bold text-[#12304A] hidden md:inline">
                Compare Packages
              </span>
            </div>

            {/* Selected Package Chips */}
            <div className="flex items-center gap-2 overflow-x-auto py-1 scrollbar-none no-scrollbar">
              {selectedPackages.map((pkg) => (
                <div
                  key={pkg.id}
                  className="shrink-0 inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#F6FBFF] border border-[#DCEAF2] text-xs font-medium text-[#12304A] shadow-xs"
                >
                  <span className="max-w-[140px] sm:max-w-[200px] truncate" title={pkg.name}>
                    {pkg.name}
                  </span>
                  <button
                    onClick={() => removePackage(pkg.id)}
                    className="w-4 h-4 rounded-full hover:bg-[#DCEAF2] text-[#5B7185] hover:text-rose-600 inline-flex items-center justify-center text-xs transition-colors"
                    aria-label={`Remove ${pkg.name} from comparison`}
                  >
                    ✕
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Right: Actions */}
          <div className="flex items-center justify-end gap-2.5 shrink-0">
            {/* Helper text if only 1 package */}
            {!canCompare && (
              <span className="text-[11px] sm:text-xs text-[#5B7185] font-medium hidden xs:inline">
                Select at least 2 packages to compare.
              </span>
            )}

            <button
              onClick={clearPackages}
              className="px-3 py-2 rounded-xl text-xs font-semibold text-[#5B7185] hover:text-rose-600 hover:bg-rose-50 transition-colors"
            >
              Clear All
            </button>

            {canCompare ? (
              <Link
                href={compareHref}
                className="inline-flex items-center gap-1.5 px-5 py-2 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-xs sm:text-sm shadow-md shadow-[#0EA5C6]/20 transition-all hover:scale-[1.02]"
              >
                <span>Compare Now</span>
                <span className="px-1.5 py-0.2 rounded-md bg-white/20 text-white text-xs font-mono">
                  {count}
                </span>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </Link>
            ) : (
              <button
                disabled
                className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-[#DCEAF2] text-[#5B7185] font-bold text-xs sm:text-sm cursor-not-allowed opacity-80"
                title="Select at least 2 packages to compare"
              >
                <span>Compare Now</span>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </button>
            )}
          </div>
        </div>

        {/* Mobile-only helper if 1 package selected */}
        {!canCompare && (
          <p className="mt-1 text-[11px] text-[#5B7185] font-medium text-center xs:hidden">
            Select at least 2 packages to compare.
          </p>
        )}
      </div>
    </aside>
  );
}
