"use client";

import React from "react";

interface ComparisonSectionProps {
  title: string;
  icon?: React.ReactNode;
  colSpan: number;
}

export function ComparisonSection({ title, icon, colSpan }: ComparisonSectionProps) {
  return (
    <tr className="bg-[#EAF8FB]/70 border-y border-[#DCEAF2]">
      <td
        colSpan={colSpan}
        className="py-3 px-4 sm:px-6 text-xs sm:text-sm font-extrabold uppercase tracking-wider text-[#0EA5C6]"
      >
        <div className="flex items-center gap-2">
          {icon && <span className="text-[#0EA5C6]">{icon}</span>}
          <span>{title}</span>
        </div>
      </td>
    </tr>
  );
}
