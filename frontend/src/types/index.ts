/**
 * Domain and API TypeScript definitions for the Smart Travel Platform.
 */

export interface Destination {
  id: number;
  name: string;
  region: string | null;
  country: string;
  description: string | null;
  image_url: string | null;
}

export interface Operator {
  id: number;
  name: string;
  website_url: string | null;
  contact_email: string | null;
  contact_phone: string | null;
  rating: number;
}

export interface Theme {
  id: number;
  name: string;
  slug: string;
  description: string | null;
}

export interface DiscoveredDestination {
  destination_id: number;
  destination_name: string;
  country: string;
  region: string | null;
  description: string | null;
  image_url: string | null;
  match_score: number;
  matching_package_count: number;
  lowest_price_per_person: number;
  lowest_estimated_total_cost: number;
  best_matching_package_id: number;
  best_matching_package_name: string;
  match_reasons?: string[];
  mismatches?: string[];
}

export interface PackageSummary {
  id: number;
  name: string;
  operator: {
    id: number;
    name: string;
    rating: number;
  } | null;
  destination: {
    id: number;
    name: string;
    country: string;
    region: string | null;
  } | null;
  starting_city: string;
  duration_days: number;
  duration_nights: number;
  price_per_person: number;
  requested_travellers: number;
  estimated_total_cost: number;
  themes: Array<{ id: number; name: string; slug: string }>;
  travel_types: string[];
  available_months: number[];
  featured_image_url: string | null;
  source_url: string;
  match_score?: number;
  budget_status?: string;
  budget_difference?: number;
  match_reasons?: string[];
  mismatches?: string[];
  provider?: string;
  source_type?: string;
}

export interface ItineraryDay {
  id: number;
  day_number: number;
  title: string;
  description: string;
  accommodation: string | null;
  meals_provided: string | null;
}

export interface PackageDetail extends PackageSummary {
  is_active: boolean;
  hotel_info: string | null;
  meals_info: string | null;
  transportation_info: string | null;
  sightseeing_info: string | null;
  activities_info: string | null;
  itinerary: ItineraryDay[];
  inclusions: string[];
  exclusions: string[];
  created_at?: string | null;
  updated_at?: string | null;
}

export interface SearchFormData {
  starting_city: string;
  budget: string | number;
  travellers: string | number;
  duration_days: string | number;
  interest: string;
  travel_type: string;
  month: string | number;
  destination_id?: string | number;
  page?: number | string;
  per_page?: number | string;
}

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  pagination?: {
    page: number;
    per_page: number;
    total: number;
    pages: number;
  };
  message?: string;
  error?: {
    message: string;
  };
}
