"use client";

import React from "react";

interface ComparisonRowProps {
  label: string;
  sublabel?: string;
  values: React.ReactNode[];
  highlight?: boolean;
}

export function ComparisonRow({
  label,
  sublabel,
  values,
  highlight = false,
}: ComparisonRowProps) {
  return (
    <tr
      className={`border-b border-[#DCEAF2] hover:bg-[#F6FBFF]/80 transition-colors ${
        highlight ? "bg-[#F6FBFF]/50" : "bg-white"
      }`}
    >
      <th
        scope="row"
        className="py-3.5 sm:py-4 px-3.5 sm:px-6 text-left align-top text-xs sm:text-sm font-bold text-[#12304A] bg-white sticky left-0 z-10 border-r border-[#DCEAF2] min-w-[140px] sm:min-w-[180px] w-[180px] shadow-sm sm:shadow-none"
      >
        <div className="leading-snug">{label}</div>
        {sublabel && (
          <div className="text-[11px] font-normal text-[#5B7185] mt-0.5 leading-tight">
            {sublabel}
          </div>
        )}
      </th>
      {values.map((val, idx) => (
        <td
          key={idx}
          className="py-3.5 sm:py-4 px-4 sm:px-6 align-top text-xs sm:text-sm text-[#12304A] border-r last:border-r-0 border-[#DCEAF2] min-w-[260px] sm:min-w-[300px]"
        >
          {val}
        </td>
      ))}
    </tr>
  );
}
