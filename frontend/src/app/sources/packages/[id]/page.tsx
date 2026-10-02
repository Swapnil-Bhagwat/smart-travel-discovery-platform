"use client";

import React, { Suspense, useEffect, useState, use } from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { Badge } from "@/components/Badge";
import { LoadingSpinner } from "@/components/LoadingState";
import { ErrorState } from "@/components/ErrorState";
import { PackageDetail } from "@/types";
import { fetchPackageDetail } from "@/services/api";

function DemoSourceContent({ id }: { id: string }) {
  const [packageDetail, setPackageDetail] = useState<PackageDetail | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshKey, setRefreshKey] = useState<number>(0);

  useEffect(() => {
    let cancelled = false;

    fetchPackageDetail(id)
      .then((data) => {
        if (!cancelled) {
          setPackageDetail(data);
          setError(null);
        }
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          const msg = err instanceof Error ? err.message : "Failed to load package information.";
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
  }, [id, refreshKey]);

  if (loading) {
    return <LoadingSpinner message="Loading demo source information..." />;
  }

  if (error || !packageDetail) {
    return (
      <div className="max-w-3xl mx-auto py-16 px-4">
        <ErrorState
          title="Could not load demo source"
          message={error || "Package information is currently unavailable."}
          onRetry={() => {
            setLoading(true);
            setRefreshKey((k) => k + 1);
          }}
        />
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Breadcrumb & Navigation */}
      <div className="flex items-center justify-between mb-8">
        <Link
          href={`/packages/${packageDetail.id}`}
          className="inline-flex items-center gap-2 text-sm text-[#5B7185] hover:text-[#0EA5C6] transition-colors font-semibold"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          <span>Back to Package</span>
        </Link>

        <span className="text-xs font-bold px-2.5 py-1 rounded bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
          Demo Source Record #{packageDetail.id}
        </span>
      </div>

      {/* Main Card */}
      <div className="bg-white rounded-2xl border border-[#DCEAF2] p-6 sm:p-10 shadow-sm space-y-8">
        {/* Header Information */}
        <div>
          <div className="flex flex-wrap items-center gap-2 mb-3">
            <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold uppercase tracking-wider bg-[#FFF4EC] text-[#FF8A4C] border border-[#FF8A4C]/30">
              Platform Demonstration Dataset
            </span>
            {packageDetail.destination && (
              <Badge variant="primary">
                {packageDetail.destination.name}, {packageDetail.destination.country}
              </Badge>
            )}
          </div>

          <h1 className="text-2xl sm:text-3xl font-extrabold text-[#12304A] tracking-tight">
            {packageDetail.name}
          </h1>

          <div className="mt-3 flex flex-wrap items-center gap-4 text-xs sm:text-sm text-[#5B7185]">
            {packageDetail.operator && (
              <div>
                Tour Operator: <strong className="text-[#12304A]">{packageDetail.operator.name}</strong>
                {packageDetail.operator.rating > 0 && (
                  <span className="ml-1.5 text-amber-700 font-semibold text-xs bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
                    ★ {packageDetail.operator.rating.toFixed(1)}
                  </span>
                )}
              </div>
            )}
            <span>•</span>
            <div>
              Starting City: <strong className="text-[#12304A]">{packageDetail.starting_city}</strong>
            </div>
            <span>•</span>
            <div>
              Duration: <strong className="text-[#12304A]">{packageDetail.duration_days} Days / {packageDetail.duration_nights} Nights</strong>
            </div>
          </div>
        </div>

        {/* Clear Demonstration Notice Box */}
        <div className="rounded-xl bg-[#EAF8FB] border border-[#0EA5C6]/30 p-5 sm:p-6 space-y-3">
          <div className="flex items-center gap-2.5 text-[#0EA5C6] font-bold text-sm sm:text-base">
            <svg className="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h2>Demonstration & Sample Travel Data Notice</h2>
          </div>
          <p className="text-xs sm:text-sm text-[#12304A] leading-relaxed">
            This travel package is part of the curated demonstration dataset for the <strong>Smart Travel Discovery and Comparison Platform</strong>.
            All itineraries, accommodations, inclusions, tour operator profiles, and price structures are standardized sample records designed to test intelligent filtering, multi-preference discovery, and side-by-side package comparisons.
          </p>
          <p className="text-xs text-[#5B7185] leading-relaxed">
            This platform does not process commercial bookings, live inventory reservations, or payments. Data shown is illustrative for portfolio and development evaluation.
          </p>
        </div>

        {/* Package Attribute Summary Table */}
        <div className="border border-[#DCEAF2] rounded-xl overflow-hidden">
          <div className="bg-[#F6FBFF] px-4 py-2.5 border-b border-[#DCEAF2] text-xs font-bold uppercase tracking-wider text-[#5B7185]">
            Source Metadata Summary
          </div>
          <dl className="divide-y divide-[#DCEAF2] text-xs sm:text-sm">
            <div className="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4">
              <dt className="font-semibold text-[#5B7185]">Package Name</dt>
              <dd className="sm:col-span-2 font-bold text-[#12304A]">{packageDetail.name}</dd>
            </div>
            <div className="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4">
              <dt className="font-semibold text-[#5B7185]">Tour Operator</dt>
              <dd className="sm:col-span-2 text-[#12304A]">
                {packageDetail.operator?.name || "Independent"} (Rating: {packageDetail.operator?.rating || "N/A"})
              </dd>
            </div>
            <div className="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4">
              <dt className="font-semibold text-[#5B7185]">Target Destination</dt>
              <dd className="sm:col-span-2 text-[#0EA5C6] font-semibold">
                {packageDetail.destination?.name}, {packageDetail.destination?.region ? `${packageDetail.destination.region}, ` : ""}{packageDetail.destination?.country}
              </dd>
            </div>
            <div className="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4">
              <dt className="font-semibold text-[#5B7185]">Base Rate</dt>
              <dd className="sm:col-span-2 font-bold text-[#12304A]">
                ₹{packageDetail.price_per_person.toLocaleString("en-IN")} per person
              </dd>
            </div>
            <div className="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4">
              <dt className="font-semibold text-[#5B7185]">Reference Identifier</dt>
              <dd className="sm:col-span-2 font-mono text-xs text-[#5B7185] break-all">
                {packageDetail.source_url || `smart-travel-pkg-${packageDetail.id}`}
              </dd>
            </div>
          </dl>
        </div>

        {/* Action Controls */}
        <div className="pt-4 flex flex-wrap items-center gap-3">
          <Link
            href={`/packages/${packageDetail.id}`}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-xs sm:text-sm transition-colors shadow-sm"
          >
            <span>Back to Package Details</span>
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </Link>

          <Link
            href="/packages"
            className="px-4 py-2.5 rounded-xl bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] font-bold text-xs sm:text-sm transition-colors shadow-xs"
          >
            Browse All Packages
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function DemoSourcePage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const unwrappedParams = use(params);

  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A]">
      <Header />
      <main className="flex-1">
        <Suspense fallback={<LoadingSpinner message="Loading demo source..." />}>
          <DemoSourceContent id={unwrappedParams.id} />
        </Suspense>
      </main>
      <Footer />
    </div>
  );
}
