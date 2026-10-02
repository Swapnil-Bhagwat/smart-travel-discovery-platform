"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Destination, Theme, SearchFormData } from "@/types";
import { fetchDestinations, fetchThemes } from "@/services/api";

const STARTING_CITIES = [
  "Delhi",
  "Mumbai",
  "Pune",
  "Bangalore",
  "Hyderabad",
];

const TRAVEL_TYPES = ["Solo", "Couple", "Family", "Group"];

const MONTHS = [
  { value: 1, label: "January" },
  { value: 2, label: "February" },
  { value: 3, label: "March" },
  { value: 4, label: "April" },
  { value: 5, label: "May" },
  { value: 6, label: "June" },
  { value: 7, label: "July" },
  { value: 8, label: "August" },
  { value: 9, label: "September" },
  { value: 10, label: "October" },
  { value: 11, label: "November" },
  { value: 12, label: "December" },
];

const COMMON_DURATIONS = [3, 4, 5, 6, 7, 8, 10];

interface SearchFormProps {
  initialValues?: Partial<SearchFormData>;
  compact?: boolean;
}

export function SearchForm({ initialValues, compact = false }: SearchFormProps) {
  const router = useRouter();

  const [formData, setFormData] = useState<SearchFormData>({
    starting_city: initialValues?.starting_city || "Delhi",
    budget: initialValues?.budget || 40000,
    travellers: initialValues?.travellers || 2,
    duration_days: initialValues?.duration_days || 5,
    interest: initialValues?.interest || "Adventure",
    travel_type: initialValues?.travel_type || "Couple",
    month: initialValues?.month || 12,
    destination_id: initialValues?.destination_id || "",
  });

  const [destinations, setDestinations] = useState<Destination[]>([]);
  const [themes, setThemes] = useState<Theme[]>([]);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitting, setSubmitting] = useState(false);

  // Load themes & destinations from backend
  useEffect(() => {
    let isMounted = true;
    async function loadMeta() {
      try {
        const [dests, thms] = await Promise.all([
          fetchDestinations().catch(() => []),
          fetchThemes().catch(() => []),
        ]);
        if (isMounted) {
          setDestinations(dests);
          setThemes(thms);
        }
      } catch {
        // Fallback options available in UI
      }
    }
    loadMeta();
    return () => {
      isMounted = false;
    };
  }, []);

  const validate = (): boolean => {
    const errs: Record<string, string> = {};

    if (!formData.starting_city || !formData.starting_city.trim()) {
      errs.starting_city = "Please select a starting city";
    }

    const budgetNum = Number(formData.budget);
    if (isNaN(budgetNum) || budgetNum < 0) {
      errs.budget = "Budget must be a non-negative number";
    }

    const travellersNum = Number(formData.travellers);
    if (!Number.isInteger(travellersNum) || travellersNum < 1) {
      errs.travellers = "Travellers must be at least 1";
    }

    const durationNum = Number(formData.duration_days);
    if (!Number.isInteger(durationNum) || durationNum <= 0) {
      errs.duration_days = "Trip duration must be greater than 0 days";
    }

    if (!formData.interest || !formData.interest.trim()) {
      errs.interest = "Please select a travel interest";
    }

    if (!formData.travel_type || !TRAVEL_TYPES.includes(formData.travel_type)) {
      errs.travel_type = "Please select a valid travel type";
    }

    const monthNum = Number(formData.month);
    if (!Number.isInteger(monthNum) || monthNum < 1 || monthNum > 12) {
      errs.month = "Please select a valid travel month (1–12)";
    }

    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!validate()) return;

    setSubmitting(true);

    const queryParams = new URLSearchParams({
      starting_city: String(formData.starting_city).trim(),
      budget: String(formData.budget),
      travellers: String(formData.travellers),
      duration_days: String(formData.duration_days),
      interest: String(formData.interest).trim(),
      travel_type: String(formData.travel_type).trim(),
      month: String(formData.month),
    });

    if (formData.destination_id && String(formData.destination_id).trim() !== "") {
      queryParams.set("destination_id", String(formData.destination_id).trim());
      router.push(`/packages?${queryParams.toString()}`);
    } else {
      router.push(`/discover?${queryParams.toString()}`);
    }
  };  return (
    <form
      onSubmit={handleSubmit}
      className={`rounded-2xl bg-white border border-[#DCEAF2] shadow-xl shadow-sky-950/5 p-6 md:p-8 ${
        compact ? "max-w-4xl" : "max-w-5xl"
      } mx-auto`}
    >
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        {/* Starting Point */}
        <div>
          <label
            htmlFor="starting_city"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Starting Point <span className="text-[#0EA5C6]">*</span>
          </label>
          <select
            id="starting_city"
            value={formData.starting_city}
            onChange={(e) => {
              setFormData({ ...formData, starting_city: e.target.value });
              if (errors.starting_city) setErrors({ ...errors, starting_city: "" });
            }}
            className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
              errors.starting_city ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
            }`}
          >
            {STARTING_CITIES.map((city) => (
              <option key={city} value={city}>
                {city}
              </option>
            ))}
          </select>
          {errors.starting_city && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.starting_city}</p>
          )}
        </div>

        {/* Total Budget */}
        <div>
          <label
            htmlFor="budget"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Total Budget (INR ₹) <span className="text-[#0EA5C6]">*</span>
          </label>
          <div className="relative">
            <span className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#5B7185] text-sm">
              ₹
            </span>
            <input
              id="budget"
              type="number"
              min="0"
              step="500"
              value={formData.budget}
              onChange={(e) => {
                setFormData({ ...formData, budget: e.target.value });
                if (errors.budget) setErrors({ ...errors, budget: "" });
              }}
              placeholder="e.g. 50000"
              className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl pl-8 pr-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
                errors.budget ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
              }`}
            />
          </div>
          {errors.budget ? (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.budget}</p>
          ) : (
            <p className="mt-1 text-[11px] text-[#5B7185]">Total trip budget for all travellers</p>
          )}
        </div>

        {/* Number of Travellers */}
        <div>
          <label
            htmlFor="travellers"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Travellers <span className="text-[#0EA5C6]">*</span>
          </label>
          <input
            id="travellers"
            type="number"
            min="1"
            max="30"
            value={formData.travellers}
            onChange={(e) => {
              setFormData({ ...formData, travellers: e.target.value });
              if (errors.travellers) setErrors({ ...errors, travellers: "" });
            }}
            className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
              errors.travellers ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
            }`}
          />
          {errors.travellers && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.travellers}</p>
          )}
        </div>

        {/* Trip Duration */}
        <div>
          <label
            htmlFor="duration_days"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Trip Duration <span className="text-[#0EA5C6]">*</span>
          </label>
          <div className="flex gap-2">
            <select
              id="duration_days"
              value={formData.duration_days}
              onChange={(e) => {
                setFormData({ ...formData, duration_days: e.target.value });
                if (errors.duration_days) setErrors({ ...errors, duration_days: "" });
              }}
              className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
                errors.duration_days ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
              }`}
            >
              {COMMON_DURATIONS.map((d) => (
                <option key={d} value={d}>
                  {d} Days ({d - 1} Nights)
                </option>
              ))}
            </select>
          </div>
          {errors.duration_days && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.duration_days}</p>
          )}
        </div>

        {/* Travel Interest / Theme */}
        <div>
          <label
            htmlFor="interest"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Travel Interest <span className="text-[#0EA5C6]">*</span>
          </label>
          <select
            id="interest"
            value={formData.interest}
            onChange={(e) => {
              setFormData({ ...formData, interest: e.target.value });
              if (errors.interest) setErrors({ ...errors, interest: "" });
            }}
            className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
              errors.interest ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
            }`}
          >
            {themes.length > 0 ? (
              themes.map((th) => (
                <option key={th.id} value={th.name}>
                  {th.name}
                </option>
              ))
            ) : (
              <>
                <option value="Adventure">Adventure</option>
                <option value="Beach">Beach</option>
                <option value="Nature">Nature</option>
                <option value="Culture">Culture</option>
                <option value="Heritage">Heritage</option>
                <option value="Wildlife">Wildlife</option>
                <option value="Luxury">Luxury</option>
                <option value="Spiritual">Spiritual</option>
              </>
            )}
          </select>
          {errors.interest && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.interest}</p>
          )}
        </div>

        {/* Travel Type */}
        <div>
          <label
            htmlFor="travel_type"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Travel Type <span className="text-[#0EA5C6]">*</span>
          </label>
          <select
            id="travel_type"
            value={formData.travel_type}
            onChange={(e) => {
              setFormData({ ...formData, travel_type: e.target.value });
              if (errors.travel_type) setErrors({ ...errors, travel_type: "" });
            }}
            className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
              errors.travel_type ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
            }`}
          >
            {TRAVEL_TYPES.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>
          {errors.travel_type && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.travel_type}</p>
          )}
        </div>

        {/* Travel Month */}
        <div>
          <label
            htmlFor="month"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Travel Month <span className="text-[#0EA5C6]">*</span>
          </label>
          <select
            id="month"
            value={formData.month}
            onChange={(e) => {
              setFormData({ ...formData, month: e.target.value });
              if (errors.month) setErrors({ ...errors, month: "" });
            }}
            className={`w-full bg-[#F6FBFF] hover:bg-white border rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all ${
              errors.month ? "border-rose-400 bg-rose-50/20" : "border-[#DCEAF2]"
            }`}
          >
            {MONTHS.map((m) => (
              <option key={m.value} value={m.value}>
                {m.label}
              </option>
            ))}
          </select>
          {errors.month && (
            <p className="mt-1 text-xs text-rose-500 font-medium">{errors.month}</p>
          )}
        </div>

        {/* Destination (Optional) */}
        <div>
          <label
            htmlFor="destination_id"
            className="block text-xs font-semibold uppercase tracking-wider text-[#12304A] mb-1.5"
          >
            Destination <span className="text-[#5B7185] font-normal">(Optional)</span>
          </label>
          <select
            id="destination_id"
            value={formData.destination_id}
            onChange={(e) =>
              setFormData({ ...formData, destination_id: e.target.value })
            }
            className="w-full bg-[#F6FBFF] hover:bg-white border border-[#DCEAF2] rounded-xl px-3.5 py-2.5 text-sm text-[#12304A] focus:outline-none focus:ring-2 focus:ring-[#0EA5C6] focus:border-[#0EA5C6] focus:bg-white transition-all"
          >
            <option value="">✨ Let me discover a destination</option>
            {destinations.map((d) => (
              <option key={d.id} value={d.id}>
                {d.name} ({d.country})
              </option>
            ))}
          </select>
          <p className="mt-1.5 text-[11px] text-[#5B7185] leading-relaxed">
            Select a destination to search packages directly. Choose &quot;Let me discover a destination&quot; to get destination suggestions.
          </p>
        </div>
      </div>

      {/* Action Submit */}
      <div className="mt-8 pt-6 border-t border-[#DCEAF2] flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-2 text-xs text-[#5B7185]">
          <svg
            className="w-4 h-4 text-[#0EA5C6] shrink-0"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <span>
            {formData.destination_id
              ? "Destination selected: Searching packages directly."
              : 'Select a destination to search packages directly, or choose "Let me discover a destination" to get destination suggestions.'}
          </span>
        </div>

        <button
          type="submit"
          disabled={submitting}
          className="w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-8 py-3.5 rounded-xl bg-[#0EA5C6] hover:bg-[#0b8fae] text-white font-bold text-sm tracking-wide transition-all shadow-md shadow-[#0EA5C6]/20 disabled:opacity-50 disabled:cursor-not-allowed hover:scale-[1.01] active:scale-[0.99]"
        >
          {submitting ? (
            <>
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              <span>Searching...</span>
            </>
          ) : (
            <>
              <svg
                className="w-4 h-4 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2.5"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
              <span>Search Packages</span>
            </>
          )}
        </button>
      </div>
    </form>
  );
}
