"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";
import { PackageDetail } from "@/types";

interface ComparisonPackageHeaderProps {
  packageData: PackageDetail;
  travellers: number;
  onRemove: (id: number) => void;
}

export function ComparisonPackageHeader({
  packageData,
  travellers,
  onRemove,
}: ComparisonPackageHeaderProps) {
  const fallbackImage =
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80";

  return (
    <div className="flex flex-col h-full bg-white rounded-2xl border border-[#DCEAF2] p-4 sm:p-5 shadow-sm hover:shadow-md transition-shadow relative">
      {/* Top action: Remove button */}
      <div className="flex items-center justify-between mb-3">
        <span className="text-[11px] font-bold uppercase tracking-wider text-[#0EA5C6] bg-[#EAF8FB] px-2 py-0.5 rounded border border-[#DCEAF2]">
          Package #{packageData.id}
        </span>
        <button
          onClick={() => onRemove(packageData.id)}
          className="inline-flex items-center gap-1 text-xs font-semibold text-[#5B7185] hover:text-rose-600 transition-colors px-2 py-1 rounded-lg hover:bg-rose-50"
          title="Remove from comparison"
        >
          <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
          <span>Remove</span>
        </button>
      </div>

      {/* Package Image */}
      <div className="relative h-40 sm:h-44 w-full rounded-xl overflow-hidden bg-slate-100 mb-3.5">
        <Image
          src={packageData.featured_image_url || fallbackImage}
          alt={packageData.name}
          fill
          sizes="(max-width: 768px) 80vw, 33vw"
          className="object-cover"
          unoptimized
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[#12304A]/60 via-transparent to-transparent" />
        <div className="absolute bottom-2 left-2 text-[11px] font-semibold text-white bg-[#12304A]/80 px-2 py-0.5 rounded backdrop-blur-sm">
          Ex {packageData.starting_city}
        </div>
      </div>

      {/* Destination & Operator */}
      <div className="text-xs text-[#5B7185] flex items-center justify-between gap-1 mb-1">
        <span className="font-bold text-[#0EA5C6] truncate">
          {packageData.destination
            ? `${packageData.destination.name}, ${packageData.destination.country}`
            : "Destination"}
        </span>
        {packageData.operator && (
          <span className="flex items-center gap-1 font-semibold text-[#12304A] shrink-0">
            <span className="text-amber-500">★</span>
            {packageData.operator.rating.toFixed(1)}
          </span>
        )}
      </div>

      {/* Package Name */}
      <h3 className="text-base font-bold text-[#12304A] leading-snug line-clamp-2 min-h-[2.75rem] mb-1">
        {packageData.name}
      </h3>

      {/* Operator Name */}
      {packageData.operator && (
        <p className="text-xs text-[#5B7185] mb-4">
          By <strong className="text-[#12304A]">{packageData.operator.name}</strong>
        </p>
      )}

      {/* View Details CTA */}
      <div className="mt-auto pt-2">
        <Link
          href={`/packages/${packageData.id}?travellers=${travellers}`}
          className="w-full inline-flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white text-xs font-bold transition-colors shadow-xs"
        >
          <span>View Details</span>
          <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </Link>
      </div>
    </div>
  );
}
