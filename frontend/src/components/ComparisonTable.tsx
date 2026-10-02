"use client";

import React from "react";
import { PackageDetail } from "@/types";
import { Badge } from "./Badge";
import { ComparisonPackageHeader } from "./ComparisonPackageHeader";
import { ComparisonSection } from "./ComparisonSection";
import { ComparisonRow } from "./ComparisonRow";

interface ComparisonTableProps {
  packages: PackageDetail[];
  travellers: number;
  onRemovePackage: (id: number) => void;
}

const MONTH_NAMES: { [key: number]: string } = {
  1: "Jan",
  2: "Feb",
  3: "Mar",
  4: "Apr",
  5: "May",
  6: "Jun",
  7: "Jul",
  8: "Aug",
  9: "Sep",
  10: "Oct",
  11: "Nov",
  12: "Dec",
};

export function ComparisonTable({
  packages,
  travellers,
  onRemovePackage,
}: ComparisonTableProps) {
  const colSpan = packages.length + 1;

  return (
    <div className="w-full bg-white rounded-2xl border border-[#DCEAF2] shadow-sm overflow-hidden">
      {/* Scrollable table container */}
      <div className="overflow-x-auto w-full scrollbar-thin">
        <table className="w-full border-collapse text-left">
          {/* Header Row: Package cards */}
          <thead>
            <tr className="border-b border-[#DCEAF2] bg-[#F6FBFF]/30">
              <th
                scope="col"
                className="py-6 px-4 sm:px-6 align-bottom bg-white sticky left-0 z-20 border-r border-[#DCEAF2] min-w-[140px] sm:min-w-[180px] w-[180px] shadow-sm sm:shadow-none"
              >
                <div className="space-y-1">
                  <span className="text-[11px] font-bold uppercase tracking-wider text-[#0EA5C6]">
                    Side-by-Side
                  </span>
                  <h3 className="text-base sm:text-lg font-extrabold text-[#12304A]">
                    Comparing {packages.length} Packages
                  </h3>
                  <p className="text-xs text-[#5B7185]">
                    Standardized attributes for neutral evaluation.
                  </p>
                </div>
              </th>

              {packages.map((pkg) => (
                <th
                  key={pkg.id}
                  scope="col"
                  className="p-4 sm:p-5 align-top border-r last:border-r-0 border-[#DCEAF2] min-w-[260px] sm:min-w-[300px]"
                >
                  <ComparisonPackageHeader
                    packageData={pkg}
                    travellers={travellers}
                    onRemove={onRemovePackage}
                  />
                </th>
              ))}
            </tr>
          </thead>

          <tbody>
            {/* ================================================== */}
            {/* 1. BASIC INFORMATION (OVERVIEW) */}
            {/* ================================================== */}
            <ComparisonSection
              title="Basic Information"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Package Name"
              values={packages.map((pkg) => (
                <span key={pkg.id} className="font-bold text-[#12304A]">
                  {pkg.name}
                </span>
              ))}
            />

            <ComparisonRow
              label="Tour Operator"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="space-y-0.5">
                  <span className="font-semibold text-[#12304A]">
                    {pkg.operator ? pkg.operator.name : "Independent"}
                  </span>
                  {pkg.operator && pkg.operator.rating > 0 && (
                    <div className="flex items-center gap-1 text-xs text-[#5B7185]">
                      <span className="text-amber-500 font-bold">★ {pkg.operator.rating.toFixed(1)}</span>
                      <span>operator rating</span>
                    </div>
                  )}
                </div>
              ))}
            />

            <ComparisonRow
              label="Destination"
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  <span className="font-semibold text-[#0EA5C6]">
                    {pkg.destination?.name}
                  </span>
                  <span className="text-xs text-[#5B7185] block">
                    {pkg.destination?.region ? `${pkg.destination.region}, ` : ""}
                    {pkg.destination?.country}
                  </span>
                </div>
              ))}
            />

            <ComparisonRow
              label="Starting City"
              values={packages.map((pkg) => (
                <span key={pkg.id} className="font-medium text-[#12304A]">
                  Ex {pkg.starting_city}
                </span>
              ))}
            />

            <ComparisonRow
              label="Trip Duration"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="flex items-center gap-2">
                  <span className="px-2.5 py-1 rounded-md text-xs font-bold bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
                    ⏱ {pkg.duration_days} Days / {pkg.duration_nights} Nights
                  </span>
                </div>
              ))}
            />

            <ComparisonRow
              label="Travel Types"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="flex flex-wrap gap-1.5">
                  {pkg.travel_types && pkg.travel_types.length > 0 ? (
                    pkg.travel_types.map((tt, i) => (
                      <Badge key={i} variant="secondary">
                        {tt}
                      </Badge>
                    ))
                  ) : (
                    <span className="text-xs text-[#5B7185]">All travel types</span>
                  )}
                </div>
              ))}
            />

            {/* ================================================== */}
            {/* 2. PRICING */}
            {/* ================================================== */}
            <ComparisonSection
              title="Pricing & Budget"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Price per Person"
              sublabel="Base package rate"
              highlight
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  <span className="text-base sm:text-lg font-extrabold text-[#12304A]">
                    ₹{pkg.price_per_person.toLocaleString("en-IN")}
                  </span>
                  <span className="text-xs text-[#5B7185] ml-1">/ person</span>
                </div>
              ))}
            />

            <ComparisonRow
              label="Estimated Total Cost"
              sublabel={`Calculated for ${travellers} traveller${travellers > 1 ? "s" : ""}`}
              highlight
              values={packages.map((pkg) => {
                const total =
                  pkg.estimated_total_cost ||
                  Math.round(pkg.price_per_person * travellers);
                return (
                  <div key={pkg.id}>
                    <span className="text-lg sm:text-xl font-extrabold text-[#0EA5C6]">
                      ₹{total.toLocaleString("en-IN")}
                    </span>
                    <span className="block text-[11px] text-[#5B7185]">
                      total for {travellers} traveller{travellers > 1 ? "s" : ""}
                    </span>
                  </div>
                );
              })}
            />

            <ComparisonRow
              label="Match Score"
              sublabel="From deterministic search criteria"
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  {pkg.match_score !== undefined && pkg.match_score !== null ? (
                    <span className="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
                      {pkg.match_score} / 100 Match
                    </span>
                  ) : (
                    <span className="text-xs text-[#5B7185] italic">Not scored in search</span>
                  )}
                </div>
              ))}
            />

            <ComparisonRow
              label="Budget Status"
              values={packages.map((pkg) => {
                if (pkg.budget_status === "over_budget") {
                  return (
                    <div key={pkg.id} className="space-y-1">
                      <span className="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-[#FFF4EC] text-[#FF8A4C] border border-[#FF8A4C]/30">
                        Over budget
                      </span>
                      {pkg.budget_difference && (
                        <p className="text-xs text-[#FF8A4C] font-semibold">
                          +₹{Math.round(pkg.budget_difference).toLocaleString("en-IN")} difference
                        </p>
                      )}
                    </div>
                  );
                }
                if (pkg.budget_status === "within_budget") {
                  return (
                    <span
                      key={pkg.id}
                      className="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200"
                    >
                      Within budget
                    </span>
                  );
                }
                return (
                  <span key={pkg.id} className="text-xs text-[#5B7185]">
                    Standard pricing
                  </span>
                );
              })}
            />

            {/* ================================================== */}
            {/* 3. TRAVEL PREFERENCES */}
            {/* ================================================== */}
            <ComparisonSection
              title="Travel Preferences"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Themes & Interests"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="flex flex-wrap gap-1.5">
                  {pkg.themes && pkg.themes.length > 0 ? (
                    pkg.themes.map((th) => (
                      <Badge key={th.id} variant="primary">
                        {th.name}
                      </Badge>
                    ))
                  ) : (
                    <span className="text-xs text-[#5B7185]">—</span>
                  )}
                </div>
              ))}
            />

            <ComparisonRow
              label="Available Months"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="flex flex-wrap gap-1">
                  {pkg.available_months && pkg.available_months.length > 0 ? (
                    pkg.available_months.map((m) => (
                      <span
                        key={m}
                        className="px-2 py-0.5 rounded text-[11px] font-semibold bg-[#F6FBFF] text-[#12304A] border border-[#DCEAF2]"
                      >
                        {MONTH_NAMES[m] || m}
                      </span>
                    ))
                  ) : (
                    <span className="text-xs text-[#5B7185]">Year-round</span>
                  )}
                </div>
              ))}
            />

            {/* ================================================== */}
            {/* 4. PACKAGE INFORMATION */}
            {/* ================================================== */}
            <ComparisonSection
              title="Package Information"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Hotel Information"
              values={packages.map((pkg) => (
                <p key={pkg.id} className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
                  {pkg.hotel_info || "Standard accommodation included as per itinerary."}
                </p>
              ))}
            />

            <ComparisonRow
              label="Meals Information"
              values={packages.map((pkg) => (
                <p key={pkg.id} className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
                  {pkg.meals_info || "Included as specified in the day-by-day plan."}
                </p>
              ))}
            />

            <ComparisonRow
              label="Transportation"
              values={packages.map((pkg) => (
                <p key={pkg.id} className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
                  {pkg.transportation_info || "Transfers and sightseeing transportation included."}
                </p>
              ))}
            />

            <ComparisonRow
              label="Sightseeing"
              values={packages.map((pkg) => (
                <p key={pkg.id} className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
                  {pkg.sightseeing_info || "Curated sightseeing spots included in package."}
                </p>
              ))}
            />

            <ComparisonRow
              label="Activities"
              values={packages.map((pkg) => (
                <p key={pkg.id} className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
                  {pkg.activities_info || "Standard leisure & exploration activities."}
                </p>
              ))}
            />

            {/* ================================================== */}
            {/* 5. ITINERARY */}
            {/* ================================================== */}
            <ComparisonSection
              title="Day-by-Day Itinerary"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Day-by-Day Plan"
              sublabel="Chronological itinerary outline"
              values={packages.map((pkg) => (
                <div key={pkg.id} className="space-y-3">
                  {pkg.itinerary && pkg.itinerary.length > 0 ? (
                    pkg.itinerary.map((day) => (
                      <div
                        key={day.id || day.day_number}
                        className="p-3 rounded-xl bg-[#F6FBFF] border border-[#DCEAF2] space-y-1"
                      >
                        <div className="flex items-center gap-2">
                          <span className="text-[11px] font-bold uppercase tracking-wider text-[#0EA5C6] bg-[#EAF8FB] px-2 py-0.5 rounded border border-[#DCEAF2]">
                            Day {day.day_number}
                          </span>
                          <span className="text-xs font-bold text-[#12304A] line-clamp-1">
                            {day.title}
                          </span>
                        </div>
                        <p className="text-xs text-[#5B7185] line-clamp-2 leading-relaxed">
                          {day.description}
                        </p>
                        {(day.accommodation || day.meals_provided) && (
                          <div className="pt-1 flex flex-wrap gap-2 text-[11px] text-[#5B7185]">
                            {day.accommodation && (
                              <span>🏨 {day.accommodation}</span>
                            )}
                            {day.meals_provided && (
                              <span>🍽 {day.meals_provided}</span>
                            )}
                          </div>
                        )}
                      </div>
                    ))
                  ) : (
                    <span className="text-xs text-[#5B7185]">Detailed itinerary upon booking</span>
                  )}
                </div>
              ))}
            />

            {/* ================================================== */}
            {/* 6. INCLUSIONS */}
            {/* ================================================== */}
            <ComparisonSection
              title="Inclusions"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="What's Included"
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  {pkg.inclusions && pkg.inclusions.length > 0 ? (
                    <ul className="space-y-1.5 text-xs text-[#12304A]">
                      {pkg.inclusions.map((item, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-emerald-500 font-bold shrink-0">✓</span>
                          <span className="leading-snug">{item}</span>
                        </li>
                      ))}
                    </ul>
                  ) : (
                    <span className="text-xs text-[#5B7185]">Standard inclusions</span>
                  )}
                </div>
              ))}
            />

            {/* ================================================== */}
            {/* 7. EXCLUSIONS */}
            {/* ================================================== */}
            <ComparisonSection
              title="Exclusions"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="What's Excluded"
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  {pkg.exclusions && pkg.exclusions.length > 0 ? (
                    <ul className="space-y-1.5 text-xs text-[#5B7185]">
                      {pkg.exclusions.map((item, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-rose-500 font-bold shrink-0">✕</span>
                          <span className="leading-snug">{item}</span>
                        </li>
                      ))}
                    </ul>
                  ) : (
                    <span className="text-xs text-[#5B7185]">Personal expenses not included</span>
                  )}
                </div>
              ))}
            />

            {/* ================================================== */}
            {/* 8. REFERENCE */}
            {/* ================================================== */}
            <ComparisonSection
              title="Reference"
              icon={
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              }
              colSpan={colSpan}
            />

            <ComparisonRow
              label="Source Link"
              values={packages.map((pkg) => (
                <div key={pkg.id}>
                  <a
                    href={`/sources/packages/${pkg.id}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#0EA5C6] hover:underline"
                  >
                    <span>Demo Source</span>
                    <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </a>
                </div>
              ))}
            />
          </tbody>
        </table>
      </div>
    </div>
  );
}
