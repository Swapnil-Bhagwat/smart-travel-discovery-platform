import React from "react";
import { ItineraryDay } from "@/types";

export function ItineraryView({ itinerary }: { itinerary: ItineraryDay[] }) {
  if (!itinerary || itinerary.length === 0) {
    return (
      <p className="text-sm text-[#5B7185] italic">
        Detailed day-by-day itinerary is currently being updated for this demo package.
      </p>
    );
  }

  // Sort by day number ascending
  const sortedDays = [...itinerary].sort((a, b) => a.day_number - b.day_number);

  return (
    <div className="relative border-l-2 border-[#0EA5C6]/30 ml-4 space-y-8 pl-6 my-6">
      {sortedDays.map((day) => (
        <div key={day.id || day.day_number} className="relative group">
          {/* Timeline node */}
          <div className="absolute -left-[33px] top-0 w-6 h-6 rounded-full bg-white border-2 border-[#0EA5C6] flex items-center justify-center text-[10px] font-bold text-[#0EA5C6] group-hover:scale-110 transition-transform shadow-xs">
            {day.day_number}
          </div>

          {/* Day Content */}
          <div className="rounded-xl bg-white border border-[#DCEAF2] p-5 shadow-xs hover:border-[#0EA5C6]/40 transition-colors">
            <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
              <span className="text-xs uppercase font-bold tracking-wider text-[#0EA5C6]">
                Day {day.day_number}
              </span>

              {/* Badges for Accommodation & Meals */}
              <div className="flex flex-wrap items-center gap-2">
                {day.meals_provided && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-orange-50 text-[#FF8A4C] border border-[#FF8A4C]/30 px-2 py-0.5 rounded-md">
                    🍴 {day.meals_provided}
                  </span>
                )}
                {day.accommodation && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-[#EAF8FB] text-[#0EA5C6] border border-[#0EA5C6]/30 px-2 py-0.5 rounded-md">
                    🏨 {day.accommodation}
                  </span>
                )}
              </div>
            </div>

            <h4 className="text-base font-bold text-[#12304A] mb-2">{day.title}</h4>
            <p className="text-sm text-[#5B7185] leading-relaxed whitespace-pre-line">
              {day.description}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}
