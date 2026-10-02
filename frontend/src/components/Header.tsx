"use client";

import React from "react";
import Link from "next/link";
import { useCompare } from "@/context/CompareContext";

export function Header() {
  const { selectedPackages, travellersCount } = useCompare();
  const compareCount = selectedPackages.length;
  const compareHref =
    compareCount > 0
      ? `/compare?ids=${selectedPackages.map((p) => p.id).join(",")}&travellers=${travellersCount || 2}`
      : "/compare";

  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-[#DCEAF2] shadow-xs">
      {/* Demo Notice Banner */}
      <div className="bg-[#EAF8FB] border-b border-[#DCEAF2] px-4 py-1.5 text-center text-xs text-[#12304A]">
        <span className="font-semibold text-[#0EA5C6]">DEMO PLATFORM:</span> Package details,
        itineraries, and pricing shown are realistic sample data for travel
        discovery testing.
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo / Brand */}
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#0EA5C6] to-[#14B8A6] flex items-center justify-center shadow-md shadow-[#0EA5C6]/20 group-hover:scale-105 transition-transform">
              <svg
                className="w-5 h-5 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2.5"
                  d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                />
              </svg>
            </div>
            <div>
              <span className="text-lg font-bold tracking-tight text-[#12304A] group-hover:text-[#0EA5C6] transition-colors">
                SmartTravel
              </span>
              <span className="hidden sm:inline-block ml-2 px-2 py-0.5 text-[10px] uppercase font-bold tracking-wider rounded-md bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
                MVP Discovery
              </span>
            </div>
          </Link>

          {/* Nav Links */}
          <nav className="flex items-center gap-1 sm:gap-2">
            <Link
              href="/"
              className="px-3.5 py-2 rounded-lg text-sm font-semibold text-[#5B7185] hover:text-[#0EA5C6] hover:bg-[#EAF8FB] transition-colors"
            >
              Plan Trip
            </Link>
            <Link
              href="/packages"
              className="px-3.5 py-2 rounded-lg text-sm font-semibold text-[#5B7185] hover:text-[#0EA5C6] hover:bg-[#EAF8FB] transition-colors"
            >
              All Packages
            </Link>
            <Link
              href={compareHref}
              className="px-3.5 py-2 rounded-lg text-sm font-semibold text-[#5B7185] hover:text-[#0EA5C6] hover:bg-[#EAF8FB] transition-colors inline-flex items-center gap-1.5"
            >
              <span>Compare</span>
              {compareCount > 0 && (
                <span className="px-1.5 py-0.2 rounded-md bg-[#0EA5C6] text-white text-[11px] font-bold leading-tight">
                  {compareCount}
                </span>
              )}
            </Link>
          </nav>
        </div>
      </div>
    </header>
  );
}
