"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";
import { PackageSummary } from "@/types";
import { Badge } from "./Badge";
import { useCompare } from "@/context/CompareContext";

interface PackageCardProps {
  packageData: PackageSummary;
  requestedTravellers?: number;
  searchQuery?: string;
}

export function PackageCard({
  packageData,
  requestedTravellers = 1,
  searchQuery = "",
}: PackageCardProps) {
  const { isInCompare, addPackage, removePackage, setTravellersCount } = useCompare();
  const inCompare = isInCompare(packageData.id);
  const [isWhyMatchesExpanded, setIsWhyMatchesExpanded] = React.useState(false);

  const fallbackImage =
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80";

  const totalCost =
    packageData.estimated_total_cost ||
    Math.round(packageData.price_per_person * requestedTravellers);

  const detailsParams = new URLSearchParams(searchQuery || "");
  if (!detailsParams.has("travellers")) {
    detailsParams.set("travellers", String(requestedTravellers));
  }
  const detailsHref = `/packages/${packageData.id}?${detailsParams.toString()}`;

  const hasExplanations =
    (packageData.match_reasons && packageData.match_reasons.length > 0) ||
    (packageData.mismatches && packageData.mismatches.length > 0);

  const handleCompareClick = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();

    if (inCompare) {
      removePackage(packageData.id);
    } else {
      setTravellersCount(requestedTravellers);
      addPackage({
        id: packageData.id,
        name: packageData.name,
        destinationName: packageData.destination?.name,
        startingCity: packageData.starting_city,
        pricePerPerson: packageData.price_per_person,
      });
    }
  };

  return (
    <article
      className={`group rounded-2xl bg-white border transition-all duration-300 overflow-hidden flex flex-col shadow-sm hover:shadow-xl hover:shadow-sky-950/5 ${
        inCompare
          ? "border-[#0EA5C6] ring-2 ring-[#0EA5C6]/20 bg-[#F6FBFF]/30"
          : "border-[#DCEAF2] hover:border-[#0EA5C6]/40"
      }`}
    >
      {/* Package Header Image */}
      <div className="relative h-48 w-full overflow-hidden bg-slate-100">
        <Image
          src={packageData.featured_image_url || fallbackImage}
          alt={packageData.name}
          fill
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          className="object-cover group-hover:scale-105 transition-transform duration-500"
          unoptimized
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[#12304A]/60 via-transparent to-transparent" />

        {/* Duration & Source badges */}
        <div className="absolute top-3 left-3 flex flex-col gap-1.5 items-start">
          <span className="px-2.5 py-1 rounded-md text-xs font-semibold bg-white/90 text-[#12304A] backdrop-blur-md border border-white/60 shadow-xs">
            ⏱ {packageData.duration_days} Days / {packageData.duration_nights} Nights
          </span>
          <span className="px-2 py-0.5 rounded text-[10px] font-medium bg-[#12304A]/75 text-white/90 backdrop-blur-md border border-white/20 shadow-xs">
            {packageData.source_type === "live"
              ? `Live • ${packageData.provider || "Partner"}`
              : "Demo Package"}
          </span>
        </div>

        {/* Top right badges: Match Score & Over Budget & Compare */}
        <div className="absolute top-3 right-3 flex flex-col items-end gap-1.5">
          {inCompare && (
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-[#0EA5C6] text-white shadow-xs flex items-center gap-1">
              ✓ In Compare
            </span>
          )}
          {packageData.match_score !== undefined && (
            <span className="px-2.5 py-1 rounded-md text-xs font-bold bg-[#EAF8FB]/95 text-[#0EA5C6] backdrop-blur-md border border-[#DCEAF2] shadow-xs">
              {packageData.match_score} / 100 Match
            </span>
          )}
          {packageData.budget_status === "over_budget" && (
            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-[#FF8A4C] text-white shadow-xs">
              {packageData.budget_difference ? `+₹${Math.round(packageData.budget_difference).toLocaleString("en-IN")}` : "Over Budget"}
            </span>
          )}
        </div>

        {/* Starting City */}
        <div className="absolute bottom-3 left-3 text-xs font-semibold text-white bg-[#12304A]/80 px-2 py-0.5 rounded backdrop-blur-sm">
          Ex {packageData.starting_city}
        </div>
      </div>

      {/* Package Body */}
      <div className="p-5 flex-1 flex flex-col justify-between space-y-4">
        <div>
          {/* Destination & Operator */}
          <div className="flex items-center justify-between text-xs text-[#5B7185] mb-1.5">
            <span className="font-bold text-[#0EA5C6]">
              {packageData.destination
                ? `${packageData.destination.name}, ${packageData.destination.country}`
                : "Destination"}
            </span>
            {packageData.operator && (
              <span className="flex items-center gap-1 font-medium text-[#5B7185]">
                <span className="text-amber-500">★</span> {packageData.operator.rating.toFixed(1)}{" "}
                <span className="hidden sm:inline">({packageData.operator.name})</span>
              </span>
            )}
          </div>

          {/* Package Name */}
          <h3 className="text-lg font-bold text-[#12304A] group-hover:text-[#0EA5C6] transition-colors line-clamp-2">
            {packageData.name}
          </h3>

          {/* Themes Badges */}
          <div className="mt-3 flex flex-wrap gap-1.5">
            {packageData.themes.map((th) => (
              <Badge key={th.id} variant="primary">
                {th.name}
              </Badge>
            ))}
            {packageData.travel_types.map((tt) => (
              <Badge key={tt} variant="secondary">
                {tt}
              </Badge>
            ))}
          </div>

          {/* Expandable "Why this matches" Section */}
          {hasExplanations && (
            <div className="mt-3 pt-3 border-t border-slate-100">
              <button
                type="button"
                onClick={() => setIsWhyMatchesExpanded(!isWhyMatchesExpanded)}
                className="flex items-center justify-between w-full text-xs font-semibold text-[#0EA5C6] hover:text-[#0b8fae] transition-colors py-1 group/btn"
              >
                <span className="flex items-center gap-1.5">
                  <span className="underline decoration-dotted underline-offset-4">Why this matches</span>
                  {packageData.match_score !== undefined && (
                    <span className="text-[11px] font-medium text-[#5B7185]">
                      ({packageData.match_score}/100)
                    </span>
                  )}
                </span>
                <span className="text-[10px] text-[#5B7185] transition-transform duration-200">
                  {isWhyMatchesExpanded ? "▲ Hide" : "▼ Details"}
                </span>
              </button>

              {isWhyMatchesExpanded && (
                <div className="mt-2 text-xs space-y-2.5 bg-[#F6FBFF] rounded-xl p-3 border border-[#DCEAF2]">
                  {packageData.match_reasons && packageData.match_reasons.length > 0 && (
                    <div className="space-y-1.5">
                      <p className="text-[10px] font-bold uppercase tracking-wider text-[#12304A]">Match Reasons</p>
                      {packageData.match_reasons.map((reason, idx) => (
                        <div key={idx} className="flex items-start gap-1.5 text-[#12304A] leading-tight">
                          <span className="text-emerald-600 font-bold shrink-0">✓</span>
                          <span>{reason}</span>
                        </div>
                      ))}
                    </div>
                  )}

                  {packageData.mismatches && packageData.mismatches.length > 0 && (
                    <div className="pt-2 border-t border-[#DCEAF2] space-y-1.5">
                      <p className="text-[10px] font-bold uppercase tracking-wider text-amber-600">Possible Mismatch</p>
                      {packageData.mismatches.map((mismatch, idx) => (
                        <div key={idx} className="flex items-start gap-1.5 text-amber-900 leading-tight">
                          <span className="text-amber-500 font-bold shrink-0">!</span>
                          <span>{mismatch}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Pricing & CTA */}
        <div className="pt-3 border-t border-[#DCEAF2] flex flex-col gap-3">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-[11px] text-[#5B7185] font-semibold uppercase tracking-wider">Price per person</p>
              <p className="text-base font-bold text-[#12304A]">
                ₹{packageData.price_per_person.toLocaleString("en-IN")}
              </p>
            </div>
            {requestedTravellers > 1 && (
              <div className="text-right">
                <p className="text-[11px] text-[#5B7185] font-semibold uppercase tracking-wider">Total ({requestedTravellers} pax)</p>
                <p className="text-sm font-bold text-[#0EA5C6]">
                  ₹{totalCost.toLocaleString("en-IN")}
                </p>
              </div>
            )}
          </div>

          <div className="grid grid-cols-2 gap-2 pt-1">
            <button
              type="button"
              onClick={handleCompareClick}
              className={`inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold transition-all ${
                inCompare
                  ? "bg-[#EAF8FB] text-[#0EA5C6] border border-[#0EA5C6]/60 shadow-xs hover:bg-rose-50 hover:text-rose-600 hover:border-rose-300"
                  : "bg-white hover:bg-[#EAF8FB] text-[#12304A] border border-[#DCEAF2] shadow-xs"
              }`}
              title={inCompare ? "Click to remove from comparison" : "Add to comparison"}
            >
              {inCompare ? (
                <>
                  <span className="text-emerald-600 font-extrabold">✓</span>
                  <span>Added</span>
                </>
              ) : (
                <>
                  <span className="text-[#0EA5C6] font-bold">+</span>
                  <span>Add to Compare</span>
                </>
              )}
            </button>

            <Link
              href={detailsHref}
              className="inline-flex items-center justify-center gap-1 px-3 py-2 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-xs transition-colors shadow-sm text-center"
            >
              View Details
            </Link>
          </div>
        </div>
      </div>
    </article>
  );
}
