"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";
import { DiscoveredDestination, SearchFormData } from "@/types";
import { MatchScoreBadge } from "./Badge";

interface DestinationCardProps {
  destination: DiscoveredDestination;
  searchParams: Partial<SearchFormData>;
}

export function DestinationCard({
  destination,
  searchParams,
}: DestinationCardProps) {
  const [isWhyDestExpanded, setIsWhyDestExpanded] = React.useState(false);

  // Construct the packages query while preserving user search parameters and adding destination_id
  const packageQuery = new URLSearchParams();
  if (searchParams.starting_city) packageQuery.set("starting_city", String(searchParams.starting_city));
  if (searchParams.budget) packageQuery.set("budget", String(searchParams.budget));
  if (searchParams.travellers) packageQuery.set("travellers", String(searchParams.travellers));
  if (searchParams.duration_days) packageQuery.set("duration_days", String(searchParams.duration_days));
  if (searchParams.interest) packageQuery.set("interest", String(searchParams.interest));
  if (searchParams.travel_type) packageQuery.set("travel_type", String(searchParams.travel_type));
  if (searchParams.month) packageQuery.set("month", String(searchParams.month));
  packageQuery.set("destination_id", String(destination.destination_id));

  const fallbackImage =
    "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=800&q=80";

  const hasExplanations =
    (destination.match_reasons && destination.match_reasons.length > 0) ||
    (destination.mismatches && destination.mismatches.length > 0);

  return (
    <div className="group rounded-2xl bg-white border border-[#DCEAF2] hover:border-[#0EA5C6]/40 transition-all duration-300 overflow-hidden flex flex-col shadow-sm hover:shadow-xl hover:shadow-sky-950/5">
      {/* Destination Image & Badges */}
      <div className="relative h-56 w-full overflow-hidden bg-slate-100">
        <Image
          src={destination.image_url || fallbackImage}
          alt={destination.destination_name}
          fill
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          className="object-cover group-hover:scale-105 transition-transform duration-500"
          unoptimized
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[#12304A]/90 via-[#12304A]/25 to-transparent" />

        {/* Top Badges */}
        <div className="absolute top-4 left-4 right-4 flex items-center justify-between">
          <MatchScoreBadge score={destination.match_score} />
          <span className="px-2.5 py-1 rounded-full text-xs font-semibold bg-white/90 text-[#12304A] backdrop-blur-md border border-white/60 shadow-xs">
            {destination.matching_package_count} {destination.matching_package_count === 1 ? "Package" : "Packages"}
          </span>
        </div>

        {/* Destination Location Info on Bottom of Image */}
        <div className="absolute bottom-3 left-4 right-4">
          <p className="text-xs uppercase tracking-wider font-semibold text-[#EAF8FB]">
            {destination.region ? `${destination.region}, ` : ""}
            {destination.country}
          </p>
          <h3 className="text-xl font-bold text-white group-hover:text-[#EAF8FB] transition-colors">
            {destination.destination_name}
          </h3>
        </div>
      </div>

      {/* Card Content Body */}
      <div className="p-5 flex-1 flex flex-col justify-between space-y-4">
        {/* Description snippet */}
        {destination.description && (
          <p className="text-xs text-[#5B7185] line-clamp-2 leading-relaxed">
            {destination.description}
          </p>
        )}

        {/* Best matching highlight */}
        <div className="rounded-xl bg-[#F6FBFF] border border-[#DCEAF2] p-3">
          <p className="text-[11px] uppercase tracking-wider font-semibold text-[#5B7185]">
            Best Matching Package:
          </p>
          <p className="text-xs font-bold text-[#12304A] truncate mt-0.5">
            {destination.best_matching_package_name}
          </p>
        </div>

        {/* Expandable "Why this destination?" Section */}
        {hasExplanations && (
          <div className="pt-2 border-t border-slate-100">
            <button
              type="button"
              onClick={() => setIsWhyDestExpanded(!isWhyDestExpanded)}
              className="flex items-center justify-between w-full text-xs font-semibold text-[#0EA5C6] hover:text-[#0b8fae] transition-colors py-1 group/btn"
            >
              <span className="flex items-center gap-1.5">
                <span className="underline decoration-dotted underline-offset-4">Why this destination?</span>
              </span>
              <span className="text-[10px] text-[#5B7185] transition-transform duration-200">
                {isWhyDestExpanded ? "▲ Hide" : "▼ Details"}
              </span>
            </button>

            {isWhyDestExpanded && (
              <div className="mt-2 text-xs space-y-2.5 bg-[#F6FBFF] rounded-xl p-3 border border-[#DCEAF2]">
                {destination.match_reasons && destination.match_reasons.length > 0 && (
                  <div className="space-y-1.5">
                    <p className="text-[10px] font-bold uppercase tracking-wider text-[#12304A]">Match Reasons</p>
                    {destination.match_reasons.map((reason, idx) => (
                      <div key={idx} className="flex items-start gap-1.5 text-[#12304A] leading-tight">
                        <span className="text-emerald-600 font-bold shrink-0">✓</span>
                        <span>{reason}</span>
                      </div>
                    ))}
                  </div>
                )}

                {destination.mismatches && destination.mismatches.length > 0 && (
                  <div className="pt-2 border-t border-[#DCEAF2] space-y-1.5">
                    <p className="text-[10px] font-bold uppercase tracking-wider text-amber-600">Possible Mismatch</p>
                    {destination.mismatches.map((mismatch, idx) => (
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

        {/* Pricing & CTA */}
        <div className="pt-2 border-t border-[#DCEAF2] flex items-end justify-between gap-3">
          <div>
            <p className="text-[11px] text-[#5B7185] uppercase font-semibold tracking-wider">
              Starting from
            </p>
            <p className="text-lg font-bold text-[#12304A]">
              ₹{destination.lowest_price_per_person.toLocaleString("en-IN")}{" "}
              <span className="text-xs font-normal text-[#5B7185]">/ person</span>
            </p>
            <p className="text-[11px] text-[#5B7185]">
              Total: ₹{destination.lowest_estimated_total_cost.toLocaleString("en-IN")}
            </p>
          </div>

          <Link
            href={`/packages?${packageQuery.toString()}`}
            className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-xs transition-all shadow-sm hover:gap-2"
          >
            <span>View Packages</span>
            <svg
              className="w-3.5 h-3.5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2.5"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </Link>
        </div>
      </div>
    </div>
  );
}
