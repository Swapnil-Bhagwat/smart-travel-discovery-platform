"use client";

import React, { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { PackageCard } from "@/components/PackageCard";
import { PackageCardsSkeleton } from "@/components/LoadingState";
import { ErrorState } from "@/components/ErrorState";
import { EmptyState } from "@/components/EmptyState";
import { Pagination } from "@/components/Pagination";
import { PackageSummary } from "@/types";
import { searchPackages } from "@/services/api";
import { useCompare } from "@/context/CompareContext";

interface PaginationData {
  page: number;
  per_page: number;
  total: number;
  pages: number;
}

function PackagesContent() {
  const searchParams = useSearchParams();
  const { setTravellersCount } = useCompare();

  const starting_city = searchParams.get("starting_city") || "";
  const budget = searchParams.get("budget") || "";
  const travellers = searchParams.get("travellers") || "1";
  const duration_days = searchParams.get("duration_days") || "";
  const interest = searchParams.get("interest") || "";
  const travel_type = searchParams.get("travel_type") || "";
  const month = searchParams.get("month") || "";
  const destination_id = searchParams.get("destination_id") || "";

  // Parse page and per_page from query params
  const rawPage = searchParams.get("page") || "1";
  const rawPerPage = searchParams.get("per_page") || "20";
  const currentPage = Math.max(1, parseInt(rawPage, 10) || 1);
  const perPage = Math.max(1, Math.min(100, parseInt(rawPerPage, 10) || 20));

  // Sync current search traveller count to comparison context
  useEffect(() => {
    if (travellers) {
      setTravellersCount(Number(travellers) || 1);
    }
  }, [travellers, setTravellersCount]);

  const [packages, setPackages] = useState<PackageSummary[]>([]);
  const [pagination, setPagination] = useState<PaginationData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshKey, setRefreshKey] = useState<number>(0);

  useEffect(() => {
    let cancelled = false;

    searchPackages({
      starting_city,
      budget,
      travellers: Number(travellers) || 1,
      duration_days,
      interest,
      travel_type,
      month,
      destination_id,
      page: currentPage,
      per_page: perPage,
    })
      .then((res) => {
        if (cancelled) return;
        if (res.success) {
          setPackages(res.data || []);
          if (res.pagination) {
            setPagination(res.pagination);
          } else {
            setPagination({
              page: currentPage,
              per_page: perPage,
              total: res.data ? res.data.length : 0,
              pages: 1,
            });
          }
          setError(null);
        } else {
          setError(res.error?.message || "Failed to retrieve travel packages.");
        }
      })
      .catch((err: unknown) => {
        if (cancelled) return;
        const msg = err instanceof Error ? err.message : "Error searching packages";
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
  }, [
    starting_city,
    budget,
    travellers,
    duration_days,
    interest,
    travel_type,
    month,
    destination_id,
    currentPage,
    perPage,
    refreshKey,
  ]);

  const hasFilters = Boolean(
    starting_city || budget || duration_days || interest || travel_type || month || destination_id
  );

  // Helper to build page link while preserving all current search query parameters
  const createPageHref = (targetPage: number) => {
    const params = new URLSearchParams(searchParams.toString());
    params.set("page", String(targetPage));
    if (searchParams.has("per_page")) {
      params.set("per_page", String(perPage));
    }
    return `/packages?${params.toString()}`;
  };

  const totalItems = pagination?.total ?? packages.length;
  const activePage = pagination?.page ?? currentPage;
  const activePerPage = pagination?.per_page ?? perPage;
  const totalPages = pagination?.pages ?? (totalItems > 0 ? Math.ceil(totalItems / activePerPage) : 0);

  const startItem = totalItems === 0 ? 0 : (activePage - 1) * activePerPage + 1;
  const endItem = Math.min(activePage * activePerPage, totalItems);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Header & Active Filter Bar */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-[#DCEAF2]">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
              {hasFilters ? "Search Results" : "Catalog Directory"}
            </span>
          </div>
          <h1 className="text-3xl font-extrabold text-[#12304A] tracking-tight">
            Matching Travel Packages
          </h1>
          <p className="mt-1 text-sm text-[#5B7185] max-w-2xl">
            {hasFilters
              ? "Verified sample packages filtered by your selected destination, duration, and budget requirements."
              : "Browsing all active verified demo packages in the platform inventory."}
          </p>
        </div>

        {/* Filter Chips / Edit Link */}
        <div className="flex flex-wrap items-center gap-2 text-xs">
          {starting_city && (
            <span className="px-3 py-1.5 rounded-lg bg-white border border-[#DCEAF2] text-[#5B7185] shadow-xs">
              Ex <strong className="text-[#12304A]">{starting_city}</strong>
            </span>
          )}
          {budget && (
            <span className="px-3 py-1.5 rounded-lg bg-white border border-[#DCEAF2] text-[#5B7185] shadow-xs">
              Budget: <strong className="text-[#0EA5C6]">₹{Number(budget).toLocaleString("en-IN")}</strong>
            </span>
          )}
          {duration_days && (
            <span className="px-3 py-1.5 rounded-lg bg-white border border-[#DCEAF2] text-[#5B7185] shadow-xs">
              <strong className="text-[#12304A]">{duration_days} Days</strong>
            </span>
          )}
          {interest && (
            <span className="px-3 py-1.5 rounded-lg bg-white border border-[#DCEAF2] text-[#5B7185] shadow-xs">
              Theme: <strong className="text-[#12304A]">{interest}</strong>
            </span>
          )}
          <Link
            href={hasFilters ? `/?${searchParams.toString()}` : "/"}
            className="px-3.5 py-1.5 rounded-lg bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] font-semibold text-xs transition-colors shadow-xs"
          >
            {hasFilters ? "Edit Filters" : "Filter Packages"}
          </Link>
        </div>
      </div>

      {/* Results Container */}
      <div className="mt-8">
        {loading && <PackageCardsSkeleton count={6} />}

        {!loading && error && (
          <ErrorState
            title="Package Search Failed"
            message={error}
            onRetry={() => {
              setLoading(true);
              setRefreshKey((k) => k + 1);
            }}
          />
        )}

        {!loading && !error && totalItems === 0 && (
          <EmptyState
            title="No Packages Found"
            message="No active packages matched all your filters. Try widening your budget limit or changing the duration or departure month."
            actionText="Modify Search Criteria"
            actionHref={hasFilters ? `/?${searchParams.toString()}` : "/"}
          />
        )}

        {!loading && !error && packages.length === 0 && totalItems > 0 && (
          <div className="rounded-2xl bg-white border border-[#DCEAF2] p-8 text-center max-w-md mx-auto my-12 shadow-sm">
            <h3 className="text-lg font-bold text-[#12304A]">Page Out of Range</h3>
            <p className="text-sm text-[#5B7185] mt-2">
              Page {activePage} exceeds available results ({totalPages} total pages).
            </p>
            <Link
              href={createPageHref(1)}
              className="mt-4 inline-flex items-center px-4 py-2 rounded-xl bg-[#0EA5C6] text-white text-xs font-bold hover:bg-[#0C8EA9] transition-colors shadow-xs"
            >
              Back to Page 1
            </Link>
          </div>
        )}

        {!loading && !error && packages.length > 0 && (
          <div>
            {/* Top Result Count Bar */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6 pb-2">
              <div className="text-sm font-medium text-[#5B7185]">
                Showing <span className="font-bold text-[#12304A]">{startItem}–{endItem}</span> of{" "}
                <span className="font-bold text-[#12304A]">{totalItems}</span> packages
                {totalPages > 1 && (
                  <span className="text-xs text-[#8FA2B2] ml-2">
                    (Page {activePage} of {totalPages})
                  </span>
                )}
              </div>
            </div>

            {/* Packages Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {packages.map((pkg) => (
                <PackageCard
                  key={pkg.id}
                  packageData={pkg}
                  requestedTravellers={Number(travellers) || 1}
                  searchQuery={searchParams.toString()}
                />
              ))}
            </div>

            {/* Bottom Pagination Controls */}
            <Pagination
              currentPage={activePage}
              totalPages={totalPages}
              totalItems={totalItems}
              itemsPerPage={activePerPage}
              createPageHref={createPageHref}
              onPageClick={() => {
                if (typeof window !== "undefined") {
                  window.scrollTo({ top: 0, behavior: "smooth" });
                }
              }}
            />

            <div className="mt-6 text-center text-xs text-[#8FA2B2]">
              All details, day-by-day itineraries, and inclusions can be inspected on each package details page.
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default function PackagesPage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A]">
      <Header />
      <main className="flex-1 pb-32 sm:pb-28">
        <Suspense fallback={<div className="max-w-7xl mx-auto p-10"><PackageCardsSkeleton count={6} /></div>}>
          <PackagesContent />
        </Suspense>
      </main>
      <Footer />
    </div>
  );
}
