"use client";

import React, { Suspense, useEffect, useState, useCallback, useMemo } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { ComparisonTable } from "@/components/ComparisonTable";
import { ComparisonLoading } from "@/components/ComparisonLoading";
import { ComparisonError } from "@/components/ComparisonError";
import { PackageDetail } from "@/types";
import { fetchPackageDetail } from "@/services/api";
import { useCompare } from "@/context/CompareContext";

function CompareContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { syncPackages, removePackage: removeContextPackage, setTravellersCount } = useCompare();

  // Extract query parameters
  const rawIds = searchParams.get("ids") || "";
  const rawTravellers = searchParams.get("travellers");
  const travellers = Math.max(1, Math.min(30, Number(rawTravellers) || 2));

  // Parse and sanitize IDs
  const parsedIds = useMemo(() => {
    if (!rawIds.trim()) return [];
    const parts = rawIds.split(",");
    const valid: number[] = [];
    for (const part of parts) {
      const clean = part.trim();
      const num = Number(clean);
      if (!isNaN(num) && num > 0 && !valid.includes(num)) {
        valid.push(num);
      }
    }
    // Limit to max 3 packages
    return valid.slice(0, 3);
  }, [rawIds]);

  const isInsufficient = parsedIds.length < 2;
  const [packages, setPackages] = useState<PackageDetail[]>([]);
  const [loading, setLoading] = useState<boolean>(!isInsufficient);
  const [error, setError] = useState<string | null>(null);
  const [refreshKey, setRefreshKey] = useState<number>(0);

  // Sync travellers count to context
  useEffect(() => {
    setTravellersCount(travellers);
  }, [travellers, setTravellersCount]);

  // Fetch package details
  useEffect(() => {
    if (parsedIds.length < 2) {
      return;
    }

    let cancelled = false;

    // Concurrently fetch each package detail
    Promise.allSettled(
      parsedIds.map((id) => fetchPackageDetail(id, travellers))
    )
      .then((results) => {
        if (cancelled) return;

        const loaded: PackageDetail[] = [];
        let failedCount = 0;

        results.forEach((res) => {
          if (res.status === "fulfilled" && res.value && res.value.id) {
            loaded.push(res.value);
          } else {
            failedCount++;
          }
        });

        if (loaded.length >= 2) {
          setPackages(loaded);
          setError(null);
          // Sync with CompareContext so selection is consistent
          syncPackages(
            loaded.map((p) => ({
              id: p.id,
              name: p.name,
              startingCity: p.starting_city,
              pricePerPerson: p.price_per_person,
            }))
          );
        } else if (loaded.length === 1) {
          setPackages(loaded);
          setError(
            failedCount > 0
              ? "Some packages could not be found or are inactive. At least 2 active packages are required for comparison."
              : null
          );
        } else {
          setPackages([]);
          setError(
            failedCount > 0
              ? "Unable to find the requested travel packages. They may be inactive or invalid."
              : null
          );
        }
      })
      .catch((err: unknown) => {
        if (cancelled) return;
        const msg = err instanceof Error ? err.message : "Error loading packages.";
        setError(msg);
      })
      .finally(() => {
        if (!cancelled) {
          setLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [parsedIds, travellers, refreshKey, syncPackages]);

  // Handle removing a package from comparison
  const handleRemovePackage = useCallback(
    (packageId: number) => {
      const remaining = packages.filter((p) => p.id !== packageId);
      setPackages(remaining);
      removeContextPackage(packageId);

      const remainingIds = remaining.map((p) => p.id);
      if (remainingIds.length > 0) {
        router.push(`/compare?ids=${remainingIds.join(",")}&travellers=${travellers}`);
      } else {
        router.push(`/compare?travellers=${travellers}`);
      }
    },
    [packages, travellers, router, removeContextPackage]
  );

  // Handle changing travellers count on the comparison page
  const handleTravellersChange = (newCount: number) => {
    const valid = Math.max(1, Math.min(30, newCount));
    if (parsedIds.length > 0) {
      router.push(`/compare?ids=${parsedIds.join(",")}&travellers=${valid}`);
    } else {
      router.push(`/compare?travellers=${valid}`);
    }
  };

  // 1. Loading state
  if (!isInsufficient && loading) {
    return <ComparisonLoading count={parsedIds.length || 3} />;
  }

  // 2. Fatal fetch error with no packages
  if (error && packages.length < 2) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <ComparisonError
          title="Could not load travel packages"
          message={error}
          onRetry={() => {
            setLoading(true);
            setRefreshKey((k) => k + 1);
          }}
        />
      </div>
    );
  }

  // 3. Insufficient packages state (< 2 valid packages)
  if (packages.length < 2) {
    return (
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center">
        <div className="w-16 h-16 mx-auto rounded-2xl bg-[#EAF8FB] border border-[#DCEAF2] flex items-center justify-center text-[#0EA5C6] mb-5 shadow-sm">
          <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
        </div>

        <h1 className="text-2xl sm:text-3xl font-extrabold text-[#12304A] tracking-tight">
          Select at least 2 packages to compare.
        </h1>
        <p className="mt-2 text-sm text-[#5B7185] max-w-lg mx-auto">
          {packages.length === 1
            ? `You have selected "${packages[0].name}". Add at least one more package to see a side-by-side comparison.`
            : "Browse our verified package catalog and choose 2 or 3 packages to compare side-by-side."}
        </p>

        {packages.length === 1 && (
          <div className="mt-6 inline-flex items-center gap-2 p-3 rounded-xl bg-white border border-[#DCEAF2] shadow-xs text-xs text-[#12304A]">
            <span className="w-2 h-2 rounded-full bg-emerald-500" />
            <span>Currently selected: <strong>{packages[0].name}</strong></span>
          </div>
        )}

        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Link
            href="/packages"
            className="px-6 py-2.5 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-sm shadow-md shadow-[#0EA5C6]/20 transition-all"
          >
            Browse Packages
          </Link>
          <Link
            href="/"
            className="px-5 py-2.5 rounded-xl bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] font-bold text-sm transition-colors shadow-xs"
          >
            Plan a New Trip
          </Link>
        </div>
      </div>
    );
  }

  // 4. Valid Comparison: 2 or 3 packages
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-10">
      {/* Top Breadcrumb & Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center gap-2 text-xs text-[#5B7185] mb-1.5 font-medium">
            <Link href="/packages" className="hover:text-[#0EA5C6] transition-colors">
              Packages
            </Link>
            <span>/</span>
            <span className="text-[#12304A] font-bold">Package Comparison</span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-extrabold text-[#12304A] tracking-tight">
            Compare Travel Packages
          </h1>
          <p className="mt-1 text-xs sm:text-sm text-[#5B7185]">
            Evaluating {packages.length} selected packages side-by-side using standardized information.
          </p>
        </div>

        {/* Travellers Controller & Add More Button */}
        <div className="flex flex-wrap items-center gap-3">
          {/* Travellers Counter */}
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white border border-[#DCEAF2] shadow-xs">
            <label htmlFor="compare-pax" className="text-xs font-semibold text-[#5B7185]">
              Travellers:
            </label>
            <input
              id="compare-pax"
              type="number"
              min="1"
              max="30"
              value={travellers}
              onChange={(e) => handleTravellersChange(Number(e.target.value) || 1)}
              className="w-14 bg-[#F6FBFF] border border-[#DCEAF2] rounded-lg px-2 py-1 text-xs font-bold text-[#12304A] text-center focus:outline-none focus:ring-2 focus:ring-[#0EA5C6]"
            />
          </div>

          {/* Add 3rd package button if only 2 selected */}
          {packages.length === 2 && (
            <Link
              href="/packages"
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-[#EAF8FB] hover:bg-[#d8f2f8] text-[#0EA5C6] border border-[#0EA5C6]/30 text-xs font-bold transition-colors shadow-xs"
            >
              <span>+ Add 3rd Package</span>
            </Link>
          )}

          <Link
            href="/packages"
            className="px-3.5 py-2 rounded-xl bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] text-xs font-bold transition-colors shadow-xs"
          >
            Browse More
          </Link>
        </div>
      </div>

      {/* Comparison Table */}
      <ComparisonTable
        packages={packages}
        travellers={travellers}
        onRemovePackage={handleRemovePackage}
      />

      {/* Bottom Information Notice */}
      <div className="mt-8 text-center text-xs text-[#5B7185] max-w-2xl mx-auto space-y-1">
        <p>
          Pricing and estimated costs are calculated neutrally based on official operator rates for{" "}
          <strong className="text-[#12304A]">{travellers} traveller{travellers > 1 ? "s" : ""}</strong>.
        </p>
        <p className="text-[11px] text-[#5B7185]/80">
          No automated winner or recommendation bias is applied. Please evaluate the inclusions, accommodation, and day-by-day itineraries to decide the best fit for your journey.
        </p>
      </div>
    </div>
  );
}

export default function ComparePage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A]">
      <Header />
      <main className="flex-1 pb-16">
        <Suspense fallback={<ComparisonLoading count={3} />}>
          <CompareContent />
        </Suspense>
      </main>
      <Footer />
    </div>
  );
}
