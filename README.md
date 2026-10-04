# Smart Travel Discovery and Comparison Platform

An intelligent, explainable, and extensible travel discovery, comparison, and recommendation platform built with **Next.js** (TypeScript, Tailwind CSS) and **Flask** (Python, SQLAlchemy, MySQL).

---

## Table of Contents
1. [Problem Statement](#1-problem-statement)
2. [Project Objective](#2-project-objective)
3. [Core User Flow](#3-core-user-flow)
4. [Key Features](#4-key-features)
5. [Technology Stack](#5-technology-stack)
6. [System Architecture](#6-system-architecture)
7. [Database Overview](#7-database-overview)
8. [API Overview](#8-api-overview)
9. [Recommendation Logic & Scoring Engine](#9-recommendation-logic--scoring-engine)
10. [Comparison Functionality](#10-comparison-functionality)
11. [Demo Dataset Specifications](#11-demo-dataset-specifications)
12. [Provider-Ready Architecture](#12-provider-ready-architecture)
13. [Installation & Setup](#13-installation--setup)
14. [Environment Variables](#14-environment-variables)
15. [How to Run Backend](#15-how-to-run-backend)
16. [How to Run Frontend](#16-how-to-run-frontend)
17. [How to Seed Demo Data](#17-how-to-seed-demo-data)
18. [Testing & Verification Commands](#18-testing--verification-commands)
19. [Deployment Preparation](#19-deployment-preparation)
20. [Important Demo-Data Disclaimer](#20-important-demo-data-disclaimer)
21. [AI-Assisted Development](#21-ai-assisted-development)
22. [Future Enhancements](#22-future-enhancements)

---

## 1. Problem Statement
Travelers frequently face information overload, fragmented itinerary options across disparate agency websites, opaque pricing models, and unexplainable algorithmic recommendations that push sponsored listings rather than genuine preference matches. Furthermore, side-by-side comparison of day-by-day itineraries, specific inclusions, exclusions, and cost-per-day metrics is tedious and error-prone.

---

## 2. Project Objective
The **Smart Travel Discovery and Comparison Platform** provides a transparent, explainable, and multi-dimensional search and comparison platform. Key goals include:
- Transparent, deterministic 100-point recommendation scoring with factual, data-grounded explanations.
- Dual discovery pathways: direct destination search or guided destination discovery based on travel interests.
- High-fidelity side-by-side comparison of 2–3 travel packages with dynamic traveller headcount calculations.
- Clean, provider-ready architectural foundation designed for future authorized external API integrations without website scraping.

---

## 3. Core User Flow

The platform accommodates two intuitive user journeys:

### Journey A: Direct Search & Package Comparison
```text
Homepage
   ↓ [User inputs starting city, budget, duration, month, travel type, interest + selects Destination]
Search Packages
   ↓
Package Results (/packages) [Paginated, sorted by 100-point match score]
   ↓
Why This Matches / Why Not 100% [Inspect factual data-grounded reasons]
   ↓
Add to Compare [Select 2 or 3 packages]
   ↓
Side-by-Side Comparison (/compare) [Dynamic headcount pricing, itinerary diff, inclusions/exclusions]
   ↓
Package Details (/packages/[id]) [Full itinerary breakdown and operator profile]
   ↓
Demo Source Attribution (/sources/packages/[id]) [Transparency and provider audit trail]
```

### Journey B: Guided Destination Discovery
```text
Homepage
   ↓ [User inputs preferences and selects "Let me discover a destination"]
Search Packages
   ↓
Destination Suggestions (/discover) [Destinations ranked by interest, budget, and package availability]
   ↓
Why This Destination? [Data-grounded suitability explanation]
   ↓
View Packages [Transfers all search criteria to /packages for the chosen destination]
   ↓
Add to Compare → Side-by-Side Comparison
```

---

## 4. Key Features

- **Dual Search Modality**: Search by explicit destination or discover ideal destinations dynamically based on travel interests and budget.
- **Deterministic 100-Point Recommendation Engine**: 
  - Budget fit (**25 pts**)
  - Travel interest match (**25 pts**; also a strict hard filter)
  - Duration fit (**20 pts**)
  - Travel type fit (**15 pts**; supports Solo, Couple, Family, Group)
  - Month availability (**10 pts**)
  - Starting city departure (**5 pts**; also a strict hard filter)
- **Strict Hard Filtering**:
  - Starting city constraint
  - Travel interest constraint (strict theme matching; non-matching packages are excluded completely)
  - Explicit destination constraint (when a destination is selected)
  - Active package status constraint (`is_active = TRUE`)
  - Over-budget hard exclusion (packages exceeding budget by more than 20% are excluded)
- **Factual, Explainable Insights**: No black-box algorithms or unsupported superlative claims ("best", "winner", "perfect for you", "most popular"). Every match reason and mismatch notice is fact-checked against real database values.
- **Side-by-Side Package Comparison**:
  - Compare 2 to 3 packages simultaneously.
  - Guard against 4th package addition with clear UI guidance.
  - Interactive traveller headcount multiplier ($1$ to $10+$ travellers) updating total pricing and per-person cost.
  - Objective value indicators: lowest price, shortest duration, lowest cost per day, most inclusions.
- **Seamless Pagination**: Responsive pagination preserving active filter queries and active comparison selections across page navigation.
- **Demo Source Transparency**: Dedicated verification views showing provider attribution, catalog source type, and verification status.

---

## 5. Technology Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **UI & Language**: React 19, TypeScript
- **Styling**: Tailwind CSS v4, Vanilla CSS Design Tokens
- **Icons & Polish**: Heroicons / Inline SVG

### Backend
- **Framework**: Python 3.12, Flask
- **ORM & Database Tooling**: Flask-SQLAlchemy, Flask-Migrate, PyMySQL
- **Security & Headers**: Flask-CORS, cryptography
- **Environment Management**: python-dotenv

### Database
- **Engine**: MySQL 8.x
- **User**: Dedicated least-privilege user `travel_app`
- **Integrity**: Foreign key cascading constraints, indexed queries

---

## 6. System Architecture

The application adopts a clean, layered architecture separating user interface, API endpoints, business logic, provider abstraction, and data persistence:

```text
Next.js Frontend (Port 3000)
        ↓ (HTTP / REST JSON)
Flask REST API (Port 5000)
        ↓
Routes (Blueprints: packages, destinations, discover, recommendations, operators, themes, providers, health)
        ↓
Business Services
        ├── Recommendation Service (Deterministic 100-pt scoring & factual explanations)
        ├── Search Logic (Hard constraints & soft scoring application)
        └── In-Memory Cache Service (Taxonomy caching with TTL)
        ↓
Provider Layer
        ├── BaseTravelProvider (Abstract interface)
        ├── ProviderRegistry (Dynamic registration & health)
        └── ProviderSearchService (Aggregator & deduplicator)
        ↓
Demo Provider (MySQL Adapter)
        ↓
MySQL Database (smart_travel_db)
```

### Recommendation and Comparison Details
- **Recommendation Service**: Evaluates eligible packages against user preferences using normalized distance metrics for budget and duration, calculating deterministic 100-point scores with data-grounded reasons and factual mismatch notifications.
- **Comparison Functionality**: The frontend comparison view (`/compare`) fetches individual package details for the 2–3 selected packages via `GET /api/v1/packages/<id>`, dynamically calculates headcount-adjusted costs, compares day-by-day itineraries, counts inclusions/exclusions, and computes factual value highlights without declaring subjective "overall winners".

---

## 7. Database Overview

The MySQL database `smart_travel_db` enforces relational integrity across 10 normalized tables matching the implemented schema:

| Table | Description |
|---|---|
| `destinations` | 25 Indian destinations with `name`, `region`, `country`, `description`, and `image_url` |
| `operators` | 10 fictional demo tour operators with `name`, `rating`, `website_url`, `contact_email`, and `contact_phone` |
| `themes` | 10 travel themes with `name`, `slug`, and `description` |
| `packages` | 107 total packages (103 active, 4 inactive) with `name`, `starting_city`, `duration_days`, `duration_nights`, `price_per_person`, `is_active`, `hotel_info`, `meals_info`, `transportation_info`, `sightseeing_info`, `activities_info`, `featured_image_url`, and `source_url` |
| `package_themes` | Many-to-many junction table mapping `packages.id` to `themes.id` |
| `package_travel_types` | Allowed travel types per package from the enum (`Solo`, `Couple`, `Family`, `Group`) |
| `package_availability_months` | Operating months (1–12) per package |
| `package_itineraries` | Day-by-day itinerary entries with `day_number`, `title`, `description`, `accommodation`, and `meals_provided` |
| `package_inclusions` | Line-item inclusions (`description`) per package |
| `package_exclusions` | Line-item exclusions (`description`) per package |

---

## 8. API Overview

All API endpoints follow a standardized, secure JSON response envelope:

**Success Response (HTTP 200/201):**
```json
{
  "success": true,
  "data": { ... }
}
```

**Error Response (HTTP 400/404/500):**
```json
{
  "success": false,
  "error": {
    "message": "Human-readable error description"
  }
}
```

### Registered Endpoints (14 Actual Endpoints)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Service health check |
| `GET` | `/api/v1/health/db` | Database connectivity verification |
| `GET` | `/api/v1/destinations` | List destinations with pagination (`page`, `per_page`) and optional `search`/`name` and `country` filters |
| `GET` | `/api/v1/destinations/<id>` | Retrieve single destination details by ID |
| `GET` | `/api/v1/operators` | List demo tour operators with pagination and optional name search |
| `GET` | `/api/v1/operators/<id>` | Retrieve single operator details by ID |
| `GET` | `/api/v1/themes` | List all travel themes (cached in-memory) |
| `GET` | `/api/v1/themes/<id>` | Retrieve single theme details by ID |
| `GET` | `/api/v1/packages` | Search & score packages (supports pagination, hard filters, soft preferences, and match explanations) |
| `GET` | `/api/v1/packages/<id>` | Full package details including day-by-day itinerary, inclusions, exclusions, and operator info |
| `GET` | `/api/v1/discover/destinations` | Destination discovery with suitability scoring and data-grounded reasons based on matching packages |
| `GET` | `/api/v1/recommendations/packages` | Top-recommended packages based on user preferences and hard constraints |
| `GET` | `/api/v1/providers` | Provider registry status, health, and enablement |
| `GET` | `/api/v1/providers/search` | Provider-agnostic package search across enabled providers |

> **Note on Package Comparison**: Side-by-side package comparison is conducted by requesting the selected package IDs via `GET /api/v1/packages/<id>` and assembling the comparative matrix client-side in the `/compare` interface.

---

## 9. Recommendation Logic & Scoring Engine

### Hard Filters (Pre-requisites for Inclusion)
1. **Starting City**: The package departure city must match the user's starting city (case-insensitive).
2. **Travel Interest**: **HARD FILTER** — If a travel interest is selected, the package **must** have a matching theme (`Theme.name` or `Theme.slug`, case-insensitive). Non-matching packages are excluded completely.
3. **Explicit Destination**: If searching for a specific destination, packages for all other destinations are excluded.
4. **Active Packages Only**: Inactive packages (`is_active = FALSE`) are strictly excluded from search and recommendation results.
5. **Over-Budget Cap**: Packages exceeding the user's total budget by more than 20% are excluded.

### 100-Point Deterministic Soft Scoring
Eligible packages that pass all hard filters are scored across six factual dimensions:

1. **Budget Fit (Max 25 Points)**:
   - Estimated total cost $\le$ Budget: **25 pts** (`within_budget`)
   - Over budget by $\le 10\%$: **18 pts** (`over_budget`, within 10% fallback)
   - Over budget by $> 10\%$ and $\le 20\%$: **10 pts** (`over_budget`, within 20% fallback)
   - Over budget by $> 20\%$: **0 pts** (excluded by hard filter)

2. **Travel Interest Match (25 Points)**:
   - Matches user's selected interest/theme: **25 pts** (guaranteed for all returned packages due to the hard filter)

3. **Duration Fit (Max 20 Points)**:
   - Exact duration match: **20 pts**
   - Within $\pm 1$ day: **16 pts**
   - Within $\pm 2$ days: **12 pts**
   - Within $\pm 3$ days: **8 pts**
   - Deviation $> 3$ days: **4 pts**

4. **Travel Type Fit (Max 15 Points)**:
   - Package includes the requested travel type (`Solo`, `Couple`, `Family`, `Group`): **15 pts**
   - Does not include the requested travel type: **0 pts**

5. **Month Availability (Max 10 Points)**:
   - Package operates in the requested month (1–12): **10 pts**
   - Not operating in the requested month: **0 pts**

6. **Starting City Departure (5 Points)**:
   - Departs from the requested starting city: **5 pts** (guaranteed for all returned packages due to the hard filter)

$$\text{Total Match Score} = 25 (\text{Budget}) + 25 (\text{Interest}) + 20 (\text{Duration}) + 15 (\text{Travel Type}) + 10 (\text{Month}) + 5 (\text{Starting City}) = 100 \text{ Points}$$

### Data-Grounded Explanations
- **Match Reasons**: Generated strictly from verified package attributes (e.g., *"Fits your ₹40,000 total budget"*, *"Matches your Adventure interest"*, *"Matches your 5-day duration preference"*, *"Suitable for Family travel"*, *"Available in October"*, *"Departs from your starting city (Delhi)"*).
- **Mismatches**: Factual callouts when preferences are not fully met (e.g., *"₹2,500 above your selected budget"*, *"Package is 6 days instead of your preferred 5 days"*, *"Designed for Solo, Group travel"*).
- **Zero Superlatives**: Unsupported promotional claims (e.g., *"best"*, *"winner"*, *"most popular"*, *"perfect for you"*) are strictly prohibited by code checks.

---

## 10. Comparison Functionality

- **Capacity**: Side-by-side comparison of 2 or 3 packages simultaneously.
- **Safety**: Adding a 4th package is blocked with an informative alert indicating the 3-package limit.
- **Persistence**: Comparison selections persist across pagination, filter changes, and navigation via local state and URL query parameters (`?ids=1,2,3`).
- **Dynamic Headcount**: An interactive traveller selector ($1$ to $10+$ travellers) dynamically recalculates total package costs while displaying individual per-person pricing.
- **Objective Value Analysis**:
  - Highlights lowest total price.
  - Highlights shortest duration.
  - Highlights lowest cost per day.
  - Highlights package with the highest number of inclusions.
- **Zero Winner Bias**: Does not declare an overall winner, allowing users to evaluate trade-offs objectively.

---

## 11. Demo Dataset Specifications

The local MySQL database contains a curated demonstration inventory:
- **25 Destinations**: Covering North, South, West, East, and Central India (e.g., Manali, Goa, Jaipur, Munnar, Varanasi, Ladakh, Andaman, Rishikesh, Darjeeling, etc.).
- **10 Tour Operators**: Fictional demo agencies (e.g., "Himalayan Horizons Demo", "Coastal Breeze Holidays Demo", "Royal Rajasthan Tours Demo") with realistic contact profiles and sample ratings.
- **10 Travel Themes**: Beach, Heritage, Adventure, Wildlife, Hill Station, Pilgrimage, Honeymoon, Trekking, Luxury, Cultural.
- **4 Travel Types**: Solo, Couple, Family, Group.
- **107 Packages**: 
  - **103 Active Packages**
  - **4 Inactive Packages** (used to verify inactive package filtering)
- **Data Integrity**: Every active package includes complete day-by-day itineraries, itemized inclusions, exclusions, travel types, and operating months.

---

## 12. Provider-Ready Architecture

The platform architecture is decoupled and extensible for future external travel integrations:
- **BaseTravelProvider (`backend/app/providers/base.py`)**: Defines an abstract contract (`search_packages`, `get_package_details`, `health_check`).
- **NormalizedPackage DTO (`backend/app/schemas/package_dto.py`)**: Uniform schema translating provider data to a consistent structure (`provider`, `source_type`, `external_id`, `identity`).
- **ProviderRegistry (`backend/app/providers/registry.py`)**: Centrally registers, enables, or disables providers via configuration flags.
- **Zero Web Scraping**: The system does not scrape external websites or bypass bot-detection terms. Future integrations will connect via official authorized partner APIs using backend environment credentials.
- **In-Memory Cache (`backend/app/services/cache_service.py`)**: Built-in TTL caching for static taxonomy data (themes, destinations, provider health) eliminates redundant database queries without external dependencies.

---

## 13. Installation & Setup

### Prerequisites
- **Node.js**: v18.0 or higher
- **Python**: v3.10 or higher
- **MySQL**: v8.0 or higher

### Step 1: Database Setup
Log in to MySQL as root or an administrator and create the application database and dedicated user:
```sql
CREATE DATABASE smart_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'travel_app'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON smart_travel_db.* TO 'travel_app'@'localhost';
FLUSH PRIVILEGES;
```

### Step 2: Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your MySQL credentials
```

### Step 3: Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env.local
# Set NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:5000/api/v1
```

---

## 14. Environment Variables

### Backend Configuration (`backend/.env`)
```bash
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
HOST=127.0.0.1
PORT=5000
SECRET_KEY=your_secret_key_here

CORS_ORIGINS=*

MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=travel_app
MYSQL_PASSWORD=your_secure_password
MYSQL_DATABASE=smart_travel_db

DEMO_PROVIDER_ENABLED=true
VIATOR_ENABLED=false
BOOKING_ENABLED=false
```

### Frontend Configuration (`frontend/.env.local`)
```bash
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:5000/api/v1
```

---

## 15. How to Run Backend

With the Python virtual environment activated:
```bash
cd backend
python run.py
```
The Flask API will start at `http://127.0.0.1:5000`.

---

## 16. How to Run Frontend

```bash
cd frontend
npm run dev
```
The Next.js application will start at `http://localhost:3000`.

---

## 17. How to Seed Demo Data

To populate the database with the full 107-package demonstration dataset:
```bash
cd backend
python scripts/seed_demo_data.py
```

---

## 18. Testing & Verification Commands

### Run Backend Unit Tests (128 Tests)
```bash
cd backend
python -m unittest discover -s tests
```

### Run Frontend Lint & Build
```bash
cd frontend
npm run lint
npm run build
```

### Run Step 10 Comprehensive Audit Script
```bash
cd backend
python scripts/audit_step10_comprehensive.py
```

### Run Step 10 Manual Verification Matrix Script
```bash
cd backend
python scripts/run_manual_test_matrix.py
```

---

## 19. Deployment Preparation

The application is structured for production deployment across containerized or serverless hosting:

### Frontend Deployment (Next.js)
- **Platforms**: Vercel, Netlify, AWS Amplify, or a Docker Node container.
- **Build Command**: `npm run build`
- **Output**: Static assets + Node.js SSR runtime.
- **Environment Variable**: Set `NEXT_PUBLIC_API_BASE_URL` to the public production backend URL (e.g. `https://api.yourdomain.com/api/v1`).

### Backend Deployment (Flask)
- **Platforms**: Render, Railway, AWS ECS, Google Cloud Run, or Ubuntu VPS.
- **Production Server**: Run using a production WSGI server such as Gunicorn:
  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
  ```
- **Security Flags**: Set `FLASK_DEBUG=0` and restrict `CORS_ORIGINS` to the production frontend domain (e.g. `https://travel.yourdomain.com`).

### Database Hosting (MySQL)
- **Platforms**: AWS RDS MySQL, DigitalOcean Managed MySQL, PlanetScale, or a secured dedicated MySQL 8 instance.
- **Security**: Store database credentials securely in platform secret managers; never commit `.env` files.

---

## 20. Important Demo-Data Disclaimer

> **IMPORTANT DISCLAIMER**:
> - All travel packages, itineraries, pricing, and hotel details presented on this platform are **curated demonstration data**.
> - Tour operators listed (e.g., "Himalayan Horizons Demo", "Coastal Breeze Holidays Demo") are **fictional entities** created solely for demonstration and academic evaluation.
> - This platform **does not process payments or live bookings**.
> - External live travel provider integrations (Viator, Booking.com) are architectural stubs and are **disabled by default**. No live web scraping is conducted.

---

## 21. AI-Assisted Development

This project was developed using AI-assisted development tools, including ChatGPT and Google Antigravity. AI tools were used for implementation assistance, code generation, debugging, documentation, and development workflow support. The project requirements, system architecture, feature decisions, testing, validation, and final technical direction were reviewed and directed by the developer.

---

## 22. Future Enhancements

- **User Accounts & Saved Trips**: User authentication to save, bookmark, and export personalized itineraries.
- **Authorized Provider Integrations**: Activation of live external provider APIs with authorized partner credentials.
- **Transit Add-ons**: Multi-modal transit calculation (flights, trains, intercity cabs) integrated into overall trip estimates.
- **Multi-Currency Support**: Real-time currency conversion for international travelers.
