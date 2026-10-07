# Smart Travel Discovery and Comparison Platform

A web-based platform that helps travellers discover suitable destinations and compare travel packages using budget and travel preferences.

[![Live Demo](https://img.shields.io/badge/Demo-Live%20on%20Vercel-black?style=flat&logo=vercel)](https://smart-travel-discovery-platform.vercel.app)
[![Backend API](https://img.shields.io/badge/API-Live%20on%20Render-blue?style=flat&logo=render)](https://smart-travel-discovery-platform-api.onrender.com/api/v1/health)
[![Next.js](https://img.shields.io/badge/Next.js-16-black?style=flat&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-61dafb?style=flat&logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?style=flat&logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-38bdf8?style=flat&logo=tailwindcss)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat)](https://www.sqlalchemy.org/)
[![TiDB Cloud](https://img.shields.io/badge/TiDB_Cloud-MySQL--Compatible-teal?style=flat)](https://tidbcloud.com/)

---

## Live Links

- **Live Application (Frontend)**: [https://smart-travel-discovery-platform.vercel.app](https://smart-travel-discovery-platform.vercel.app)
- **GitHub Repository**: [https://github.com/Swapnil-Bhagwat/smart-travel-discovery-platform](https://github.com/Swapnil-Bhagwat/smart-travel-discovery-platform)
- **Live Production API**: [https://smart-travel-discovery-platform-api.onrender.com/api/v1](https://smart-travel-discovery-platform-api.onrender.com/api/v1)

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution](#2-solution)
3. [Core User Flow](#3-core-user-flow)
4. [MVP Inputs](#4-mvp-inputs)
5. [Key Features](#5-key-features)
6. [Recommendation & Matching Logic](#6-recommendation--matching-logic)
7. [Technology Stack](#7-technology-stack)
8. [System Architecture](#8-system-architecture)
9. [Database Overview](#9-database-overview)
10. [Demo Dataset](#10-demo-dataset)
11. [Testing & Verification](#11-testing--verification)
12. [Deployment Architecture](#12-deployment-architecture)
13. [Limitations](#13-limitations)
14. [AI-Assisted Development](#14-ai-assisted-development)
15. [Future Scope](#15-future-scope)
16. [Local Setup Guide](#16-local-setup-guide)

---

## 1. Problem Statement

Planning leisure travel typically requires travellers to visit multiple agency websites, search through fragmented listings, parse inconsistent pricing structures, and manually cross-reference itineraries. Key pain points include:

- **Fragmented Research**: Comparing packages from different operators requires juggling dozens of browser tabs and unstructured notes.
- **Opaque Value & Inclusions**: Identifying what is covered (meals, transfers, hotels) versus hidden out-of-pocket costs is tedious.
- **Biased Search Listings**: Commercial search aggregators often push sponsored packages rather than results objectively matched to the traveller's budget, group size, and travel interests.
- **Destination Uncertainty**: Travellers with fixed budgets and themes (e.g., "Beach trip in October for ₹30,000") lack intuitive tools to discover which destinations match their criteria when they have not picked a specific location yet.

---

## 2. Solution

The **Smart Travel Discovery and Comparison Platform** provides a centralized, transparent travel evaluation portal that unifies destination discovery, package search, and side-by-side comparison into a coherent workflow:

- **Centralized Catalog**: Standardizes travel packages into a normalized data model covering daily itineraries, line-item inclusions, and exclusions.
- **Dual Discovery Modes**: Supports travellers who have a specific destination in mind as well as those seeking recommendations based on preferences.
- **Explainable Recommendation Scoring**: Ranks packages using an objective, deterministic 100-point scoring algorithm with transparent, fact-based match explanations.
- **Side-by-Side Comparison**: Enables direct comparison of 2–3 travel packages with dynamic traveller headcount multipliers, itinerary diffs, and objective value metrics without declaring arbitrary "winners".

---

## 3. Core User Flow

The application supports two distinct user journeys:

### Journey A: Destination Known
```text
User inputs travel criteria (city, budget, duration, month, group type, interest)
    ↓
Selects specific destination
    ↓
Views matching packages sorted by 100-point compatibility score
    ↓
Reviews factual match breakdown ("Why This Matches" / "Why Not 100%")
    ↓
Selects 2 or 3 packages to compare
    ↓
Evaluates side-by-side comparison matrix with dynamic headcount pricing
    ↓
Inspects detailed day-by-day itinerary and operator information
```

### Journey B: Destination Unknown
```text
User inputs travel criteria (without selecting a destination)
    ↓
Guided destination discovery (/discover)
    ↓
Reviews recommended destinations scored by interest alignment & budget feasibility
    ↓
Selects a suggested destination
    ↓
Transitions to filtered packages for the chosen destination
    ↓
Selects 2 or 3 packages to compare
    ↓
Evaluates side-by-side comparison matrix and package details
```

---

## 4. MVP Inputs

The search and recommendation engine operates on 8 practical travel criteria:

| Input | Description | Example |
|---|---|---|
| **Starting Point** | Departure city (hard filter) | Delhi, Mumbai, Bangalore |
| **Total Trip Budget** | Total spending budget in ₹ INR | ₹40,000 |
| **Travel Interest** | Primary theme / interest (hard filter) | Beach, Heritage, Adventure, Wildlife, Hill Station |
| **Trip Duration** | Target duration in days | 5 Days |
| **Travel Type** | Travel party composition | Solo, Couple, Family, Group |
| **Number of Travellers** | Headcount used for budget & per-person calculations | 2 Travellers |
| **Travel Month** | Intended month of departure (1–12) | October |
| **Destination** | *Optional*: Specific destination or guided discovery | Goa, Manali, Jaipur, or Discover |

---

## 5. Key Features

- **Destination Discovery**: Suggests suitable destinations ranked by theme match, package availability, and budget viability when travellers have not selected a destination.
- **Package Search**: Multi-criteria search with real-time filtering and deterministic ranking.
- **Hard Interest Filtering**: Strict enforcement of selected travel interests—packages not matching the requested theme are completely excluded.
- **Budget-Aware Matching with 20% Fallback**: Prioritizes packages within budget (`price_per_person * travellers <= budget`). If no package fits within budget, surfaces the closest alternatives up to 20% over budget with clear callouts.
- **Explainable Match Scores**: Each package receives an objective match score (up to 100 points) paired with verified match reasons and factual mismatch notes.
- **Comprehensive Package Details**: Complete breakdown of hotel tier, meal plans, transport, sightseeing, and activities.
- **Day-by-Day Itineraries**: Structured daily schedule with day number, title, detailed description, accommodation details, and meals provided.
- **Itemized Inclusions & Exclusions**: Clear line-item lists identifying covered amenities and excluded personal expenses.
- **Side-by-Side Comparison (2–3 Packages)**:
  - Compares 2 or 3 packages simultaneously (blocks 4th addition with informative notice).
  - Dynamic traveller headcount selector ($1$ to $10+$ travellers) recalculating total cost.
  - Highlights lowest price, shortest duration, lowest cost per day, and highest inclusion count.
  - Avoids declaring subjective "overall winners", allowing travellers to weigh trade-offs independently.
- **Stateful Pagination**: Result pagination (`page`, `per_page`) preserving active search parameters and comparison selections across page transitions.
- **Provider-Ready Architecture**: Service-layer abstraction (`BaseTravelProvider`, `ProviderRegistry`) designed for future authorized partner API integrations.
- **Demo Package & Source Attribution**: Dedicated attribution page displaying source metadata and verification badges for demo data transparency.

---

## 6. Recommendation & Matching Logic

### Deterministic 100-Point Scoring Model

The recommendation engine calculates a deterministic compatibility score out of **100 points** across six factual dimensions:

$$\text{Match Score} = 25 (\text{Budget}) + 25 (\text{Interest}) + 20 (\text{Duration}) + 15 (\text{Travel Type}) + 10 (\text{Month}) + 5 (\text{Starting City})$$

| Dimension | Max Points | Scoring Breakdown |
|---|---|---|
| **Budget Fit** | **25 pts** | Total cost $\le$ Budget: **25 pts**<br>Over budget by $\le 10\%$: **18 pts**<br>Over budget by $> 10\%$ and $\le 20\%$: **10 pts**<br>Over budget by $> 20\%$: **0 pts** (excluded) |
| **Travel Interest** | **25 pts** | Exact theme match: **25 pts** *(guaranteed for all returned results due to hard filter)* |
| **Trip Duration** | **20 pts** | Exact match: **20 pts**<br>Within $\pm 1$ day: **16 pts**<br>Within $\pm 2$ days: **12 pts**<br>Within $\pm 3$ days: **8 pts**<br>Deviation $> 3$ days: **4 pts** |
| **Travel Type** | **15 pts** | Package supports selected type (`Solo`, `Couple`, `Family`, `Group`): **15 pts**<br>Not supported: **0 pts** |
| **Availability Month** | **10 pts** | Package operates in requested month (1–12): **10 pts**<br>Not operating: **0 pts** |
| **Starting City** | **5 pts** | Departs from requested city: **5 pts** *(guaranteed for all returned results due to hard filter)* |

### Strict Hard Filters

Before scoring, the search engine applies non-negotiable hard constraints:
1. **Travel Interest**: **Strict Hard Filter** — Packages must match the user's selected interest/theme. Non-matching packages are excluded completely.
2. **Starting City**: Departure city must match the requested origin.
3. **Explicit Destination**: When a destination is chosen, packages for other destinations are excluded.
4. **Active Packages Only**: Inactive packages (`is_active = FALSE`) are strictly filtered out.
5. **Over-Budget Cap**: Packages exceeding the user's total budget by more than 20% are excluded.

### Deterministic vs. ML / LLM Transparency

> **Important**: The current recommendation engine is **100% deterministic and rule-based**. It does **not** rely on Machine Learning (ML), black-box neural networks, or Large Language Models (LLMs). Every score, match reason, and trade-off callout is fact-checked against database attributes, guaranteeing reproducible, auditable, and deterministic scoring without LLM-generated recommendations.

---

## 7. Technology Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **Library**: React 19
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS v4, Custom CSS Design Tokens
- **Icons**: Inline SVG / Heroicons

### Backend
- **Language**: Python 3.10+
- **Framework**: Flask 3.0
- **ORM & Migrations**: Flask-SQLAlchemy 3.1, Flask-Migrate 4.0, SQLAlchemy 2.0
- **Database Driver**: PyMySQL (with SSL/TLS verification)
- **CORS Handling**: Flask-CORS

### Database
- **Engine**: MySQL 8.0 compatible
- **Production Database**: TiDB Cloud (Serverless distributed MySQL-compatible database with secure TLS)
- **Local Development**: Local MySQL 8.x instance

### Deployment & Infrastructure
- **Frontend Hosting**: Vercel (Edge network, automated CI/CD)
- **Backend Hosting**: Render (Managed Python Web Service running Gunicorn WSGI)
- **Database Hosting**: TiDB Cloud (High-availability managed MySQL-compatible cluster)

---

## 8. System Architecture

The application is structured into decoupled layers separating presentation, API routing, business logic, provider abstraction, and relational persistence:

```text
┌───────────────────────────────────────────────────────────┐
│              Next.js 16 Frontend (Vercel)                 │
│    App Router | TypeScript | React 19 | Tailwind CSS     │
└─────────────────────────────┬─────────────────────────────┘
                              │ HTTPS / REST JSON
                              ▼
┌───────────────────────────────────────────────────────────┐
│               Flask 3.0 REST API (Render)                 │
│         Gunicorn WSGI | Blueprints | CORS Middleware      │
└─────────────────────────────┬─────────────────────────────┘
                              │
         ┌────────────────────┴────────────────────┐
         ▼                                         ▼
┌───────────────────────────────┐   ┌───────────────────────────────┐
│       Business Services       │   │    Provider Abstraction       │
│  - 100-pt Recommendation Svc  │   │  - BaseTravelProvider (ABC)   │
│  - Destination Discovery Svc  │   │  - ProviderRegistry           │
│  - In-Memory Taxonomy Cache   │   │  - DemoProvider (MySQL)       │
└───────────────┬───────────────┘   └───────────────┬───────────────┘
                │                                   │
                └─────────────────┬─────────────────┘
                                  ▼
┌───────────────────────────────────────────────────────────┐
│               SQLAlchemy 2.0 ORM / PyMySQL                │
└─────────────────────────────┬─────────────────────────────┘
                              │ TLS / SSL
                              ▼
┌───────────────────────────────────────────────────────────┐
│         TiDB Cloud / MySQL-Compatible Database            │
│       Normalized Schema | Relational Integrity           │
└───────────────────────────────────────────────────────────┘
```

### Provider Abstraction Layer

The platform includes an extensible provider architecture located in `backend/app/providers/`:
- **`BaseTravelProvider`**: Abstract interface defining standard provider methods (`search_packages`, `get_package_details`, `health_check`).
- **`NormalizedPackage` DTO**: Standardized data transfer object that normalizes incoming provider data into a unified structure (`provider`, `source_type`, `external_id`, `identity`).
- **`ProviderRegistry`**: Dynamic registry that enables/disables providers via configuration flags (`DEMO_PROVIDER_ENABLED`, etc.).
- **Zero Web Scraping Policy**: Live providers will connect exclusively through authorized partner APIs once production credentials are provisioned.

---

## 9. Database Overview

The relational database enforces data integrity across 10 normalized domain tables:

| Table | Description | Records |
|---|---|---|
| `destinations` | Travel destinations with name, region, country, description, and images | 25 |
| `operators` | Tour operators with company name, rating, website, and contact details | 10 |
| `themes` | Travel categories (Beach, Heritage, Adventure, etc.) with slugs | 10 |
| `packages` | Core package catalog with duration, pricing, hotel, meal, and transport info | 107 |
| `package_themes` | Many-to-many junction table mapping packages to themes | 114 |
| `package_travel_types` | Allowed travel types (`Solo`, `Couple`, `Family`, `Group`) per package | 240+ |
| `package_availability_months` | Operating months (1–12) per package | 600+ |
| `package_itineraries` | Day-by-day itineraries with daily title, description, hotel, and meal info | 400+ |
| `package_inclusions` | Itemized line-item inclusions per package | 400+ |
| `package_exclusions` | Itemized line-item exclusions per package | 300+ |

---

## 10. Demo Dataset

The platform includes a realistic demonstration inventory for testing and portfolio evaluation:

- **25 Destinations**: Covering North, South, West, East, and Central India (e.g., Manali, Goa, Jaipur, Munnar, Varanasi, Ladakh, Andaman, Rishikesh, Darjeeling, Mysore, Udaipur, etc.).
- **10 Tour Operators**: Realistic fictional agencies (e.g., "Himalayan Horizons Demo", "Coastal Breeze Holidays Demo", "Royal Rajasthan Tours Demo") with sample contact profiles and ratings.
- **10 Travel Themes**: Beach, Heritage, Adventure, Wildlife, Hill Station, Pilgrimage, Honeymoon, Trekking, Luxury, Cultural.
- **4 Travel Types**: Solo, Couple, Family, Group.
- **107 Total Packages**:
  - **103 Active Packages** (searchable and displayed in catalog)
  - **4 Inactive Packages** (used to verify inactive package filtering and data integrity)

> **Demo Data Notice**: All package and operator records are realistic sample data created for academic demonstration, automated testing, and portfolio presentation.

---

## 11. Testing & Verification

The platform has been audited and verified:

| Test Suite / Check | Scope | Result |
|---|---|---|
| **Backend Unit Tests** | 131 test cases covering search, filters, scoring, DTOs, API endpoints, and caching | **131 Passed (0 Failures, 0 Errors)** |
| **Frontend Linting** | ESLint static analysis across all TypeScript and React components | **Clean (0 Errors, 0 Warnings)** |
| **Frontend Production Build** | Next.js Turbopack production compilation and type check | **Build Succeeded** |
| **Live Production API Checks** | `GET /api/v1/health`<br>`GET /api/v1/health/db`<br>`GET /api/v1/packages?page=1&per_page=5` | **HTTP 200 OK** |
| **Live End-to-End User Journeys** | Destination discovery, package search, detailed itineraries, and 2–3 package comparison | **Verified Working** |

To run the backend test suite locally:
```bash
cd backend
python -m unittest discover -s tests
```

---

## 12. Deployment Architecture

The application is deployed across production environments:

- **Frontend**: Hosted on [Vercel](https://vercel.com/) with automated deployments from GitHub.
  - Automatically compiles Next.js App Router static assets and client bundles.
  - Connected to the backend via `NEXT_PUBLIC_API_BASE_URL`.
- **Backend**: Hosted on [Render](https://render.com/) as a Python Web Service.
  - Runs using Gunicorn: `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"`.
  - Configured with `CORS_ORIGINS` to allow requests from the Vercel frontend.
- **Database**: Hosted on [TiDB Cloud](https://tidbcloud.com/) Serverless.
  - MySQL 8.0-compatible distributed SQL database.
  - Connects securely using TLS/SSL (`MYSQL_SSL=true`).
- **Configuration & Secrets**: Handled strictly via platform environment variables; no credentials or secrets are stored in version control.

---

## 13. Limitations

- **Demo/Sample Data**: Package details, prices, and itineraries are curated demo data for demonstration purposes.
- **Fictional Operators**: Tour operator entities are fictional demonstration profiles.
- **No Booking or Payment Processing**: The platform is an informational discovery and comparison engine; it does not process live financial transactions.
- **No Live Provider APIs Enabled**: External provider APIs (Viator, Booking.com) are architectural stubs and are disabled by default until authorized production partner credentials are provisioned.
- **No Web Scraping**: The project does not scrape third-party travel websites, maintaining ethical data practices.
- **Deterministic Recommendation Engine**: Recommendations use deterministic rule-based scoring rather than machine learning models.

---

## 14. AI-Assisted Development

This project was developed using AI-assisted development tools, including ChatGPT and Google Antigravity. AI tools were used for implementation assistance, code generation, debugging, documentation, and development workflow support. The project requirements, system architecture, feature decisions, testing, validation, and final technical direction were reviewed and directed by the developer.

---

## 15. Future Scope

- **Authorized Live Provider Integrations**: Connect real-time availability and live pricing via authorized partner APIs.
- **User Accounts & Saved Itineraries**: User authentication allowing travellers to bookmark packages, save search configurations, and export trip plans.
- **Machine Learning Recommendations**: Incorporate collaborative filtering and preference embeddings to complement the deterministic baseline.
- **Price Tracking & Alerts**: Historical price monitoring with email notifications on price drops.
- **Direct Booking Deep Links**: Integrate affiliate/partner deep links allowing users to book directly on verified operator portals.

---

## 16. Local Setup Guide

### Prerequisites
- **Node.js**: v18.0 or higher
- **Python**: v3.10 or higher
- **MySQL**: v8.0 or higher

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/Swapnil-Bhagwat/smart-travel-discovery-platform.git
cd smart-travel-discovery-platform
```

---

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
```

Configure `backend/.env` with your local database credentials:
```env
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=local-dev-secret-key

MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=travel_app
MYSQL_PASSWORD=your_secure_password
MYSQL_DATABASE=smart_travel_db

CORS_ORIGINS=*
DEMO_PROVIDER_ENABLED=true
```

Run database migrations and seed the demo dataset:
```bash
# Apply migrations
flask db upgrade

# Seed 107 demo packages across 25 destinations
python scripts/seed_demo_data.py

# Start the Flask API server
python run.py
```
The backend API will start at `http://127.0.0.1:5000`.

---

### Step 3: Frontend Setup
In a new terminal window:
```bash
cd frontend

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env.local
```

Ensure `frontend/.env.local` contains:
```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:5000/api/v1
```

Start the Next.js development server:
```bash
npm run dev
```
Open `http://localhost:3000` in your browser to view the application.
