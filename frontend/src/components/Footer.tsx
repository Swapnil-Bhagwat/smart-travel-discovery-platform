import React from "react";
import Link from "next/link";

export function Footer() {
  return (
    <footer className="mt-auto bg-[#12304A] border-t border-[#0EA5C6]/20 py-10 px-4 sm:px-6 lg:px-8 text-slate-300">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-sm">
        <div>
          <p className="font-bold text-white tracking-wide">Smart Travel Discovery and Comparison Platform</p>
          <p className="mt-1 text-xs text-slate-300/80 max-w-md">
            Development MVP connecting Next.js, React, TypeScript, and Tailwind CSS to a Python Flask and MySQL backend architecture.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-6 text-xs text-slate-300">
          <Link href="/" className="hover:text-[#0EA5C6] transition-colors">
            Home Search
          </Link>
          <Link href="/packages" className="hover:text-[#0EA5C6] transition-colors">
            Packages List
          </Link>
          <span className="text-slate-400">Demo Inventory &copy; {new Date().getFullYear()}</span>
        </div>
      </div>
    </footer>
  );
}
