"use client";

import React, { Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { SearchForm } from "@/components/SearchForm";
import { SearchFormData } from "@/types";

function HomeSearchForm() {
  const searchParams = useSearchParams();
  const initialValues: Partial<SearchFormData> = {};

  const city = searchParams.get("starting_city");
  if (city) initialValues.starting_city = city;

  const budget = searchParams.get("budget");
  if (budget) initialValues.budget = Number(budget) || 40000;

  const travellers = searchParams.get("travellers");
  if (travellers) initialValues.travellers = Number(travellers) || 2;

  const duration = searchParams.get("duration_days");
  if (duration) initialValues.duration_days = Number(duration) || 5;

  const interest = searchParams.get("interest");
  if (interest) initialValues.interest = interest;

  const travel_type = searchParams.get("travel_type");
  if (travel_type) initialValues.travel_type = travel_type;

  const month = searchParams.get("month");
  if (month) initialValues.month = Number(month) || 12;

  const destination_id = searchParams.get("destination_id");
  if (destination_id) initialValues.destination_id = destination_id;

  return <SearchForm key={JSON.stringify(initialValues)} initialValues={initialValues} />;
}

export default function HomePage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#F6FBFF] text-[#12304A] selection:bg-[#0EA5C6] selection:text-white">
      <Header />

      <main className="flex-1">
        {/* Hero Section */}
        <section className="relative pt-12 pb-16 md:pt-16 md:pb-24 px-4 sm:px-6 lg:px-8 overflow-hidden">
          {/* Subtle Ambient Background Gradients */}
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-gradient-to-b from-[#0EA5C6]/10 via-[#EAF8FB]/50 to-transparent blur-3xl pointer-events-none -z-10" />

          <div className="max-w-4xl mx-auto text-center mb-10">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-[#EAF8FB] text-[#0EA5C6] border border-[#DCEAF2] mb-4 shadow-xs">
              ✨ Smart Travel Discovery Platform
            </span>
            <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-[#12304A]">
              Find Your <span className="text-[#0EA5C6]">Perfect Trip</span>
            </h1>
            <p className="mt-4 text-base sm:text-lg text-[#5B7185] max-w-2xl mx-auto leading-relaxed">
              Have a destination in mind? Or want to discover where your budget and schedule can take you? Enter your trip details below to get started.
            </p>
          </div>

          {/* Search Form Container */}
          <Suspense fallback={<div className="max-w-5xl mx-auto h-96 bg-white/50 rounded-2xl animate-pulse" />}>
            <HomeSearchForm />
          </Suspense>
        </section>

        {/* How Destination Discovery Works */}
        <section className="py-16 px-4 sm:px-6 lg:px-8 border-t border-[#DCEAF2] bg-white/60">
          <div className="max-w-6xl mx-auto">
            <div className="text-center max-w-2xl mx-auto mb-12">
              <h2 className="text-2xl sm:text-3xl font-bold text-[#12304A] tracking-tight">
                How It Works
              </h2>
              <p className="mt-2 text-sm text-[#5B7185]">
                A deterministic, package-backed matching engine designed to help you discover destinations without guesswork.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {/* Feature 1 */}
              <div className="rounded-2xl bg-white border border-[#DCEAF2] p-6 flex flex-col items-start shadow-xs hover:shadow-md transition-shadow">
                <div className="w-12 h-12 rounded-xl bg-[#EAF8FB] border border-[#0EA5C6]/30 text-[#0EA5C6] flex items-center justify-center font-bold text-lg mb-4">
                  1
                </div>
                <h3 className="text-lg font-bold text-[#12304A] mb-2">
                  Define Your Travel Parameters
                </h3>
                <p className="text-xs sm:text-sm text-[#5B7185] leading-relaxed">
                  Provide your starting city, group size, trip duration, intended travel month, and total budget in INR.
                </p>
              </div>

              {/* Feature 2 */}
              <div className="rounded-2xl bg-white border border-[#DCEAF2] p-6 flex flex-col items-start shadow-xs hover:shadow-md transition-shadow">
                <div className="w-12 h-12 rounded-xl bg-teal-50 border border-[#14B8A6]/30 text-[#14B8A6] flex items-center justify-center font-bold text-lg mb-4">
                  2
                </div>
                <h3 className="text-lg font-bold text-[#12304A] mb-2">
                  Discover or Search Directly
                </h3>
                <p className="text-xs sm:text-sm text-[#5B7185] leading-relaxed">
                  Already decided? Pick your destination. Unsure? Leave it blank and our discovery algorithm ranks destinations with matching active packages.
                </p>
              </div>

              {/* Feature 3 */}
              <div className="rounded-2xl bg-white border border-[#DCEAF2] p-6 flex flex-col items-start shadow-xs hover:shadow-md transition-shadow">
                <div className="w-12 h-12 rounded-xl bg-orange-50 border border-[#FF8A4C]/30 text-[#FF8A4C] flex items-center justify-center font-bold text-lg mb-4">
                  3
                </div>
                <h3 className="text-lg font-bold text-[#12304A] mb-2">
                  Inspect Transparent Details
                </h3>
                <p className="text-xs sm:text-sm text-[#5B7185] leading-relaxed">
                  Review verified operators, comprehensive day-by-day itineraries, transparent inclusions, and exclusions before finalizing.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}
