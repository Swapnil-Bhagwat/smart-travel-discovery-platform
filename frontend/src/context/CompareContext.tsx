"use client";

import React, { createContext, useContext, useState, useEffect, useCallback, useSyncExternalStore } from "react";

export interface ComparePackageItem {
  id: number;
  name: string;
  destinationName?: string;
  startingCity?: string;
  pricePerPerson?: number;
}

interface CompareContextType {
  selectedPackages: ComparePackageItem[];
  travellersCount: number;
  warningMessage: string | null;
  addPackage: (pkg: ComparePackageItem) => boolean;
  removePackage: (id: number | string) => void;
  clearPackages: () => void;
  isInCompare: (id: number | string) => boolean;
  setTravellersCount: (count: number) => void;
  dismissWarning: () => void;
  syncPackages: (packages: ComparePackageItem[]) => void;
}

const STORAGE_KEY = "smart_travel_compare_items";
const TRAVELLERS_KEY = "smart_travel_compare_travellers";
const MAX_PACKAGES = 3;

// Memory cache to return stable array reference from getSnapshot
let memoryPackages: ComparePackageItem[] = [];
let hasReadStorage = false;
const listeners = new Set<() => void>();

function emitChange() {
  for (const listener of listeners) {
    listener();
  }
}

function readStorage(): ComparePackageItem[] {
  if (typeof window === "undefined") return [];
  if (!hasReadStorage) {
    hasReadStorage = true;
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed)) {
          memoryPackages = parsed
            .filter((item) => item && item.id !== undefined && typeof item.name === "string")
            .map((item) => ({
              id: Number(item.id),
              name: String(item.name),
              destinationName: item.destinationName ? String(item.destinationName) : undefined,
              startingCity: item.startingCity ? String(item.startingCity) : undefined,
              pricePerPerson: item.pricePerPerson !== undefined ? Number(item.pricePerPerson) : undefined,
            }))
            .slice(0, MAX_PACKAGES);
        }
      }
    } catch {
      // Ignore parse errors
    }
  }
  return memoryPackages;
}

function writeStorage(items: ComparePackageItem[]) {
  memoryPackages = items.slice(0, MAX_PACKAGES);
  hasReadStorage = true;
  if (typeof window !== "undefined") {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(memoryPackages));
    } catch {
      // Ignore write errors
    }
  }
  emitChange();
}

let memoryTravellers = 2;
let hasReadTravellers = false;
const travellersListeners = new Set<() => void>();

function emitTravellersChange() {
  for (const listener of travellersListeners) {
    listener();
  }
}

function readTravellersStorage(): number {
  if (typeof window === "undefined") return 2;
  if (!hasReadTravellers) {
    hasReadTravellers = true;
    try {
      const stored = localStorage.getItem(TRAVELLERS_KEY);
      if (stored) {
        const num = Number(stored);
        if (!isNaN(num) && num > 0) {
          memoryTravellers = num;
        }
      }
    } catch {
      // Ignore parse errors
    }
  }
  return memoryTravellers;
}

function writeTravellersStorage(count: number) {
  memoryTravellers = count;
  hasReadTravellers = true;
  if (typeof window !== "undefined") {
    try {
      localStorage.setItem(TRAVELLERS_KEY, String(count));
    } catch {
      // Ignore
    }
  }
  emitTravellersChange();
}

function subscribeTravellers(callback: () => void) {
  travellersListeners.add(callback);
  return () => {
    travellersListeners.delete(callback);
  };
}

function getTravellersServerSnapshot() {
  return 2;
}

function getTravellersSnapshot() {
  return readTravellersStorage();
}

function subscribe(callback: () => void) {
  listeners.add(callback);
  return () => {
    listeners.delete(callback);
  };
}

const emptyArray: ComparePackageItem[] = [];
function getServerSnapshot() {
  return emptyArray;
}

function getSnapshot() {
  return readStorage();
}

const CompareContext = createContext<CompareContextType | undefined>(undefined);

export function CompareProvider({ children }: { children: React.ReactNode }) {
  const selectedPackages = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot);
  const travellersCount = useSyncExternalStore(
    subscribeTravellers,
    getTravellersSnapshot,
    getTravellersServerSnapshot
  );
  const [warningMessage, setWarningMessage] = useState<string | null>(null);

  const setTravellersCount = useCallback((count: number) => {
    const safeCount = Math.max(1, Number(count) || 1);
    writeTravellersStorage(safeCount);
  }, []);

  // Auto-dismiss warning message after 4 seconds
  useEffect(() => {
    if (!warningMessage) return;
    const timer = setTimeout(() => {
      setWarningMessage(null);
    }, 4000);
    return () => clearTimeout(timer);
  }, [warningMessage]);

  const addPackage = useCallback(
    (pkg: ComparePackageItem): boolean => {
      const numId = Number(pkg.id);
      // If already in list, treat as successful
      if (selectedPackages.some((p) => Number(p.id) === numId)) {
        return true;
      }

      if (selectedPackages.length >= MAX_PACKAGES) {
        setWarningMessage("You can compare up to 3 packages at a time.");
        return false;
      }

      const next = [...selectedPackages, { ...pkg, id: numId }];
      writeStorage(next);
      setWarningMessage(null);
      return true;
    },
    [selectedPackages]
  );

  const removePackage = useCallback(
    (id: number | string) => {
      const numId = Number(id);
      const next = selectedPackages.filter((p) => Number(p.id) !== numId);
      writeStorage(next);
      setWarningMessage(null);
    },
    [selectedPackages]
  );

  const clearPackages = useCallback(() => {
    writeStorage([]);
    setWarningMessage(null);
  }, []);

  const isInCompare = useCallback(
    (id: number | string): boolean => {
      const numId = Number(id);
      return selectedPackages.some((p) => Number(p.id) === numId);
    },
    [selectedPackages]
  );

  const dismissWarning = useCallback(() => {
    setWarningMessage(null);
  }, []);

  const syncPackages = useCallback((packages: ComparePackageItem[]) => {
    const normalized = packages.map((p) => ({
      ...p,
      id: Number(p.id),
    }));
    writeStorage(normalized);
  }, []);

  return (
    <CompareContext.Provider
      value={{
        selectedPackages,
        travellersCount,
        warningMessage,
        addPackage,
        removePackage,
        clearPackages,
        isInCompare,
        setTravellersCount,
        dismissWarning,
        syncPackages,
      }}
    >
      {children}
    </CompareContext.Provider>
  );
}

export function useCompare() {
  const context = useContext(CompareContext);
  if (!context) {
    throw new Error("useCompare must be used within a CompareProvider");
  }
  return context;
}

