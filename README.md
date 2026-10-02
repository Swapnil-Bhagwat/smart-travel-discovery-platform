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
21. [Future Enhancements](#21-future-enhancements)

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
  - Budget fit (30 pts)
  - Duration fit (25 pts)
  - Travel type fit (25 pts)
  - Month availability (20 pts)
- **Strict Hard Filtering**:
  - Starting city constraint
  - Travel interest constraint (strict theme matching)
  - Explicit destination constraint
  - Active package status constraint
  - >20% over-budget hard exclusion
- **Factual, Explainable Insights**: No black-box algorithms or unsupported superlative claims ("best", "winner", "perfect for you", "most popular"). Every match reason and mismatch notice is fact-checked against real database values.
- **Side-by-Side Package Comparison**:
  - Compare 2 to 3 packages simultaneously.
  - Guard against 4th package addition with clear UI guidance.
  - Interactive traveller headcount multiplier updating total pricing and per-person cost.
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
Routes (Blueprints: packages, destinations, compare, discover, providers, health)
        ↓
Business Services
        ├── Recommendation Service (Deterministic 100-pt scoring)
        ├── Comparison Service (Matrix generation, value highlights)
        ├── Search Service (Constraint application)
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

### Recommendation and Comparison Flow Details
- **Recommendation Service**: Evaluates eligible packages against user preferences using normalized distance metrics for budget and duration, calculating deterministic scores with data-grounded reasons.
- **Comparison Service**: Consolidates 2 or 3 selected package identifiers, calculates per-day costs, normalizes day-by-day itineraries, tallies inclusions/exclusions, and computes factual value highlights without declaring subjective "overall winners".

---

## 7. Database Overview

The MySQL database `smart_travel_db` enforces relational integrity across 10 normalized tables:

| Table | Description |
|---|---|
| `destinations` | 25 Indian destinations with state, region, description, image, and best season |
| `operators` | 10 fictional demo tour operators with ratings, verified badges, and licenses |
| `themes` | 10 travel themes (Beach, Heritage, Adventure, Wildlife, Hill Station, etc.) |
| `packages` | 107 total packages (103 active, 4 inactive) with duration, base price, starting city |
| `package_themes` | Many-to-many junction mapping packages to themes |
| `package_travel_types` | Allowed travel types (Solo, Couple, Family, Friends, Group) per package |
| `package_availability_months` | Operating months (1–12) per package |
| `itineraries` | Day-by-day itinerary entries with titles, activities, meals, and accommodations |
| `package_inclusions` | Line-item inclusions (Hotels, meals, transfers, guides, entry tickets) |
| `package_exclusions` | Clear exclusion notices (Airfare, personal expenses, insurance) |

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

### Registered Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Service health check |
| `GET` | `/api/v1/health/db` | Database connectivity verification |
| `GET` | `/api/v1/destinations` | List all destinations (supports region/budget filtering) |
| `GET` | `/api/v1/destinations/<id>` | Retrieve destination details |
| `GET` | `/api/v1/operators` | List demo tour operators |
| `GET` | `/api/v1/operators/<id>` | Retrieve operator details |
| `GET` | `/api/v1/themes` | List all travel themes |
| `GET` | `/api/v1/themes/<id>` | Retrieve theme details |
| `GET` | `/api/v1/packages` | Search & score packages (supports pagination, hard/soft filters) |
| `GET` | `/api/v1/packages/<id>` | Full package details with itinerary and inclusions |
| `GET` | `/api/v1/packages/compare` | Compare 2–3 packages by IDs (`?ids=1,2,3`) |
| `GET` | `/api/v1/discover/destinations` | Destination discovery with suitability scores |
| `GET` | `/api/v1/recommendations/packages` | Top-recommended packages based on preferences |
| `GET` | `/api/v1/providers` | Provider registry status and health |
| `GET` | `/api/v1/providers/search` | Provider-agnostic package search |

---

## 9. Recommendation Logic & Scoring Engine

### Hard Filters (Pre-requisites for Inclusion)
1. **Starting City**: If specified, the package departure city must match.
2. **Travel Interest**: If specified, the package must possess a matching theme. Non-matching packages are excluded.
3. **Explicit Destination**: If searching for a specific destination, all other destinations are excluded.
4. **Active Packages Only**: Inactive packages (`is_active = FALSE`) are excluded from search results.
5. **Over-Budget Cap**: Packages exceeding user budget by more than 20% are excluded.

### 100-Point Deterministic Soft Scoring
Eligible packages are scored across four objective dimensions:

1. **Budget Fit (30 Points)**:
   - Price $\le$ Budget: **30 pts**
   - Budget $<$ Price $\le 1.10 \times$ Budget: **20 pts**
   - $1.10 \times \text{Budget} < \text{Price} \le 1.20 \times \text{Budget}$: **10 pts**
   - Price $> 1.20 \times$ Budget: **0 pts** (or hard excluded if budget filter applied)

2. **Duration Fit (25 Points)**:
   - Exact match: **25 pts**
   - Within $\pm 1$ day: **18 pts**
   - Within $\pm 2$ days: **10 pts**
   - Deviation $> 2$ days: **0 pts**

3. **Travel Type Fit (25 Points)**:
   - Matching travel type (e.g., Couple, Family, Solo): **25 pts**
   - Non-matching: **0 pts**

4. **Month Availability (20 Points)**:
   - Package operates in requested month: **20 pts**
   - Non-matching: **0 pts**

---

## 10. Comparison Functionality

- **Capacity**: Side-by-side comparison of 2 or 3 packages.
- **Safety**: Adding a 4th package is prevented with a clear alert indicating the 3-package limit.
- **Persistence**: Comparison selections are preserved in local storage and URL query params across pagination and navigation.
- **Dynamic Headcount**: An interactive traveller selector ($1$ to $10$ travellers) dynamically updates total package pricing and displays individual per-person costs.
- **Objective Value Analysis**:
  - Highlights lowest total price.
  - Highlights shortest duration.
  - Highlights lowest cost per day.
  - Highlights package with the most inclusions.
- **Zero Winner Bias**: Does not declare subjective "overall winners", letting users make informed choices based on objective metrics.

---

## 11. Demo Dataset Specifications

The local MySQL database contains a curated demonstration inventory:
- **25 Destinations**: Covering North, South, West, East, and Central India.
- **10 Tour Operators**: Clearly fictional demo agencies (e.g., "Himalayan Horizons Demo", "Coastal Breeze Holidays Demo") with realistic contact profiles and sample license numbers.
- **10 Travel Themes**: Beach, Heritage, Adventure, Wildlife, Hill Station, Pilgrimage, Honeymoon, Trekking, Luxury, Cultural.
- **107 Packages**: 
  - **103 Active Packages**
  - **4 Inactive Packages** (verifying soft-delete / inactive package filtering)
- **Data Integrity**: Every active package includes complete day-by-day itineraries, itemized inclusions, exclusions, travel types, and operating months.

---

## 12. Provider-Ready Architecture

The platform architecture is decoupled and extensible for future external travel integrations:
- **BaseTravelProvider**: Defines an abstract contract (`search_packages`, `get_package_details`, `health_check`).
- **NormalizedPackage DTO**: Uniform schema translating provider data to a consistent structure (`provider`, `source_type`, `external_id`, `identity`).
- **ProviderRegistry**: Centrally enables or disables providers via configuration flags.
- **Zero Web Scraping**: The system does not scrape external websites or bypass bot-detection terms. Future integrations will connect via official authorized partner APIs using backend environment credentials.
- **In-Memory Cache**: Built-in TTL caching for static taxonomy data (themes, destinations) eliminates redundant database queries without external dependencies.

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
python scripts/seed_database.py
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

## 21. Future Enhancements

- **User Accounts & Saved Trips**: User authentication to save, bookmark, and export personalized itineraries.
- **Authorized Provider Integrations**: Activation of live external provider APIs with authorized partner credentials.
- **Transit Add-ons**: Multi-modal transit calculation (flights, trains, intercity cabs) integrated into overall trip estimates.
- **Multi-Currency Support**: Real-time currency conversion for international travelers.
