"use client";

import React, { Suspense, useEffect, useState, use } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { Badge } from "@/components/Badge";
import { ItineraryView } from "@/components/ItineraryView";
import { LoadingSpinner } from "@/components/LoadingState";
import { ErrorState } from "@/components/ErrorState";
import { PackageDetail } from "@/types";
import { fetchPackageDetail } from "@/services/api";
import { useCompare } from "@/context/CompareContext";

const MONTH_NAMES = [
  "",
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

function PackageDetailContent({ id }: { id: string }) {
  const searchParams = useSearchParams();
  const travellersParam = Number(searchParams.get("travellers")) || 1;

  const starting_city = searchParams.get("starting_city") || "";
  const budget = searchParams.get("budget") || "";
  const duration_days = searchParams.get("duration_days") || "";
  const interest = searchParams.get("interest") || "";
  const travel_type = searchParams.get("travel_type") || "";
  const month = searchParams.get("month") || "";
  const destination_id = searchParams.get("destination_id") || "";

  const [travellers, setTravellers] = useState<number>(travellersParam);
  const [packageDetail, setPackageDetail] = useState<PackageDetail | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshKey, setRefreshKey] = useState<number>(0);

  const { isInCompare, addPackage, removePackage, setTravellersCount } = useCompare();
  const inCompare = packageDetail ? isInCompare(packageDetail.id) : false;

  const handleCompareToggle = () => {
    if (!packageDetail) return;
    if (inCompare) {
      removePackage(packageDetail.id);
    } else {
      setTravellersCount(travellers);
      addPackage({
        id: packageDetail.id,
        name: packageDetail.name,
        destinationName: packageDetail.destination?.name,
        startingCity: packageDetail.starting_city,
        pricePerPerson: packageDetail.price_per_person,
      });
    }
  };

  const backParams = new URLSearchParams();
  if (starting_city) backParams.set("starting_city", starting_city);
  if (budget) backParams.set("budget", budget);
  if (travellers) backParams.set("travellers", String(travellers));
  if (duration_days) backParams.set("duration_days", duration_days);
  if (interest) backParams.set("interest", interest);
  if (travel_type) backParams.set("travel_type", travel_type);
  if (month) backParams.set("month", month);
  if (destination_id) backParams.set("destination_id", destination_id);

  const backHref = backParams.toString() ? `/packages?${backParams.toString()}` : "/packages";

  useEffect(() => {
    let cancelled = false;

    fetchPackageDetail(id, travellers)
      .then((data) => {
        if (!cancelled) {
          setPackageDetail(data);
          setError(null);
        }
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          const msg = err instanceof Error ? err.message : "Failed to load package details.";
          setError(msg);
        }
      })
      .finally(() => {
        if (!cancelled) {
          setLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [id, travellers, refreshKey]);

  if (loading) {
    return <LoadingSpinner message="Loading complete package itinerary and details..." />;
  }

  if (error || !packageDetail) {
    return (
      <div className="max-w-3xl mx-auto py-16 px-4">
        <ErrorState
          title="Could not load package"
          message={error || "Package details unavailable"}
          onRetry={() => {
            setLoading(true);
            setRefreshKey((k) => k + 1);
          }}
        />
      </div>
    );
  }

  const fallbackImage =
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80";

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Back Button & Breadcrumbs */}
      <div className="flex items-center justify-between mb-6">
        <Link
          href={backHref}
          className="inline-flex items-center gap-2 text-sm text-[#5B7185] hover:text-[#12304A] transition-colors font-medium"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          <span>Back to Packages</span>
        </Link>

        <div className="flex items-center gap-2">
          {inCompare && (
            <span className="text-xs font-bold px-2.5 py-1 rounded bg-[#EAF8FB] text-[#0EA5C6] border border-[#0EA5C6]/30 flex items-center gap-1">
              ✓ In Comparison
            </span>
          )}
          <span className="text-xs font-semibold px-2.5 py-1 rounded bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
            Package #{packageDetail.id}
          </span>
        </div>
      </div>

      {/* Main Title Header */}
      <div className="mb-8">
        <div className="flex flex-wrap items-center gap-2 mb-2">
          <Badge variant="primary">
            {packageDetail.destination?.name}, {packageDetail.destination?.country}
          </Badge>
          <span className="text-xs text-[#DCEAF2]">•</span>
          <span className="text-xs text-[#5B7185] font-medium">Ex {packageDetail.starting_city}</span>
          <span className="text-xs text-[#DCEAF2]">•</span>
          <span className="text-xs text-[#5B7185] font-medium">
            ⏱ {packageDetail.duration_days} Days / {packageDetail.duration_nights} Nights
          </span>
        </div>

        <h1 className="text-3xl sm:text-4xl font-extrabold text-[#12304A] tracking-tight">
          {packageDetail.name}
        </h1>

        {/* Operator subtitle */}
        {packageDetail.operator && (
          <div className="mt-2 flex items-center gap-3 text-sm text-[#5B7185]">
            <span>
              Curated by <strong className="text-[#12304A]">{packageDetail.operator.name}</strong>
            </span>
            <span className="inline-flex items-center gap-1 text-amber-700 font-semibold text-xs bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
              ★ {packageDetail.operator.rating.toFixed(1)}
            </span>
          </div>
        )}
      </div>

      {/* Grid Layout: Main Details + Sidebar */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column (2 Cols): Media, Overview, Info, Itinerary, Inclusions */}
        <div className="lg:col-span-2 space-y-10">
          {/* Featured Hero Image */}
          <div className="relative h-72 sm:h-96 w-full rounded-2xl overflow-hidden bg-white border border-[#DCEAF2] shadow-xl shadow-sky-950/5">
            <Image
              src={packageDetail.featured_image_url || fallbackImage}
              alt={packageDetail.name}
              fill
              priority
              sizes="(max-width: 1024px) 100vw, 66vw"
              className="object-cover"
              unoptimized
            />
          </div>

          {/* Key Overview Cards */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 p-5 rounded-2xl bg-white border border-[#DCEAF2] shadow-sm">
            <div>
              <p className="text-[11px] font-semibold text-[#5B7185] uppercase tracking-wider">Departure</p>
              <p className="text-sm font-bold text-[#12304A] mt-1">{packageDetail.starting_city}</p>
            </div>
            <div>
              <p className="text-[11px] font-semibold text-[#5B7185] uppercase tracking-wider">Duration</p>
              <p className="text-sm font-bold text-[#12304A] mt-1">
                {packageDetail.duration_days}D / {packageDetail.duration_nights}N
              </p>
            </div>
            <div>
              <p className="text-[11px] font-semibold text-[#5B7185] uppercase tracking-wider">Travel Styles</p>
              <p className="text-sm font-bold text-[#0EA5C6] mt-1">
                {packageDetail.travel_types.join(", ") || "General"}
              </p>
            </div>
            <div>
              <p className="text-[11px] font-semibold text-[#5B7185] uppercase tracking-wider">Best Months</p>
              <p className="text-sm font-bold text-[#12304A] mt-1 truncate">
                {packageDetail.available_months.map((m) => MONTH_NAMES[m]?.slice(0, 3)).join(", ")}
              </p>
            </div>
          </div>

          {/* Accommodation & Tour Highlights */}
          <section className="space-y-4">
            <h2 className="text-xl font-bold text-[#12304A] tracking-tight border-b border-[#DCEAF2] pb-3">
              Tour Specifications
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
              {packageDetail.hotel_info && (
                <div className="rounded-xl bg-white border border-[#DCEAF2] p-4 shadow-sm">
                  <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#0EA5C6] mb-1">
                    🏨 Accommodation
                  </div>
                  <p className="text-[#5B7185] text-xs leading-relaxed">{packageDetail.hotel_info}</p>
                </div>
              )}

              {packageDetail.meals_info && (
                <div className="rounded-xl bg-white border border-[#DCEAF2] p-4 shadow-sm">
                  <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#FF8A4C] mb-1">
                    🍴 Meals & Dining
                  </div>
                  <p className="text-[#5B7185] text-xs leading-relaxed">{packageDetail.meals_info}</p>
                </div>
              )}

              {packageDetail.transportation_info && (
                <div className="rounded-xl bg-white border border-[#DCEAF2] p-4 shadow-sm">
                  <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#0EA5C6] mb-1">
                    🚐 Transport & Transfers
                  </div>
                  <p className="text-[#5B7185] text-xs leading-relaxed">{packageDetail.transportation_info}</p>
                </div>
              )}

              {packageDetail.sightseeing_info && (
                <div className="rounded-xl bg-white border border-[#DCEAF2] p-4 shadow-sm">
                  <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#14B8A6] mb-1">
                    📷 Sightseeing Included
                  </div>
                  <p className="text-[#5B7185] text-xs leading-relaxed">{packageDetail.sightseeing_info}</p>
                </div>
              )}
            </div>

            {packageDetail.activities_info && (
              <div className="rounded-xl bg-white border border-[#DCEAF2] p-4 shadow-sm">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#FF8A4C] mb-1">
                  🎯 Activities & Experiences
                </div>
                <p className="text-[#5B7185] text-xs leading-relaxed">{packageDetail.activities_info}</p>
              </div>
            )}
          </section>

          {/* Day-by-Day Itinerary */}
          <section className="space-y-4">
            <h2 className="text-xl font-bold text-[#12304A] tracking-tight border-b border-[#DCEAF2] pb-3">
              Day-by-Day Itinerary
            </h2>
            <ItineraryView itinerary={packageDetail.itinerary} />
          </section>

          {/* Inclusions and Exclusions */}
          <section className="space-y-6">
            <h2 className="text-xl font-bold text-[#12304A] tracking-tight border-b border-[#DCEAF2] pb-3">
              Package Terms & Provisions
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Inclusions */}
              <div className="rounded-2xl bg-teal-50/60 border border-teal-200/80 p-5">
                <h3 className="text-sm font-bold uppercase tracking-wider text-[#14B8A6] mb-3 flex items-center gap-2">
                  <span className="w-5 h-5 rounded-full bg-[#14B8A6] text-white flex items-center justify-center text-xs">✓</span>
                  Inclusions
                </h3>
                <ul className="space-y-2.5 text-xs text-[#12304A]">
                  {packageDetail.inclusions?.map((inc, i) => (
                    <li key={i} className="flex items-start gap-2">
                      <span className="text-[#14B8A6] font-bold shrink-0">•</span>
                      <span>{inc}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Exclusions */}
              <div className="rounded-2xl bg-rose-50/40 border border-rose-200/80 p-5">
                <h3 className="text-sm font-bold uppercase tracking-wider text-rose-600 mb-3 flex items-center gap-2">
                  <span className="w-5 h-5 rounded-full bg-rose-100 text-rose-600 border border-rose-200 flex items-center justify-center text-xs">✕</span>
                  Exclusions
                </h3>
                <ul className="space-y-2.5 text-xs text-[#5B7185]">
                  {packageDetail.exclusions?.map((exc, i) => (
                    <li key={i} className="flex items-start gap-2">
                      <span className="text-rose-500 font-bold shrink-0">•</span>
                      <span>{exc}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </section>
        </div>

        {/* Right Column: Pricing Box & Operator Info */}
        <div className="space-y-6">
          {/* Pricing Box Sticky */}
          <div className="sticky top-24 rounded-2xl bg-white border border-[#DCEAF2] p-6 shadow-xl shadow-sky-950/5 space-y-6">
            <div>
              <p className="text-xs uppercase font-semibold tracking-wider text-[#5B7185]">Estimated Cost</p>
              <div className="mt-1 flex items-baseline gap-2">
                <span className="text-3xl font-extrabold text-[#0EA5C6]">
                  ₹{packageDetail.price_per_person.toLocaleString("en-IN")}
                </span>
                <span className="text-xs text-[#5B7185]">/ person</span>
              </div>
            </div>

            {/* Travellers modifier */}
            <div className="p-3.5 rounded-xl bg-[#F6FBFF] border border-[#DCEAF2]">
              <label htmlFor="pax" className="block text-xs font-semibold text-[#5B7185] mb-1.5">
                Calculating for travellers:
              </label>
              <div className="flex items-center gap-3">
                <input
                  id="pax"
                  type="number"
                  min="1"
                  max="30"
                  value={travellers}
                  onChange={(e) => setTravellers(Math.max(1, Number(e.target.value) || 1))}
                  className="w-20 bg-white border border-[#DCEAF2] rounded-lg px-3 py-1.5 text-sm font-bold text-[#12304A] text-center focus:outline-none focus:ring-2 focus:ring-[#0EA5C6]"
                />
                <span className="text-xs text-[#5B7185]">person(s)</span>
              </div>
              <div className="mt-3 pt-3 border-t border-[#DCEAF2] flex justify-between items-center text-xs">
                <span className="text-[#5B7185]">Total Estimated Trip Cost:</span>
                <span className="text-sm font-bold text-[#12304A]">
                  ₹{packageDetail.estimated_total_cost.toLocaleString("en-IN")}
                </span>
              </div>
            </div>

            {/* Compare Control Button */}
            <button
              type="button"
              onClick={handleCompareToggle}
              className={`w-full py-2.5 px-4 rounded-xl font-bold text-xs sm:text-sm flex items-center justify-center gap-2 transition-all shadow-xs ${
                inCompare
                  ? "bg-[#EAF8FB] text-[#0EA5C6] border border-[#0EA5C6]/60 hover:bg-rose-50 hover:text-rose-600 hover:border-rose-300"
                  : "bg-white hover:bg-[#EAF8FB] text-[#12304A] border border-[#DCEAF2] hover:border-[#0EA5C6]/50"
              }`}
              title={inCompare ? "Click to remove from comparison" : "Add to comparison"}
            >
              {inCompare ? (
                <>
                  <span className="text-emerald-600 font-extrabold text-sm">✓</span>
                  <span>Added to Compare</span>
                  <span className="text-[11px] text-[#5B7185] font-normal ml-1">(click to remove)</span>
                </>
              ) : (
                <>
                  <span className="text-[#0EA5C6] font-bold text-base">+</span>
                  <span>Add to Compare</span>
                </>
              )}
            </button>

            {/* Themes list */}
            <div>
              <p className="text-xs font-semibold text-[#5B7185] uppercase tracking-wider mb-2">Package Themes</p>
              <div className="flex flex-wrap gap-1.5">
                {packageDetail.themes.map((th) => (
                  <Badge key={th.id} variant="primary">
                    {th.name}
                  </Badge>
                ))}
              </div>
            </div>

            {/* Operator Card */}
            {packageDetail.operator && (
              <div className="pt-4 border-t border-[#DCEAF2] text-xs space-y-1.5">
                <p className="text-[11px] uppercase font-bold tracking-wider text-[#5B7185]">Tour Operator</p>
                <div className="flex items-center justify-between">
                  <p className="font-bold text-[#12304A] text-sm">{packageDetail.operator.name}</p>
                  {packageDetail.operator.rating > 0 && (
                    <span className="flex items-center gap-1 text-amber-700 font-semibold text-xs bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
                      ★ {packageDetail.operator.rating.toFixed(1)}
                    </span>
                  )}
                </div>
              </div>
            )}

            {/* Source Reference Link */}
            <div className="pt-4 border-t border-[#DCEAF2] text-xs">
              <a
                href={`/sources/packages/${packageDetail.id}`}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 text-xs text-[#5B7185] hover:text-[#0EA5C6] transition-colors font-semibold"
              >
                <span>Demo Source</span>
                <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function PackageDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const unwrappedParams = use(params);

  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A]">
      <Header />
      <main className="flex-1">
        <Suspense fallback={<LoadingSpinner message="Loading package..." />}>
          <PackageDetailContent id={unwrappedParams.id} />
        </Suspense>
      </main>
      <Footer />
    </div>
  );
}
