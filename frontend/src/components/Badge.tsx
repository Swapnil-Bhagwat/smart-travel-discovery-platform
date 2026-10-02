import React from "react";

interface BadgeProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "success" | "accent" | "outline";
  className?: string;
}

export function Badge({
  children,
  variant = "secondary",
  className = "",
}: BadgeProps) {
  const variants = {
    primary: "bg-[#EAF8FB] text-[#0EA5C6] border border-[#0EA5C6]/30 font-semibold",
    secondary: "bg-slate-100 text-[#5B7185] border border-[#DCEAF2]",
    success: "bg-teal-50 text-teal-700 border border-teal-200",
    accent: "bg-orange-50 text-[#FF8A4C] border border-[#FF8A4C]/30 font-semibold",
    outline: "bg-transparent text-[#5B7185] border border-[#DCEAF2]",
  };

  return (
    <span
      className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${variants[variant]} ${className}`}
    >
      {children}
    </span>
  );
}

export function MatchScoreBadge({ score }: { score: number }) {
  let colorClass = "bg-[#EAF8FB] text-[#0EA5C6] border-[#0EA5C6]/40";
  if (score < 60) {
    colorClass = "bg-orange-50 text-[#FF8A4C] border-[#FF8A4C]/40";
  } else if (score < 80) {
    colorClass = "bg-teal-50 text-[#14B8A6] border-[#14B8A6]/40";
  }

  return (
    <div
      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border shadow-xs ${colorClass}`}
    >
      <span className="w-2 h-2 rounded-full bg-current animate-pulse" />
      <span>{score}% Match</span>
    </div>
  );
}
