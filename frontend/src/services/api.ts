/**
 * Centralized API client for communicating with Flask backend.
 */

import {
  Destination,
  Theme,
  PackageSummary,
  PackageDetail,
  DiscoveredDestination,
  ApiResponse,
  SearchFormData,
} from "@/types";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:5000/api/v1";

async function request<T>(endpoint: string, options?: RequestInit): Promise<ApiResponse<T>> {
  const url = `${API_BASE_URL}${endpoint}`;

  try {
    const res = await fetch(url, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...options?.headers,
      },
    });

    const data: ApiResponse<T> = await res.json();

    if (!res.ok) {
      const errorMsg =
        data.error?.message ||
        `Server responded with error status ${res.status}`;
      throw new Error(errorMsg);
    }

    return data;
  } catch (err: unknown) {
    if (err instanceof Error) {
      // Preserve custom backend message
      throw err;
    }
    throw new Error("Unable to connect to travel backend service.");
  }
}

/**
 * Fetch all available destinations for search dropdown.
 */
export async function fetchDestinations(): Promise<Destination[]> {
  const res = await request<Destination[]>("/destinations?per_page=50");
  return res.data;
}

/**
 * Fetch all travel themes / interests.
 */
export async function fetchThemes(): Promise<Theme[]> {
  const res = await request<Theme[]>("/themes");
  return res.data;
}

/**
 * Search packages when destination is known (or selected from discovery).
 */
export async function searchPackages(
  params: SearchFormData
): Promise<ApiResponse<PackageSummary[]>> {
  const queryParams = new URLSearchParams();

  if (params.starting_city) queryParams.set("starting_city", String(params.starting_city));
  if (params.budget !== undefined && params.budget !== "") queryParams.set("budget", String(params.budget));
  if (params.travellers) queryParams.set("travellers", String(params.travellers));
  if (params.duration_days) queryParams.set("duration_days", String(params.duration_days));
  if (params.interest) queryParams.set("interest", String(params.interest));
  if (params.travel_type) queryParams.set("travel_type", String(params.travel_type));
  if (params.month) queryParams.set("month", String(params.month));
  if (params.destination_id && String(params.destination_id).trim() !== "") {
    queryParams.set("destination_id", String(params.destination_id));
  }
  if (params.page !== undefined && params.page !== "") {
    queryParams.set("page", String(params.page));
  }
  if (params.per_page !== undefined && params.per_page !== "") {
    queryParams.set("per_page", String(params.per_page));
  }

  return await request<PackageSummary[]>(`/packages?${queryParams.toString()}`);
}

/**
 * Discover suggested destinations when destination is unknown.
 */
export async function discoverDestinations(
  params: Omit<SearchFormData, "destination_id">,
  limit: number = 10
): Promise<ApiResponse<DiscoveredDestination[]>> {
  const queryParams = new URLSearchParams();

  if (params.starting_city) queryParams.set("starting_city", String(params.starting_city));
  if (params.budget !== undefined && params.budget !== "") queryParams.set("budget", String(params.budget));
  if (params.travellers) queryParams.set("travellers", String(params.travellers));
  if (params.duration_days) queryParams.set("duration_days", String(params.duration_days));
  if (params.interest) queryParams.set("interest", String(params.interest));
  if (params.travel_type) queryParams.set("travel_type", String(params.travel_type));
  if (params.month) queryParams.set("month", String(params.month));
  queryParams.set("limit", String(limit));

  return await request<DiscoveredDestination[]>(
    `/discover/destinations?${queryParams.toString()}`
  );
}

/**
 * Fetch full package details including itinerary, inclusions, exclusions.
 */
export async function fetchPackageDetail(
  packageId: number | string,
  travellers: number = 1
): Promise<PackageDetail> {
  const res = await request<PackageDetail>(
    `/packages/${packageId}?travellers=${travellers}`
  );
  return res.data;
}

/**
 * Fetch explainable package recommendations from Step 7 recommendation service.
 */
export async function fetchRecommendedPackages(
  params: SearchFormData,
  limit: number = 10
): Promise<ApiResponse<PackageSummary[]>> {
  const queryParams = new URLSearchParams();

  if (params.starting_city) queryParams.set("starting_city", String(params.starting_city));
  if (params.budget !== undefined && params.budget !== "") queryParams.set("budget", String(params.budget));
  if (params.travellers) queryParams.set("travellers", String(params.travellers));
  if (params.duration_days) queryParams.set("duration_days", String(params.duration_days));
  if (params.interest) queryParams.set("interest", String(params.interest));
  if (params.travel_type) queryParams.set("travel_type", String(params.travel_type));
  if (params.month) queryParams.set("month", String(params.month));
  if (params.destination_id && String(params.destination_id).trim() !== "") {
    queryParams.set("destination_id", String(params.destination_id));
  }
  queryParams.set("limit", String(limit));

  return await request<PackageSummary[]>(`/recommendations/packages?${queryParams.toString()}`);
}
