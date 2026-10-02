"use client";

import React, { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { DestinationCard } from "@/components/DestinationCard";
import { DestinationCardsSkeleton } from "@/components/LoadingState";
import { ErrorState } from "@/components/ErrorState";
import { EmptyState } from "@/components/EmptyState";
import { DiscoveredDestination, SearchFormData } from "@/types";
import { discoverDestinations } from "@/services/api";

function DiscoverContent() {
  const searchParams = useSearchParams();

  const starting_city = searchParams.get("starting_city") || "";
  const budget = searchParams.get("budget") || "";
  const travellers = searchParams.get("travellers") || "1";
  const duration_days = searchParams.get("duration_days") || "";
  const interest = searchParams.get("interest") || "";
  const travel_type = searchParams.get("travel_type") || "";
  const month = searchParams.get("month") || "";

  const isMissingParams = !starting_city || !budget || !duration_days || !interest || !travel_type || !month;

  const [destinations, setDestinations] = useState<DiscoveredDestination[]>([]);
  const [loading, setLoading] = useState<boolean>(!isMissingParams);
  const [error, setError] = useState<string | null>(
    isMissingParams ? "Missing required search parameters. Please start a search from the home page." : null
  );
  const [refreshKey, setRefreshKey] = useState<number>(0);

  const parsedSearchParams: Partial<SearchFormData> = {
    starting_city,
    budget,
    travellers: Number(travellers) || 1,
    duration_days,
    interest,
    travel_type,
    month,
  };

  useEffect(() => {
    if (isMissingParams) {
      return;
    }

    let cancelled = false;

    discoverDestinations({
      starting_city,
      budget: Number(budget),
      travellers: Number(travellers),
      duration_days: Number(duration_days),
      interest,
      travel_type,
      month: Number(month),
    })
      .then((res) => {
        if (cancelled) return;
        if (res.success) {
          setDestinations(res.data || []);
          setError(null);
        } else {
          setError(res.error?.message || "Failed to discover destinations.");
        }
      })
      .catch((err: unknown) => {
        if (cancelled) return;
        const msg = err instanceof Error ? err.message : "Error discovering destinations";
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
    isMissingParams,
    starting_city,
    budget,
    travellers,
    duration_days,
    interest,
    travel_type,
    month,
    refreshKey,
  ]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Header & Active Filter Summary */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-[#DCEAF2]">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2]">
              Discovery Engine
            </span>
          </div>
          <h1 className="text-3xl font-extrabold text-[#12304A] tracking-tight">
            Destinations For You
          </h1>
          <p className="mt-1 text-sm text-[#5B7185] max-w-2xl">
            Match scores reflect how closely available active travel packages fit your departure city, budget, duration, and preferences.
          </p>
        </div>

        {/* Active Criteria Chips */}
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
              Interest: <strong className="text-[#12304A]">{interest}</strong>
            </span>
          )}
          <Link
            href="/"
            className="px-3.5 py-1.5 rounded-lg bg-white hover:bg-[#EAF8FB] border border-[#DCEAF2] text-[#12304A] font-semibold text-xs transition-colors shadow-xs"
          >
            Edit Filters
          </Link>
        </div>
      </div>

      {/* Content States */}
      <div className="mt-8">
        {loading && <DestinationCardsSkeleton count={6} />}

        {!loading && error && (
          <ErrorState
            title="Discovery Error"
            message={error}
            onRetry={() => {
              setLoading(true);
              setRefreshKey((k) => k + 1);
            }}
          />
        )}

        {!loading && !error && destinations.length === 0 && (
          <EmptyState
            title="No Matching Destinations Found"
            message="No destinations match all your selected requirements. Try increasing your budget, changing the duration, travel month, or travel interest."
            actionText="Modify Search Criteria"
            actionHref="/"
          />
        )}

        {!loading && !error && destinations.length > 0 && (
          <div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {destinations.map((dest) => (
                <DestinationCard
                  key={dest.destination_id}
                  destination={dest}
                  searchParams={parsedSearchParams}
                />
              ))}
            </div>

            <div className="mt-12 text-center text-xs text-[#5B7185]">
              Found {destinations.length} destination(s) matching your parameters. Click &ldquo;View Packages&rdquo; to browse and compare specific trips.
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default function DiscoverPage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A]">
      <Header />
      <main className="flex-1">
        <Suspense fallback={<div className="max-w-7xl mx-auto p-10"><DestinationCardsSkeleton count={6} /></div>}>
          <DiscoverContent />
        </Suspense>
      </main>
      <Footer />
    </div>
  );
}
