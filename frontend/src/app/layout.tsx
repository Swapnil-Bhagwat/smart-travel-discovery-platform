import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { CompareProvider } from "@/context/CompareContext";
import { ComparisonBar } from "@/components/ComparisonBar";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "Smart Travel Discovery & Comparison Platform",
  description: "Next.js & Flask-powered intelligent travel discovery and comparison platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col font-sans bg-[#F6FBFF] text-[#12304A]">
        <CompareProvider>
          {children}
          <ComparisonBar />
        </CompareProvider>
      </body>
    </html>
  );
}
