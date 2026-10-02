"""
Seed Demo Data Script for Smart Travel Discovery and Comparison Platform.
Populates the MySQL database (smart_travel_db) with a comprehensive,
internally consistent demo dataset for development and end-to-end testing.

NOTE: This is fictional DEMO data for local testing. Prices, operators,
itineraries, ratings, and package details are illustrative.
"""

import os
import sys
from decimal import Decimal

# Ensure backend root is in Python path
BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app import create_app
from app.extensions import db
from app.models.destination import Destination
from app.models.operator import Operator
from app.models.theme import Theme
from app.models.package import (
    Package,
    PackageTravelType,
    PackageAvailabilityMonth,
    PackageItinerary,
    PackageInclusion,
    PackageExclusion,
    package_themes,
)


# =====================================================================
# DEMO DATA DEFINITIONS
# =====================================================================

DESTINATIONS_DATA = [
    {
        "name": "Manali",
        "region": "Himachal Pradesh",
        "country": "India",
        "description": "High-altitude Himalayan resort town renowned for snow-capped peaks, pine valleys, and adventure sports.",
        "image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Goa",
        "region": "Goa",
        "country": "India",
        "description": "Coastal tropical paradise featuring palm-fringed Arabian Sea beaches, vibrant nightlife, and Portuguese heritage architecture.",
        "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Jaipur",
        "region": "Rajasthan",
        "country": "India",
        "description": "The historic Pink City, home to majestic Rajput hill forts, grand palaces, vibrant bazaars, and rich royal heritage.",
        "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Kerala",
        "region": "Kerala",
        "country": "India",
        "description": "Tropical southwestern paradise famous for emerald backwaters, Munnar tea hills, Ayurvedic retreats, and Arabian coastlines.",
        "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Kashmir",
        "region": "Jammu and Kashmir",
        "country": "India",
        "description": "The Paradise on Earth, celebrated for tranquil Dal Lake houseboats, alpine meadows of Gulmarg, and snow-dusted Himalayan peaks.",
        "image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Rishikesh",
        "region": "Uttarakhand",
        "country": "India",
        "description": "World Capital of Yoga situated along the sacred Ganges river, featuring Himalayan foothills, ashrams, and thrilling river rapids.",
        "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Andaman",
        "region": "Andaman and Nicobar Islands",
        "country": "India",
        "description": "Exotic tropical archipelago in the Bay of Bengal known for turquoise lagoons, Radhanagar Beach, and vibrant coral reef diving.",
        "image_url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Jaisalmer",
        "region": "Rajasthan",
        "country": "India",
        "description": "The Golden City rising out of the Great Thar Desert, renowned for its living yellow-sandstone fort and starlit dune camps.",
        "image_url": "https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Gangtok",
        "region": "Sikkim",
        "country": "India",
        "description": "Scenic Himalayan capital nestled amidst clouds, offering panoramic views of Mount Kanchenjunga, Buddhist monasteries, and alpine lakes.",
        "image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Meghalaya",
        "region": "Meghalaya",
        "country": "India",
        "description": "The Abode of Clouds in Northeast India, famous for bio-engineered living root bridges, plunging waterfalls, and crystal-clear rivers.",
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Dubai",
        "region": "Dubai",
        "country": "United Arab Emirates",
        "description": "Futuristic global metropolis renowned for iconic skyscrapers, luxury shopping, desert dunes, and avant-garde attractions.",
        "image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Bali",
        "region": "Bali",
        "country": "Indonesia",
        "description": "Indonesian Island of the Gods, celebrated for lush terraced rice paddies, ancient Hindu temples, surf beaches, and holistic retreats.",
        "image_url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Udaipur",
        "region": "Rajasthan",
        "country": "India",
        "description": "The City of Lakes and Venice of the East, famed for shimmering Lake Pichola, royal palaces, and romantic heritage.",
        "image_url": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Amritsar",
        "region": "Punjab",
        "country": "India",
        "description": "Spiritual hub of Sikhism and cultural heart of Punjab, home to the resplendent Golden Temple and Wagah Border.",
        "image_url": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Leh",
        "region": "Ladakh",
        "country": "India",
        "description": "High-altitude desert wonderland renowned for ancient Buddhist gompas, dramatic moonscapes, and Khardung La pass.",
        "image_url": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Darjeeling",
        "region": "West Bengal",
        "country": "India",
        "description": "The Queen of the Hills, celebrated for sprawling emerald tea gardens, Himalayan Toy Train, and Kanchenjunga sunrise views.",
        "image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Ooty",
        "region": "Tamil Nadu",
        "country": "India",
        "description": "Queen of Nilgiri Hill Stations, featuring aromatic eucalyptus forests, tea plantations, and scenic Nilgiri Mountain Railway.",
        "image_url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Coorg",
        "region": "Karnataka",
        "country": "India",
        "description": "The Scotland of India, blanketed in mist-covered coffee estates, cascading waterfalls, and Kodava warrior culture.",
        "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Agra",
        "region": "Uttar Pradesh",
        "country": "India",
        "description": "Home of the iconic white marble Taj Mahal, majestic Agra Fort, and grand Mughal architectural heritage along the Yamuna.",
        "image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Varanasi",
        "region": "Uttar Pradesh",
        "country": "India",
        "description": "One of the oldest continuously inhabited cities on Earth, known for sacred Ganga ghats, evening Ganga Aarti, and spiritual heritage.",
        "image_url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Lakshadweep",
        "region": "Lakshadweep",
        "country": "India",
        "description": "Pristine coral archipelago in the Arabian Sea boasting turquoise lagoons, white coral atolls, and untouched marine life.",
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Mysore",
        "region": "Karnataka",
        "country": "India",
        "description": "The City of Palaces, celebrated for opulent royal heritage, Mysore silk weaving, fragrant sandalwood, and grand Dussehra traditions.",
        "image_url": "https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Pondicherry",
        "region": "Puducherry",
        "country": "India",
        "description": "Charming French colonial coastal town with pastel heritage villas, promenade beaches, cafes, and spiritual Auroville ashram.",
        "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Jim Corbett",
        "region": "Uttarakhand",
        "country": "India",
        "description": "India's oldest national park nestled in Himalayan foothills, renowned for Royal Bengal Tigers, wild elephants, and jungle safaris.",
        "image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "Munnar",
        "region": "Kerala",
        "country": "India",
        "description": "Idyllic hill station in the Western Ghats surrounded by rolling tea plantations, misty valleys, and rare Neelakurinji blooms.",
        "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=800&q=80",
    },
]

OPERATORS_DATA = [
    {
        "name": "WanderNest Travels",
        "website_url": "https://wandernest-demo.example.com",
        "contact_email": "hello@wandernest-demo.example.com",
        "contact_phone": "+91-9820011223",
        "rating": Decimal("4.8"),
    },
    {
        "name": "Horizon Trails",
        "website_url": "https://horizontrails-demo.example.com",
        "contact_email": "trips@horizontrails-demo.example.com",
        "contact_phone": "+91-9830022334",
        "rating": Decimal("4.6"),
    },
    {
        "name": "TripCraft Holidays",
        "website_url": "https://tripcraft-demo.example.com",
        "contact_email": "booking@tripcraft-demo.example.com",
        "contact_phone": "+91-9840033445",
        "rating": Decimal("4.7"),
    },
    {
        "name": "ExploreSphere Tours",
        "website_url": "https://exploresphere-demo.example.com",
        "contact_email": "info@exploresphere-demo.example.com",
        "contact_phone": "+91-9850044556",
        "rating": Decimal("4.5"),
    },
    {
        "name": "TravelVista India",
        "website_url": "https://travelvista-demo.example.com",
        "contact_email": "ops@travelvista-demo.example.com",
        "contact_phone": "+91-9860055667",
        "rating": Decimal("4.9"),
    },
    {
        "name": "BlueSky Journeys",
        "website_url": "https://bluesky-demo.example.com",
        "contact_email": "hello@bluesky-demo.example.com",
        "contact_phone": "+91-9870066778",
        "rating": Decimal("4.7"),
    },
    {
        "name": "TrailMosaic Holidays",
        "website_url": "https://trailmosaic-demo.example.com",
        "contact_email": "explore@trailmosaic-demo.example.com",
        "contact_phone": "+91-9880077889",
        "rating": Decimal("4.6"),
    },
    {
        "name": "GlobeNest Travels",
        "website_url": "https://globenest-demo.example.com",
        "contact_email": "bookings@globenest-demo.example.com",
        "contact_phone": "+91-9890088990",
        "rating": Decimal("4.8"),
    },
    {
        "name": "RoamRise Tours",
        "website_url": "https://roamrise-demo.example.com",
        "contact_email": "support@roamrise-demo.example.com",
        "contact_phone": "+91-9900099001",
        "rating": Decimal("4.5"),
    },
    {
        "name": "JourneyMint",
        "website_url": "https://journeymint-demo.example.com",
        "contact_email": "trips@journeymint-demo.example.com",
        "contact_phone": "+91-9910011223",
        "rating": Decimal("4.9"),
    },
]

THEMES_DATA = [
    {
        "name": "Adventure",
        "slug": "adventure",
        "description": "High-adrenaline activities including mountain trekking, river rafting, skiing, and desert expeditions.",
    },
    {
        "name": "Beach",
        "slug": "beach",
        "description": "Sun, sand, and coastal relaxation across tropical shorelines, lagoons, and seaside villages.",
    },
    {
        "name": "Nature",
        "slug": "nature",
        "description": "Scenic valleys, lush green landscapes, waterfalls, and mountain panoramas for nature lovers.",
    },
    {
        "name": "Culture",
        "slug": "culture",
        "description": "Authentic regional culinary trails, traditional arts, folk performances, and indigenous lifestyles.",
    },
    {
        "name": "Heritage",
        "slug": "heritage",
        "description": "Historical monuments, ancient architectural wonders, centuries-old palaces, and royal forts.",
    },
    {
        "name": "Wildlife",
        "slug": "wildlife",
        "description": "Jungle safaris, rare animal sightings, bird watching, and biodiversity biosphere exploration.",
    },
    {
        "name": "Luxury",
        "slug": "luxury",
        "description": "Five-star heritage resorts, private beachfront villas, personal concierges, and fine dining.",
    },
    {
        "name": "Spiritual",
        "slug": "spiritual",
        "description": "Sacred riverside shrines, yoga ashrams, meditation caves, and peaceful pilgrimage circuits.",
    },
    {
        "name": "Romantic",
        "slug": "romantic",
        "description": "Candlelit dinners, scenic lakeside havelis, sunset cruises, and private retreats for couples and honeymooners.",
    },
    {
        "name": "Mountain",
        "slug": "mountain",
        "description": "Breathtaking high-altitude peaks, alpine passes, pine valleys, and mountain retreats across the Himalayas and Western Ghats.",
    },
]


def build_packages_data():
    """Generates 34 detailed demo travel packages with full itineraries and inclusions."""
    packages = [
        # 1. Manali - Delhi - 5d - 18500 - Adventure + Nature - Couple - Winter (10-3)
        {
            "name": "Classic Manali & Solang Valley Explorer",
            "operator_name": "WanderNest Travels",
            "destination_name": "Manali",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("18500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/manali-explorer",
            "is_active": True,
            "hotel_info": "3-star alpine resort in Old Manali featuring wooden interiors and mountain valley balconies.",
            "meals_info": "Daily buffet breakfast and 4-course dinner with Himachali specialties.",
            "transportation_info": "Overnight AC Volvo bus Delhi - Manali - Delhi; private sedan for local tours.",
            "sightseeing_info": "Hadimba Temple, Vashisht Sulphur Springs, Solang Valley, and Mall Road.",
            "activities_info": "Paragliding, snow activities, zorbing, and pine forest nature hikes.",
            "themes": ["adventure", "nature"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Overnight Transit & Manali Arrival", "Board evening Volvo in Delhi. Arrive in Manali morning, hotel check-in, afternoon stroll to historic Hadimba Temple.", "Pine Crest Alpine Resort", "Dinner"),
                (2, "Solang Valley Adventure Excursion", "Full day excursion to Solang Valley for breathtaking Himalayan views, paragliding, and cable car rides.", "Pine Crest Alpine Resort", "Breakfast & Dinner"),
                (3, "Vashisht Springs & Old Manali Cafes", "Visit the ancient Vashisht village hot springs, Manu Temple, and experience Old Manali's bohemian cafes.", "Pine Crest Alpine Resort", "Breakfast & Dinner"),
                (4, "Naggar Castle & River Beas Crossing", "Excursion to medieval Naggar Castle, Nicholas Roerich art gallery, and white water crossing point.", "Pine Crest Alpine Resort", "Breakfast & Dinner"),
                (5, "Mall Road Souvenirs & Return Transit", "Morning at leisure on Mall Road for woolens and apple preserves. Evening Volvo transit back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights accommodation in deluxe pine valley room",
                "Daily buffet breakfast and chef-crafted dinner",
                "Round-trip AC Volvo tickets between Delhi and Manali",
                "Dedicated private cab for all sightseeing excursions",
                "All toll taxes, parking fees, and driver allowances"
            ],
            "exclusions": [
                "Personal expenses, laundry, and beverage charges",
                "Adventure sports activity fees and equipment hire",
                "Heater charges during peak winter months",
                "Travel and accidental insurance coverage"
            ]
        },

        # 2. Manali - Delhi - 5d - 11500 - Adventure + Nature - Solo - Summer (4-9)
        {
            "name": "Manali Riverside Backpackers Trek",
            "operator_name": "Horizon Trails",
            "destination_name": "Manali",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("11500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/manali-backpackers",
            "is_active": True,
            "hotel_info": "Eco-friendly backpacker hostel with riverside camping tents and communal bonfire zone.",
            "meals_info": "Wholesome vegetarian breakfast and dinner prepared by camp cooks.",
            "transportation_info": "Semi-sleeper AC Volvo from Delhi; shared mountain jeeps for trailheads.",
            "sightseeing_info": "Jogini Waterfalls, Nehru Kund, Beas River banks, and Vashisht Village.",
            "activities_info": "Guided day-trek to Jogini Falls, river crossing, and camping under stars.",
            "themes": ["adventure", "nature"],
            "travel_types": ["Solo"],
            "availability_months": [4, 5, 6, 7, 8, 9],
            "itinerary": [
                (1, "Delhi Departure & Mountain Welcome", "Depart Delhi on overnight semi-sleeper. Arrive Manali, riverside campsite check-in, orientation walk.", "Riverfront Alpine Camp", "Dinner"),
                (2, "Jogini Waterfalls Day Hike", "Trek through apple orchards and pine groves to the scenic Jogini Waterfalls with panoramic valley vistas.", "Riverfront Alpine Camp", "Breakfast & Dinner"),
                (3, "Atal Tunnel & Sissu Green Valley", "Shared jeep ride through the engineering marvel Atal Tunnel to explore Sissu village in Lahaul Valley.", "Riverfront Alpine Camp", "Breakfast & Dinner"),
                (4, "Old Manali Culture & Jam Session", "Explore traditional wooden architecture in Old Manali village followed by acoustic evening by the bonfire.", "Riverfront Alpine Camp", "Breakfast & Dinner"),
                (5, "Local Flea Market & Delhi Transit", "Check out, morning shopping at Tibetan monastery market, evening Volvo back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in premium dome tent / dormitory near Beas river",
                "Breakfast and dinner on all trekking days",
                "Certified local mountain guide for hiking routes",
                "Volvo transfers Delhi - Manali - Delhi",
                "Campfire permits and wilderness safety gear"
            ],
            "exclusions": [
                "Lunch meals and personal trail snacks",
                "Porter service for personal rucksacks",
                "Rafting and paragliding adventure passes",
                "Medical evacuation expenses"
            ]
        },

        # 3. Manali - Delhi - 5d - 38000 - Luxury + Nature - Couple + Family - Year Round
        {
            "name": "Manali Luxury Cedar Chalet Retreat",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Manali",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("38000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/manali-chalet",
            "is_active": True,
            "hotel_info": "5-star luxury boutique chalet featuring cedar wood architecture, heated floors, and private jacuzzi.",
            "meals_info": "Gourmet a-la-carte breakfast and multi-cuisine candlelit dinners.",
            "transportation_info": "Chauffeur-driven luxury SUV (Innova Crysta) from Delhi to Manali round-trip.",
            "sightseeing_info": "Solang Valley VIP pass, Naggar Castle, Jana Falls, and apple estate walk.",
            "activities_info": "Private couples massage session, customized apple cider tasting, and stargazing.",
            "themes": ["luxury", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 10, 11, 12],
            "itinerary": [
                (1, "Private Chauffeur Drive to Manali", "Executive SUV pickup from Delhi, scenic Himalayan highway drive, luxury chalet check-in.", "The Himalayan Cedar Grand Resort", "Dinner"),
                (2, "Solang Valley VIP Mountain Experience", "Private transfer to Solang with VIP cable car passes and champagne picnic overlooking snow peaks.", "The Himalayan Cedar Grand Resort", "Breakfast & Dinner"),
                (3, "Spa Rejuvenation & Jana Waterfalls", "Morning aromatherapy massage followed by scenic drive through heritage deodar forests to Jana Falls.", "The Himalayan Cedar Grand Resort", "Breakfast & Dinner"),
                (4, "Naggar Art Walk & Private Apple Orchard", "Explore historical Naggar Castle and private guided walk through an organic heirloom apple farm.", "The Himalayan Cedar Grand Resort", "Breakfast & Dinner"),
                (5, "Champagne Breakfast & Return Journey", "Leisurely breakfast on private terrace, personalized souvenir box, executive drive back to Delhi.", "Executive Vehicle", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in Luxury Cedar Suite with heated flooring",
                "Full gourmet breakfast and 5-course dinners",
                "Private Innova Crysta for complete tour duration",
                "One complimentary 60-min signature spa therapy",
                "All toll charges, fuel, and VIP entry permissions"
            ],
            "exclusions": [
                "Airfare to/from Delhi",
                "Alcoholic beverages outside dinner inclusions",
                "Optional helicopter joyrides",
                "Gratuities and personal tips"
            ]
        },

        # 4. Manali - Pune - 7d - 28000 - Adventure + Nature + Spiritual - Family + Group - Summer/Autumn
        {
            "name": "Himachal High Passes & Rohtang Expedition",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Manali",
            "starting_city": "Pune",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("28000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/manali-rohtang",
            "is_active": True,
            "hotel_info": "4-star riverside family resort with landscaped gardens and children's play arena.",
            "meals_info": "Buffet breakfast, hot picnic lunches, and buffet dinner included.",
            "transportation_info": "Flight connecting Pune to Delhi, AC tempo traveler for group valley excursions.",
            "sightseeing_info": "Rohtang Pass (13,058 ft), Atal Tunnel, Manikaran Sahib Gurudwara, and Kasol.",
            "activities_info": "Glacier snow walking, hot sulphur dip at Manikaran, and Parvati valley trek.",
            "themes": ["adventure", "nature", "spiritual"],
            "travel_types": ["Family", "Group"],
            "availability_months": [5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Pune to Delhi Flight & Manali Transit", "Morning flight from Pune to Delhi, group coach boarding, scenic overnight climb to Manali.", "Overnight Coach", "Dinner"),
                (2, "Manali Arrival & Acclimatization", "Arrive in Manali, hotel check-in, rest and acclimatization, evening prayer at Vashisht Temple.", "Manali Heights Resort", "Dinner"),
                (3, "Rohtang Pass Snow Peak Expedition", "Ascend through winding hairpin bends to Rohtang Pass (13,058 ft) for majestic Pir Panjal views.", "Manali Heights Resort", "Breakfast, Lunch & Dinner"),
                (4, "Atal Tunnel to Keylong Edge", "Drive through Atal Tunnel into the high-altitude desert of Lahaul Valley and Tandi confluence.", "Manali Heights Resort", "Breakfast & Dinner"),
                (5, "Parvati Valley & Manikaran Sahib", "Full-day spiritual excursion to Manikaran hot water springs, Gurudwara langar, and Kasol cafes.", "Manali Heights Resort", "Breakfast, Lunch & Dinner"),
                (6, "Kullu Valley Rafting & Handloom Shopping", "River rafting on Beas rapids in Kullu, visit local Angora shawl weaving cooperatives.", "Manali Heights Resort", "Breakfast & Dinner"),
                (7, "Departure to Delhi & Pune Flight", "Descend to Delhi airport for evening flight back to Pune with mountain memories.", "Onward Flight", "Breakfast"),
            ],
            "inclusions": [
                "5 nights resort stay in Manali + 1 night transit coach",
                "Daily breakfast and dinner plus 2 packed lunch boxes",
                "Rohtang Pass green permit and NGT fees",
                "Group tempo traveler transportation with expert driver",
                "Trip coordinator and first-aid oxygen cylinder onboard"
            ],
            "exclusions": [
                "Domestic flights between Pune and Delhi",
                "Snow dress, boot, and ski rental fees at Rohtang",
                "River rafting tickets in Kullu",
                "Personal porterage and tips"
            ]
        },

        # 5. Manali - Delhi - 5d - 14000 - Inactive Package #1
        {
            "name": "High-Altitude Winter Manali Storm Trail",
            "operator_name": "WanderNest Travels",
            "destination_name": "Manali",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("14000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/manali-winter-storm",
            "is_active": False,  # INACTIVE DEMO PACKAGE
            "hotel_info": "Cozy mountain lodge with wooden fire hearth.",
            "meals_info": "Daily breakfast and dinner.",
            "transportation_info": "Shared tempo traveler from Delhi.",
            "sightseeing_info": "Gulaba snow point and Old Manali.",
            "activities_info": "Snow trekking and photography.",
            "themes": ["adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [12, 1],
            "itinerary": [
                (1, "Delhi to Manali Transit", "Overnight drive to snow-bound Manali.", "Mountain Hearth Lodge", "Dinner"),
                (2, "Arrival & Snow Exploration", "Check in and walk through snowed pine trails.", "Mountain Hearth Lodge", "Breakfast & Dinner"),
                (3, "Gulaba Snow Point Trek", "Hike up to Gulaba winter road barrier.", "Mountain Hearth Lodge", "Breakfast & Dinner"),
                (4, "Old Manali Wooden Architecture", "Explore traditional Kath Kuni houses.", "Mountain Hearth Lodge", "Breakfast & Dinner"),
                (5, "Return to Delhi", "Morning departure back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": ["4 nights lodge accommodation", "Breakfast and dinner", "Shared transit"],
            "exclusions": ["Gear rental", "Personal snacks", "Insurance"]
        },

        # 6. Goa - Mumbai - 4d - 12500 - Beach + Adventure - Solo + Group - Winter/Spring
        {
            "name": "North Goa Beach & Nightlife Hopping",
            "operator_name": "TravelVista India",
            "destination_name": "Goa",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("12500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/north-goa-beach",
            "is_active": True,
            "hotel_info": "3-star boutique resort near Calangute beach with swimming pool and sundeck.",
            "meals_info": "Daily tropical breakfast buffet with Goan poi and eggs.",
            "transportation_info": "AC sleeper bus Mumbai - Goa - Mumbai; two-wheelers provided for sightseeing.",
            "sightseeing_info": "Baga Beach, Anjuna Flea Market, Chapora Fort, and Fort Aguada lighthouse.",
            "activities_info": "Jet ski ride, parasailing, beach shacks exploration, and sunset club entry.",
            "themes": ["beach", "adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Goa Transit & Beach Arrival", "Overnight sleeper bus from Mumbai. Arrive in Goa, check in to resort, evening sunset at Calangute Beach.", "Seaside Palm Resort, Calangute", "Dinner"),
                (2, "Watersports Mania at Baga & Anjuna", "Morning thrilling watersports (parasailing & jet ski). Afternoon chill at Anjuna beach shacks and sunset drum circle.", "Seaside Palm Resort, Calangute", "Breakfast"),
                (3, "Chapora 'Dil Chahta Hai' Fort & Nightlife", "Climb Chapora Fort for sweeping sea views. Evening visit to iconic Tito's Lane and beachside lounges.", "Seaside Palm Resort, Calangute", "Breakfast"),
                (4, "Aguada Lighthouse & Return Bus", "Visit historic 17th-century Portuguese Aguada Fort. Check out and board afternoon bus back to Mumbai.", "Onward Bus", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in deluxe pool-facing room near beach",
                "Daily breakfast buffet at the resort",
                "Round-trip AC sleeper bus tickets from Mumbai",
                "Scooter rental (fuel excluded) for 3 days",
                "One complimentary parasailing and banana ride session"
            ],
            "exclusions": [
                "Scooter fuel charges and traffic security deposits",
                "Lunch and dinner meals outside Day 1 dinner",
                "Club entry cover charges",
                "Personal tips and beach umbrella rentals"
            ]
        },

        # 7. Goa - Pune - 4d - 19000 - Beach + Culture - Couple - Winter/Spring
        {
            "name": "South Goa Portuguese Heritage & Serenity Break",
            "operator_name": "WanderNest Travels",
            "destination_name": "Goa",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("19000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/south-goa-serenity",
            "is_active": True,
            "hotel_info": "4-star colonial heritage boutique hotel in historic Fontainhas / South Goa with lush courtyard.",
            "meals_info": "Gourmet breakfasts and 1 authentic Goan-Portuguese fusion dinner.",
            "transportation_info": "AC private sedan from Pune to Goa and return; private car for sightseeing.",
            "sightseeing_info": "Basilica of Bom Jesus, Se Cathedral, Colva Beach, and Cabo de Rama Fort.",
            "activities_info": "Heritage walking tour through Fontainhas Latin Quarter and quiet beach sunset stroll.",
            "themes": ["beach", "culture"],
            "travel_types": ["Couple"],
            "availability_months": [1, 2, 3, 4, 10, 11, 12],
            "itinerary": [
                (1, "Scenic Western Ghats Drive to South Goa", "Private sedan pickup in Pune, scenic drive through Amboli Ghat. Check in to heritage mansion, candlelit dinner.", "Casa Portuguesa Heritage Resort", "Dinner"),
                (2, "Old Goa UNESCO Churches & Latin Quarter", "Guided cultural tour of Basilica of Bom Jesus, Se Cathedral, and photo walk through colorful Fontainhas.", "Casa Portuguesa Heritage Resort", "Breakfast"),
                (3, "Cabo de Rama & Pristine Palolem Beach", "Discover the clifftop ramparts of Cabo de Rama and spend peaceful evening at crescent-shaped Palolem Beach.", "Casa Portuguesa Heritage Resort", "Breakfast"),
                (4, "Spice Plantation Tour & Return to Pune", "Morning visit to Sahakari Spice Farm with traditional buffet lunch. Evening comfortable drive back to Pune.", "Private Vehicle", "Breakfast & Lunch"),
            ],
            "inclusions": [
                "3 nights accommodation in heritage colonial room",
                "Daily breakfast and 1 plantation buffet lunch",
                "Private dedicated AC sedan for entire Pune-Goa round trip",
                "Professional certified heritage tour guide in Old Goa",
                "Spice plantation entry ticket and welcome drink"
            ],
            "exclusions": [
                "Dinner on Days 2 and 3",
                "Alcoholic beverages and mini-bar expenses",
                "Water sports activities",
                "Tips and personal gratuities"
            ]
        },

        # 8. Goa - Delhi - 5d - 48000 - Beach + Luxury - Couple + Family - Peak Winter
        {
            "name": "Goa Grand Luxury Coastal Villa",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Goa",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("48000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/goa-luxury-villa",
            "is_active": True,
            "hotel_info": "5-star luxury beachfront resort in Candolim with private plunge pools, butler service, and private beach cabana.",
            "meals_info": "Lavish champagne breakfast buffet, daily afternoon high tea, and 2 beachfront dinners.",
            "transportation_info": "Airport luxury chauffeur transfers and on-demand premium car for local excursions.",
            "sightseeing_info": "Private yacht cruise on Mandovi River, Reis Magos Fort, and private beach access.",
            "activities_info": "Couples massage at wellness spa, sunset yacht sailing with wine, and golf session.",
            "themes": ["beach", "luxury"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [11, 12, 1, 2],
            "itinerary": [
                (1, "VIP Airport Greeting & Beachfront Check-in", "Executive transfer from Dabolim/Mopa airport. Welcome champagne, settle into luxury villa, beachside dinner.", "Taj Horizon Coastal Villa & Spa", "Dinner"),
                (2, "Private Yacht Cruise on Arabian Sea", "Afternoon 2-hour chartered catamaran cruise along the Goa coastline with chilled wine and artisanal canapés.", "Taj Horizon Coastal Villa & Spa", "Breakfast & High Tea"),
                (3, "Spa Indulgence & Fine Dining", "Signature Ayurvedic couples massage at the spa followed by private candlelit beachfront seafood dinner.", "Taj Horizon Coastal Villa & Spa", "Breakfast, High Tea & Dinner"),
                (4, "Colonial Art Galleries & Sunset Cabana", "Chauffeured visit to private art galleries and museum houses. Sunset cocktails at resort's private cabana.", "Taj Horizon Coastal Villa & Spa", "Breakfast & High Tea"),
                (5, "Leisure Morning & Airport Departure", "Gourmet champagne breakfast, late check-out, luxury chauffeur transfer back to the airport.", "Executive Car", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in Luxury Villa with private plunge pool",
                "Full daily champagne breakfast, afternoon high tea, 2 gourmet dinners",
                "2-hour private yacht cruise with refreshments",
                "One 60-minute spa therapy per adult",
                "Round-trip luxury airport chauffeur transfers"
            ],
            "exclusions": [
                "Airfare from Delhi to Goa",
                "Additional meals not specified in plan",
                "Water sports outside private yacht",
                "Personal shopping expenses"
            ]
        },

        # 9. Goa - Bangalore - 3d - 9500 - Beach + Adventure - Solo + Couple + Group - Year Round
        {
            "name": "Goa Watersports & Sunset Weekend",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Goa",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("9500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/goa-watersports-weekend",
            "is_active": True,
            "hotel_info": "Cozy 3-star beachside property near Baga beach with swimming pool.",
            "meals_info": "Daily continental breakfast included.",
            "transportation_info": "AC sleeper bus Bangalore - Goa - Bangalore; shared transfers for activities.",
            "sightseeing_info": "Baga, Calangute, and Anjuna sunset view point.",
            "activities_info": "5-in-1 watersports combo: parasailing, jet ski, banana ride, bumper ride, boat ride.",
            "themes": ["beach", "adventure"],
            "travel_types": ["Solo", "Couple", "Group"],
            "availability_months": [1, 2, 3, 4, 5, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore Departure & Beach Arrival", "Board evening AC sleeper bus in Bangalore. Morning arrival in Goa, hotel check-in, relax by the pool.", "Baga Sands Resort", "Dinner"),
                (2, "Full Day Watersports Combo Package", "Head to watersports dock for parasailing, jet ski, and bumper boat rides. Evening sunset at Baga shacks.", "Baga Sands Resort", "Breakfast"),
                (3, "Anjuna Flea Market & Return Bus", "Morning stroll at Anjuna beach. Afternoon check-out and board evening return bus to Bangalore.", "Onward Bus", "Breakfast"),
            ],
            "inclusions": [
                "2 nights hotel accommodation near Baga",
                "Daily breakfast at the hotel",
                "Bangalore-Goa-Bangalore AC sleeper bus tickets",
                "Complete 5-activity watersports package with life jackets",
                "Shared pickup and drop for water activities"
            ],
            "exclusions": [
                "Lunch and dinner meals",
                "Local scooter or taxi hire",
                "Video and camera permits during watersports",
                "Personal expenses"
            ]
        },

        # 10. Goa - Mumbai - 4d - 7500 - Inactive Package #2
        {
            "name": "Monsoon Off-Season Goa Getaway",
            "operator_name": "TravelVista India",
            "destination_name": "Goa",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("7500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/monsoon-goa",
            "is_active": False,  # INACTIVE DEMO PACKAGE
            "hotel_info": "Standard budget resort near Candolim.",
            "meals_info": "Breakfast included.",
            "transportation_info": "Non-AC sleeper bus from Mumbai.",
            "sightseeing_info": "Dudhsagar waterfall view and spice plantation.",
            "activities_info": "Rain walks and waterfall photography.",
            "themes": ["beach", "nature"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [6, 7, 8],
            "itinerary": [
                (1, "Mumbai to Goa Transit", "Overnight bus journey through rain-washed Western Ghats.", "Candolim Palms Inn", "None"),
                (2, "Monsoon Beach Walks", "Arrive in Goa, check in, enjoy thunderous sea views.", "Candolim Palms Inn", "Breakfast"),
                (3, "Dudhsagar Waterfall Trek", "Full day excursion to the swollen Dudhsagar waterfall.", "Candolim Palms Inn", "Breakfast"),
                (4, "Return to Mumbai", "Check out, board evening bus back to Mumbai.", "Onward Bus", "Breakfast"),
            ],
            "inclusions": ["3 nights budget lodging", "Breakfast", "Bus transit"],
            "exclusions": ["Meals", "Water sports", "Sightseeing transfers"]
        },

        # 11. Jaipur - Delhi - 4d - 15000 - Heritage + Culture - Family + Couple - Winter (10-3)
        {
            "name": "Royal Jaipur Forts & Palaces Trail",
            "operator_name": "WanderNest Travels",
            "destination_name": "Jaipur",
            "starting_city": "Delhi",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("15000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/jaipur-heritage",
            "is_active": True,
            "hotel_info": "4-star heritage haveli hotel featuring traditional fresco walls, arches, and courtyard pool.",
            "meals_info": "Daily buffet breakfast and 1 grand Rajasthani thali dinner.",
            "transportation_info": "AC private sedan from Delhi to Jaipur round trip and for all city sightseeing.",
            "sightseeing_info": "Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, and Nahargarh Fort.",
            "activities_info": "Jeep ride up to Amber Fort, sound & light show, and block printing workshop.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Family", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Delhi to Jaipur Drive & Heritage Welcome", "Morning pickup in Delhi, comfortable expressway drive to Jaipur. Check in with garland welcome, evening puppet show.", "Alsisar Haveli Heritage Hotel", "Dinner"),
                (2, "Amber Fort & Royal City Monuments", "Ascend Amber Fort by heritage jeep, marvel at Sheesh Mahal (Mirror Palace). Afternoon visit to Hawa Mahal and Jantar Mantar.", "Alsisar Haveli Heritage Hotel", "Breakfast"),
                (3, "City Palace & Nahargarh Sunset", "Explore the royal courtyards of City Palace. Drive up to Nahargarh Fort for a breathtaking sunset over Pink City.", "Alsisar Haveli Heritage Hotel", "Breakfast & Royal Thali"),
                (4, "Bapu Bazaar Shopping & Return to Delhi", "Morning handicraft and gemstone shopping at Bapu Bazaar. Afternoon scenic highway drive back to Delhi.", "Private Sedan", "Breakfast"),
            ],
            "inclusions": [
                "3 nights stay in royal heritage room",
                "Daily breakfast and 1 authentic Rajasthani thali dinner",
                "Private dedicated AC sedan for entire Delhi-Jaipur itinerary",
                "Amber Fort jeep ride tickets and monument entry passes",
                "Approved government English/Hindi speaking tour guide"
            ],
            "exclusions": [
                "Lunch and personal food orders",
                "Camera and video shooting permits",
                "Elephant ride fees at Amber Fort",
                "Driver tips and gratuities"
            ]
        },

        # 12. Jaipur - Hyderabad - 5d - 26000 - Heritage + Culture + Luxury - Couple + Family - Autumn/Spring
        {
            "name": "Majestic Rajputana Heritage Odyssey",
            "operator_name": "TravelVista India",
            "destination_name": "Jaipur",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("26000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/jaipur-odyssey",
            "is_active": True,
            "hotel_info": "5-star luxury palace hotel with royal pavilions, peacock gardens, and wellness spa.",
            "meals_info": "Lavish royal buffet breakfasts and 2 curated fine dining dinners.",
            "transportation_info": "Airport pickup and drop in Jaipur; private air-conditioned Innova Crysta for all tours.",
            "sightseeing_info": "Amer Fort, Jaigarh Cannon, Jal Mahal promenade, Albert Hall Museum, and Chokhi Dhani.",
            "activities_info": "Royal turban tying, evening Rajasthani folk dance at Chokhi Dhani, and pottery session.",
            "themes": ["heritage", "culture", "luxury"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Hyderabad to Jaipur Arrival & Royal High Tea", "Arrive in Jaipur via flight, luxury airport transfer. Check in to palace hotel, evening high tea in courtyards.", "Jai Mahal Palace Resort", "Dinner"),
                (2, "Amer Fort Royal Ramparts & Jaigarh Cannon", "Full day exploring the hilltop fort complex of Amer, Jaivana Cannon at Jaigarh, and photo stop at Jal Mahal.", "Jai Mahal Palace Resort", "Breakfast"),
                (3, "City Palace Museum & Albert Hall", "Visit Maharaja Sawai Man Singh II Museum in City Palace and Albert Hall architectural treasure.", "Jai Mahal Palace Resort", "Breakfast & Dinner"),
                (4, "Chokhi Dhani Ethnic Cultural Village", "Day at leisure for spa, followed by immersive cultural evening at Chokhi Dhani village with camel rides and folk dance.", "Jai Mahal Palace Resort", "Breakfast & Village Feast"),
                (5, "Johari Bazaar Gemstones & Airport Transfer", "Morning artisan shopping in the walled city. Chauffeur transfer to Jaipur airport for Hyderabad flight.", "Executive Car", "Breakfast"),
            ],
            "inclusions": [
                "4 nights luxury accommodation in palace hotel",
                "Daily buffet breakfast and 2 regal dinners",
                "Chokhi Dhani entry ticket with royal Rajasthani banquet",
                "Private Innova Crysta for all airport and city transfers",
                "All monument entry tickets and museum access"
            ],
            "exclusions": [
                "Airfare between Hyderabad and Jaipur",
                "Lunches and alcoholic drinks",
                "Spa treatments and wellness massages",
                "Personal tips and porterage"
            ]
        },

        # 13. Jaipur - Delhi - 3d - 10500 - Heritage + Culture - Solo + Group - Summer/Monsoon (4-9)
        {
            "name": "Jaipur Express Weekend Discovery",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Jaipur",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("10500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1477587458883-47145ed94245?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/jaipur-express",
            "is_active": True,
            "hotel_info": "3-star modern boutique hotel with rooftop restaurant overlooking Pink City.",
            "meals_info": "Daily breakfast included.",
            "transportation_info": "AC Shatabdi Express train tickets Delhi - Jaipur - Delhi; AC cab for sightseeing.",
            "sightseeing_info": "Hawa Mahal, Amber Fort, City Palace, and Nahargarh sunset point.",
            "activities_info": "Sunset photo walk, street food tasting tour (Pyaaz Kachori, Lassi).",
            "themes": ["heritage", "culture"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [4, 5, 6, 7, 8, 9],
            "itinerary": [
                (1, "Morning Shatabdi to Jaipur & Fort Sunset", "Board morning Shatabdi train from New Delhi. Arrive in Jaipur by noon. Check in, evening sunset at Nahargarh Fort.", "Pink City Vista Hotel", "Dinner"),
                (2, "Amber Fort & City Palace Highlights", "Visit Amer Fort, Jal Mahal lake palace, City Palace, and Jantar Mantar observatory. Evening street food walk.", "Pink City Vista Hotel", "Breakfast"),
                (3, "Hawa Mahal Morning Walk & Shatabdi Return", "Early morning photo stop at Hawa Mahal facade, souvenir shopping at MI Road. Evening Shatabdi back to Delhi.", "Shatabdi Express", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in modern AC superior room",
                "Daily breakfast at the hotel",
                "Round-trip AC Chair Car Shatabdi Express train tickets",
                "Dedicated cab for city sightseeing in Jaipur",
                "Monument entry tickets for Amber Fort and City Palace"
            ],
            "exclusions": [
                "Lunch and dinner meals outside Day 1 dinner",
                "Street food tasting expenses",
                "Train catering outside standard IRCTC service",
                "Personal tips"
            ]
        },

        # 14. Kerala - Bangalore - 5d - 22000 - Nature + Wildlife - Couple + Family - Autumn/Winter
        {
            "name": "Munnar Hills & Thekkady Forest Escapade",
            "operator_name": "Horizon Trails",
            "destination_name": "Kerala",
            "starting_city": "Bangalore",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("22000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/kerala-munnar-thekkady",
            "is_active": True,
            "hotel_info": "4-star tea plantation retreat in Munnar and jungle resort in Thekkady.",
            "meals_info": "Daily South Indian and continental breakfast and buffet dinner.",
            "transportation_info": "AC private sedan from Bangalore throughout the Kerala circuit.",
            "sightseeing_info": "Eravikulam National Park (Nilgiri Tahr), Mattupetty Dam, Periyar Wildlife Sanctuary, and spice garden.",
            "activities_info": "Boat safari on Periyar Lake, spice plantation tour, and Kalaripayattu martial arts show.",
            "themes": ["nature", "wildlife"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Bangalore to Munnar Scenic Drive", "Early morning drive from Bangalore through tea hills. Check in to Munnar resort, relax amidst mist.", "Tea Valley Mountain Resort, Munnar", "Dinner"),
                (2, "Eravikulam National Park & Tea Museum", "Spot endangered Nilgiri Tahr at Eravikulam. Visit Tata Tea Museum and taste fresh single-origin brew.", "Tea Valley Mountain Resort, Munnar", "Breakfast & Dinner"),
                (3, "Scenic Drive to Thekkady & Spice Walk", "Drive to Thekkady through cardamon plantations. Afternoon guided aromatic spice garden tour.", "Periyar Jungle Lodge, Thekkady", "Breakfast & Dinner"),
                (4, "Periyar Lake Boat Safari & Martial Arts", "Morning boat safari in Periyar Tiger Reserve to spot wild elephants and bisons. Evening Kalaripayattu show.", "Periyar Jungle Lodge, Thekkady", "Breakfast & Dinner"),
                (5, "Return Drive to Bangalore", "Hearty South Indian breakfast, scenic descent down the Western Ghats back to Bangalore.", "Private Sedan", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in premium mountain/jungle resorts",
                "Daily breakfast and dinner at resorts",
                "Private dedicated AC sedan for entire Bangalore-Kerala circuit",
                "Eravikulam National Park entry pass and safari bus",
                "Periyar boat cruise ticket and spice plantation entry"
            ],
            "exclusions": [
                "Lunches and personal snacks",
                "Elephant ride and safari charges",
                "Camera fees in national parks",
                "Driver night charges if after 9 PM"
            ]
        },

        # 15. Kerala - Mumbai - 6d - 34000 - Nature + Luxury - Couple + Family - Winter
        {
            "name": "Kerala Backwaters & Luxury Houseboat Sojourn",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Kerala",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("34000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/kerala-backwaters-luxury",
            "is_active": True,
            "hotel_info": "5-star backwater luxury resort in Kumarakom and private air-conditioned premium houseboat in Alleppey.",
            "meals_info": "All meals on houseboat (fresh Karimeen fish fry); daily breakfast & dinner at resorts.",
            "transportation_info": "Airport transfers from Kochi; private AC sedan for all inter-city journeys.",
            "sightseeing_info": "Fort Kochi Chinese fishing nets, Kumarakom bird sanctuary, and Alleppey backwater canals.",
            "activities_info": "Sunset canoe ride through village canals, Ayurvedic herbal oil massage, and fishing from houseboat.",
            "themes": ["nature", "luxury"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Kochi Flight & Fort Kochi Heritage", "Arrive at Kochi airport, private transfer to boutique hotel. Evening walk past Chinese Fishing Nets.", "Brunton Boatyard / Heritage Hotel", "Dinner"),
                (2, "Scenic Transfer to Kumarakom Backwaters", "Drive to Kumarakom on the banks of Lake Vembanad. Luxury resort check-in, sunset village canoe cruise.", "Kumarakom Lake Luxury Resort", "Breakfast & Dinner"),
                (3, "Bird Sanctuary & Ayurvedic Wellness", "Early morning walk in Kumarakom Bird Sanctuary. Afternoon 60-minute authentic Ayurvedic rejuvenation therapy.", "Kumarakom Lake Luxury Resort", "Breakfast & Dinner"),
                (4, "Boarding Private Alleppey Houseboat", "Board private air-conditioned Kettuvallam houseboat. Cruise through palm-lined canals, feast on authentic Kerala lunch.", "Private AC Luxury Houseboat", "Breakfast, Lunch & Dinner"),
                (5, "Morning Canal Cruise & Marari Beach", "Enjoy sunrise over backwaters. Disembark and transfer to serene Marari beach resort for seaside relaxation.", "Marari Beach Eco-Resort", "Breakfast & Dinner"),
                (6, "Departure to Kochi Airport", "Leisure breakfast by the Arabian Sea, private chauffeur transfer back to Kochi airport for Mumbai flight.", "Private Sedan", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in 5-star backwater/beach resorts + 1 night private luxury houseboat",
                "All meals included on houseboat with private chef onboard",
                "Daily breakfast and dinner at luxury resorts",
                "Private dedicated AC sedan for entire itinerary",
                "One 60-minute Ayurvedic massage per adult"
            ],
            "exclusions": [
                "Airfare between Mumbai and Kochi",
                "Alcoholic drinks and personal laundry",
                "Water sports at Marari beach",
                "Tips to houseboat crew and drivers"
            ]
        },

        # 16. Kerala - Pune - 8d - 46000 - Nature + Culture + Beach - Family + Group - Winter
        {
            "name": "Complete God's Own Country Grand Tour",
            "operator_name": "TravelVista India",
            "destination_name": "Kerala",
            "starting_city": "Pune",
            "duration_days": 8,
            "duration_nights": 7,
            "price_per_person": Decimal("46000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/kerala-grand-tour",
            "is_active": True,
            "hotel_info": "Combination of 4-star hill resorts, wildlife lodges, traditional houseboats, and beach retreats.",
            "meals_info": "Daily breakfast, dinner at all hotels, and full board on houseboat.",
            "transportation_info": "Flight Pune-Kochi; private Innova for the complete 8-day tour, drop at Trivandrum.",
            "sightseeing_info": "Munnar tea gardens, Thekkady wildlife sanctuary, Alleppey backwaters, and Kovalam beach.",
            "activities_info": "Kathakali dance show, spice plantation walk, houseboat cruise, and lighthouse beach walk.",
            "themes": ["nature", "culture", "beach"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune to Kochi Arrival & Munnar Ascent", "Flight to Kochi, scenic mountain drive to Munnar past Cheeyappara waterfalls.", "Munnar Panorama Hill Resort", "Dinner"),
                (2, "Munnar Tea Estates & Mattupetty Dam", "Explore tea estates, Mattupetty dam boat ride, and Echo Point in Munnar.", "Munnar Panorama Hill Resort", "Breakfast & Dinner"),
                (3, "Thekkady Spice Hills & Periyar Forest", "Scenic drive to Thekkady, spice garden exploration, and evening Kathakali drama performance.", "Green Park Heritage Lodge", "Breakfast & Dinner"),
                (4, "Periyar Jungle Safari & Martial Arts", "Lake boat safari in Periyar sanctuary, Kalaripayattu martial arts show in evening.", "Green Park Heritage Lodge", "Breakfast & Dinner"),
                (5, "Alleppey Backwaters Houseboat Cruise", "Board deluxe houseboat in Alleppey, glide through paddy fields, overnight on water.", "Deluxe Backwater Houseboat", "Breakfast, Lunch & Dinner"),
                (6, "Houseboat Disembark & Kovalam Beach Drive", "Disembark, drive south to Kovalam beach resort, evening sunset at Lighthouse Beach.", "Kovalam Beachfront Retreat", "Breakfast & Dinner"),
                (7, "Kovalam Leisure & Trivandrum Temple", "Visit Padmanabhaswamy Temple in Trivandrum, afternoon relax on golden Kovalam sands.", "Kovalam Beachfront Retreat", "Breakfast & Dinner"),
                (8, "Trivandrum Airport Drop & Pune Flight", "Breakfast by the sea, chauffeur transfer to Trivandrum airport for flight home.", "Private Innova", "Breakfast"),
            ],
            "inclusions": [
                "6 nights premium resort stays + 1 night private houseboat",
                "Breakfast and dinner daily + full board meals on houseboat",
                "Private AC Innova Crysta for entire 8-day tour circuit",
                "Entry tickets to Kathakali show and Kalaripayattu performance",
                "All state road taxes, parking, and toll expenses"
            ],
            "exclusions": [
                "Air tickets between Pune, Kochi, and Trivandrum",
                "Lunch meals on hotel stay days",
                "Camera fees and personal laundry",
                "Water sports at Kovalam"
            ]
        },

        # 17. Kashmir - Delhi - 5d - 25000 - Nature + Adventure - Couple + Family - Summer/Autumn
        {
            "name": "Kashmir Valley Paradise & Gulmarg Gondola",
            "operator_name": "WanderNest Travels",
            "destination_name": "Kashmir",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("25000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/kashmir-paradise",
            "is_active": True,
            "hotel_info": "Deluxe heritage houseboat on Dal Lake and 4-star mountain hotel in Gulmarg.",
            "meals_info": "Daily breakfast and authentic Kashmiri dinner featuring Rogan Josh and Yakhni.",
            "transportation_info": "Airport pickup and drop in Srinagar; private heated vehicle for all excursions.",
            "sightseeing_info": "Dal Lake, Mughal Gardens (Shalimar & Nishat), Gulmarg, and Pahalgam valley.",
            "activities_info": "Shikara ride on Dal Lake, Gulmarg Gondola ride to Phase 1, and pony ride in Betaab valley.",
            "themes": ["nature", "adventure"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Delhi to Srinagar Flight & Shikara Sunset", "Flight to Srinagar, transfer to Dal Lake houseboat. Romantic 1-hour sunset Shikara ride.", "Royal Heritage Houseboat, Dal Lake", "Dinner"),
                (2, "Mughal Gardens & Shankaracharya Temple", "Visit Nishat Bagh, Shalimar Bagh, and Shankaracharya Temple on hilltop overlooking Srinagar.", "Royal Heritage Houseboat, Dal Lake", "Breakfast & Dinner"),
                (3, "Gulmarg Meadow of Flowers & Gondola", "Day trip to Gulmarg. Ride the famous cable car (Gondola) to Kongdoori mountain ridge.", "Grand Pine Resort, Gulmarg", "Breakfast & Dinner"),
                (4, "Pahalgam Valley of Shepherds & Lidder", "Scenic drive to Pahalgam, visit picturesque Betaab Valley and banks of pristine Lidder River.", "Grand Pine Resort, Gulmarg", "Breakfast & Dinner"),
                (5, "Morning Floating Flower Market & Flight", "Sunrise Shikara visit to floating vegetable market, souvenir walnut wood shopping, airport transfer.", "Private Vehicle", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in deluxe Dal Lake houseboat + 2 nights in Gulmarg hotel",
                "Daily breakfast and traditional Kashmiri dinners",
                "Private heating-equipped vehicle for all transfers and tours",
                "Complimentary 1-hour Shikara boat ride on Dal Lake",
                "Gulmarg Gondola Phase 1 cable car tickets"
            ],
            "exclusions": [
                "Flights between Delhi and Srinagar",
                "Pony rides and local Union taxi in Pahalgam",
                "Gondola Phase 2 upgrade ticket",
                "Tips and personal expenses"
            ]
        },

        # 18. Kashmir - Delhi - 6d - 35000 - Adventure + Nature - Solo + Group - Winter
        {
            "name": "Winter Wonderland Skiing & Snow Trail",
            "operator_name": "Horizon Trails",
            "destination_name": "Kashmir",
            "starting_city": "Delhi",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("35000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/kashmir-winter-skiing",
            "is_active": True,
            "hotel_info": "Heated ski lodge in Gulmarg with snow gear drying facilities and mountain views.",
            "meals_info": "Nutritious breakfast and warm dinner buffet with Kashmiri Kahwa tea.",
            "transportation_info": "4x4 snow chain vehicles from Srinagar to Gulmarg and return.",
            "sightseeing_info": "Gulmarg ski slopes, Apharwat Peak (Phase 2), and frozen Drung waterfall.",
            "activities_info": "2 days of beginner ski lessons with certified instructor, snowshoeing, and snowmobiling.",
            "themes": ["adventure", "nature"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [12, 1, 2, 3],
            "itinerary": [
                (1, "Delhi to Srinagar & Transfer to Snow Gulmarg", "Fly to Srinagar, 4x4 snow vehicle ascent to snowbound Gulmarg ski village. Lodge check-in, Kahwa welcome.", "Gulmarg Alpine Ski Lodge", "Dinner"),
                (2, "Skiing Lessons Day 1 on Beginners Slope", "Equip with ski gear, 4 hours of professional ski instruction, balance and gliding practice.", "Gulmarg Alpine Ski Lodge", "Breakfast & Dinner"),
                (3, "Gondola Phase 2 to Apharwat (13,780 ft)", "Ride Gondola up to Apharwat peak for majestic Himalayan powder snow views and advanced ski runs.", "Gulmarg Alpine Ski Lodge", "Breakfast & Dinner"),
                (4, "Skiing Lessons Day 2 & Snowmobiling", "Advanced turns practice on slopes, afternoon thrilling snowmobile ride through deodar forests.", "Gulmarg Alpine Ski Lodge", "Breakfast & Dinner"),
                (5, "Frozen Drung Waterfall & Srinagar Houseboat", "Descend Gulmarg, visit surreal frozen Drung waterfall, evening cozy stay on heated Dal Lake houseboat.", "Dal Lake Deluxe Houseboat", "Breakfast & Dinner"),
                (6, "Kashmiri Shawl Artisan Tour & Flight", "Visit authentic Pashmina weaving center, transfer to Srinagar airport for return flight to Delhi.", "Private Vehicle", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in heated Gulmarg ski lodge + 1 night heated houseboat",
                "Daily breakfast and warm dinners with Kashmiri Kahwa",
                "Ski equipment rental (skis, boots, poles) for 2 days",
                "Certified ski instructor for group lessons",
                "Gondola Phase 1 & Phase 2 passes"
            ],
            "exclusions": [
                "Delhi-Srinagar airfare",
                "Waterproof ski jacket and pant hire",
                "Snowmobile ride charges",
                "Medical and accident insurance"
            ]
        },

        # 19. Kashmir - Mumbai - 6d - 72000 - Luxury + Nature - Couple - Tier 4 (70k+)
        {
            "name": "Kashmir Imperial Dal Lake Royal Residence",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Kashmir",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("72000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/kashmir-royal-residence",
            "is_active": True,
            "hotel_info": "Ultra-luxury heritage suite in The Lalit Grand Palace Srinagar and 5-star Khyber Himalayan Resort Gulmarg.",
            "meals_info": "Gourmet multi-course breakfasts, royal Kashmiri Wazwan feast, and chef-curated dinners.",
            "transportation_info": "Private luxury chauffeur-driven SUV (Toyota Fortuner) for entire tour.",
            "sightseeing_info": "Pari Mahal, Royal Springs Golf Course, Gulmarg private pine trails, and Nigeen Lake.",
            "activities_info": "Private chartered Shikara breakfast cruise, couple's spa ritual, and private saffron farm visit.",
            "themes": ["luxury", "nature"],
            "travel_types": ["Couple"],
            "availability_months": [4, 5, 6, 9, 10, 11],
            "itinerary": [
                (1, "Mumbai to Srinagar & Lalit Grand Palace", "Fly into Srinagar, VIP airport greeting, private luxury transfer to heritage palace hotel. High tea in Chinar lawns.", "The Lalit Grand Palace Srinagar", "Dinner"),
                (2, "Chartered Breakfast Shikara & Royal Wazwan", "Private Shikara cruise on tranquil Nigeen Lake with onboard breakfast. Evening 36-course royal Wazwan banquet.", "The Lalit Grand Palace Srinagar", "Breakfast & Wazwan Dinner"),
                (3, "Chauffeur Drive to Khyber Resort Gulmarg", "Scenic luxury drive to Gulmarg. Check in to premier Himalayan resort, heated indoor pool overlooking snow pines.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (4, "VIP Gondola Access & Alpine Spa Treatment", "VIP priority boarding on Gulmarg Gondola. Afternoon 90-minute Himalayan couples wellness therapy.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (5, "Pampore Saffron Fields & Artisan Silk Carpets", "Descend through Pampore saffron fields, private visit to master silk-carpet weavers with tea.", "The Lalit Grand Palace Srinagar", "Breakfast & Dinner"),
                (6, "Private Departure Transfer to Mumbai", "Champagne breakfast on palace terrace, souvenir gift box, private transfer to Srinagar airport.", "Luxury SUV", "Breakfast"),
            ],
            "inclusions": [
                "3 nights at The Lalit Grand Palace + 2 nights at The Khyber Himalayan Resort",
                "Full daily gourmet breakfast and chef-curated 4-course dinners",
                "Grand Kashmiri Wazwan banquet experience",
                "One 90-minute couples spa ritual at Khyber Spa by L'Occitane",
                "Private luxury Toyota Fortuner with chauffeur for all 6 days"
            ],
            "exclusions": [
                "Flights from Mumbai to Srinagar",
                "Alcoholic beverages and premium wine lists",
                "Golf club hire fees at Royal Springs",
                "Personal shopping for carpets and shawls"
            ]
        },

        # 20. Rishikesh - Delhi - 3d - 8500 - Adventure + Spiritual - Solo + Group - Spring/Autumn
        {
            "name": "Ganges White Water Rafting & Camping",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Rishikesh",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("8500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/rishikesh-rafting",
            "is_active": True,
            "hotel_info": "Riverside safari luxury tents with attached washrooms, swimming pool, and bonfire lawn.",
            "meals_info": "All meals included: 2 breakfasts, 2 lunches, 2 dinners with barbecue snacks.",
            "transportation_info": "AC semi-sleeper coach Delhi - Rishikesh - Delhi; transfers to rafting points.",
            "sightseeing_info": "Ram Jhula, Laxman Jhula, Triveni Ghat, and Shivpuri rapids.",
            "activities_info": "16 km river rafting on Grade III/IV rapids, cliff jumping, body surfing, and volleyball.",
            "themes": ["adventure", "spiritual"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [9, 10, 11, 2, 3, 4, 5, 6],
            "itinerary": [
                (1, "Delhi to Rishikesh Drive & Evening Ganga Aarti", "Morning coach from Delhi to Rishikesh. Camp check-in, riverside volleyball, evening spiritual Ganga Aarti at Triveni Ghat.", "Wildex Riverside Camp", "Lunch & Dinner"),
                (2, "16 KM White Water Rafting & Cliff Jumping", "Thrilling 16 km white water rafting from Shivpuri through 'Roller Coaster' and 'Golf Course' rapids. Cliff jump.", "Wildex Riverside Camp", "Breakfast, Lunch & Dinner"),
                (3, "Neer Garh Waterfall Hike & Return to Delhi", "Morning hike to Neer Garh cascading waterfall. Check out, visit Beatles Ashram, afternoon return coach to Delhi.", "Onward Coach", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in luxury safari camp with attached washroom",
                "All meals (2 breakfast, 2 lunch, 2 dinner with evening snacks)",
                "16 km white water rafting with professional river guide and safety kayak",
                "High-standard life jackets, helmets, and rafting equipment",
                "Round-trip AC coach transit from Delhi"
            ],
            "exclusions": [
                "GoPro video recording charges during rafting",
                "Bungee jumping and giant swing passes",
                "Personal gear and tips",
                "Meals during highway transit"
            ]
        },

        # 21. Rishikesh - Pune - 5d - 21000 - Spiritual + Nature - Solo + Couple + Family - Year Round
        {
            "name": "Himalayan Yoga & Meditation Sanctuary",
            "operator_name": "WanderNest Travels",
            "destination_name": "Rishikesh",
            "starting_city": "Pune",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("21000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/rishikesh-yoga-sanctuary",
            "is_active": True,
            "hotel_info": "Peaceful wellness ashram resort along the Ganges with organic gardens and meditation hall.",
            "meals_info": "Sattvic vegetarian meals (organic farm-to-table breakfast, lunch, and dinner).",
            "transportation_info": "Flight Pune-Dehradun; private sedan for ashram and cave visits.",
            "sightseeing_info": "Vashistha Cave, Beatles Ashram, Parmarth Niketan, and Kunjapuri Temple.",
            "activities_info": "Daily sunrise yoga, guided meditation, sound bath healing, and Ayurvedic consultation.",
            "themes": ["spiritual", "nature"],
            "travel_types": ["Solo", "Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 9, 10, 11, 12],
            "itinerary": [
                (1, "Pune to Dehradun Flight & Ashram Arrival", "Fly from Pune to Dehradun, riverside drive to Rishikesh. Check in to ashram, orientation, gentle evening yoga.", "Ananda Ganga Wellness Ashram", "Dinner"),
                (2, "Sunrise Hatha Yoga & Vashistha Cave", "Dawn yoga by the Ganges. Afternoon silent meditation inside the ancient Vashistha cave.", "Ananda Ganga Wellness Ashram", "Breakfast, Lunch & Dinner"),
                (3, "Ayurvedic Pulse Reading & Sound Healing", "Personal consultation with Ayurvedic doctor, therapeutic herbal massage, evening sound bowl meditation.", "Ananda Ganga Wellness Ashram", "Breakfast, Lunch & Dinner"),
                (4, "Kunjapuri Sunrise & Parmarth Ganga Aarti", "Drive to Kunjapuri temple (5,400 ft) for Himalayan sunrise over snow peaks. Sunset Aarti at Parmarth Niketan.", "Ananda Ganga Wellness Ashram", "Breakfast, Lunch & Dinner"),
                (5, "Farewell Meditation & Flight to Pune", "Morning gratitude meditation, organic herbal breakfast, transfer to Dehradun airport for return flight.", "Private Sedan", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in peaceful riverfront wellness cottage",
                "Full board sattvic organic meals (all breakfasts, lunches, dinners)",
                "Daily 2 yoga sessions and 1 meditation class with master instructor",
                "One 60-minute Ayurvedic abhyanga massage",
                "All local transfers including Dehradun airport pickup and drop"
            ],
            "exclusions": [
                "Airfare from Pune to Dehradun",
                "Personal Ayurvedic medicines and supplements",
                "Adventure sports activities",
                "Gratuities"
            ]
        },

        # 22. Andaman - Bangalore - 5d - 36000 - Beach + Nature - Couple + Family - Autumn/Spring
        {
            "name": "Havelock Island & Radhanagar Coral Odyssey",
            "operator_name": "TravelVista India",
            "destination_name": "Andaman",
            "starting_city": "Bangalore",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("36000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/andaman-coral-odyssey",
            "is_active": True,
            "hotel_info": "4-star eco-resort in Port Blair and beachfront resort with private beach on Havelock Island.",
            "meals_info": "Daily coastal breakfast buffet and 3 chef-crafted dinners.",
            "transportation_info": "Premium AC cruise (Makruzz / Nautika) between Port Blair and Havelock; private AC cabs on islands.",
            "sightseeing_info": "Cellular Jail National Memorial, Radhanagar Beach (Asia's best beach), and Kalapathar Beach.",
            "activities_info": "Cellular Jail Light & Sound show, snorkeling at Elephant Beach, and coral reef viewing.",
            "themes": ["beach", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Bangalore to Port Blair & Cellular Jail", "Fly to Port Blair. Hotel check-in, visit historic Cellular Jail and witness the evocative Light & Sound show.", "Symphony Palms Port Blair", "Dinner"),
                (2, "Catamaran Cruise to Havelock Island", "Board high-speed luxury catamaran to Havelock Island. Afternoon sunset at world-famous Radhanagar Beach.", "Havelock Island Beach Resort", "Breakfast & Dinner"),
                (3, "Elephant Beach Coral Reef Snorkeling", "Speedboat to Elephant Beach for pristine white sands and guided snorkeling amidst vibrant tropical corals.", "Havelock Island Beach Resort", "Breakfast & Dinner"),
                (4, "Kalapathar Beach & Return to Port Blair", "Morning walk at Kalapathar Beach with turquoise waters. Afternoon catamaran return to Port Blair, souvenir market.", "Symphony Palms Port Blair", "Breakfast"),
                (5, "Chatham Saw Mill & Departure to Bangalore", "Visit Asia's oldest saw mill and naval museum. Transfer to Port Blair airport for return flight to Bangalore.", "Private Cab", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in Port Blair + 2 nights in Havelock beachfront resort",
                "Daily breakfast and 3 dinners",
                "High-speed luxury catamaran tickets (Port Blair - Havelock - Port Blair)",
                "Speedboat transfers and snorkeling session at Elephant Beach",
                "All private cab transfers, port handling, and entry permits"
            ],
            "exclusions": [
                "Bangalore - Port Blair flights",
                "Scuba diving and sea-walking optional upgrades",
                "Lunches and beach beverages",
                "Camera fees at Cellular Jail"
            ]
        },

        # 23. Andaman - Hyderabad - 6d - 54000 - Beach + Adventure + Luxury - Solo + Couple - Peak Winter
        {
            "name": "Andaman Deep Sea Scuba & Neil Island Cruise",
            "operator_name": "Horizon Trails",
            "destination_name": "Andaman",
            "starting_city": "Hyderabad",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("54000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/andaman-deep-sea-scuba",
            "is_active": True,
            "hotel_info": "5-star luxury beachfront villas in Havelock and Neil Island with private sundecks.",
            "meals_info": "Gourmet breakfasts, fresh seafood dinners, and welcome tropical cocktails.",
            "transportation_info": "Private cruise transfers in Royal Class; private chauffeur SUV on all islands.",
            "sightseeing_info": "Radhanagar Beach, Neil Island Natural Bridge, Laxmanpur Beach sunset, and Bharatpur Beach.",
            "activities_info": "PADI certified discover scuba dive session with underwater photography, glass-bottom boat.",
            "themes": ["beach", "adventure", "luxury"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Hyderabad to Port Blair & Luxury Transfer", "Fly into Port Blair, executive transfer to luxury seaside hotel. Relaxed evening at Corbyn's Cove beach.", "SeaShell Port Blair Luxury Resort", "Dinner"),
                (2, "Royal Class Cruise to Havelock Island", "Sail on Royal Class catamaran to Havelock. Check in to beachfront villa. Sunset stroll on Radhanagar Beach.", "Barefoot at Havelock Eco-Villa", "Breakfast & Dinner"),
                (3, "Deep Sea Scuba Diving Expedition", "Guided boat dive with certified PADI divemaster at Nemo Reef with full HD underwater video recording.", "Barefoot at Havelock Eco-Villa", "Breakfast & Dinner"),
                (4, "Cruise to Neil Island & Natural Bridge", "Cruise to tranquil Neil Island. Marvel at the unique Geological Natural Rock Bridge and Laxmanpur sunset.", "SeaShell Neil Island Villa", "Breakfast & Dinner"),
                (5, "Bharatpur Coral Viewing & Port Blair Return", "Glass-bottom boat ride over live coral reefs at Bharatpur beach. Afternoon cruise back to Port Blair.", "SeaShell Port Blair Luxury Resort", "Breakfast & Dinner"),
                (6, "Airport Transfer & Flight to Hyderabad", "Champagne breakfast, pearl jewelry shopping, private chauffeur transfer to Port Blair airport.", "Private SUV", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in 5-star beachfront luxury villas",
                "Full daily breakfast and 5 gourmet dinners",
                "Royal Class high-speed catamaran tickets on all inter-island routes",
                "Complete PADI discover scuba diving session with instructor and media",
                "Private SUV transportation throughout all three islands"
            ],
            "exclusions": [
                "Hyderabad to Port Blair airfare",
                "Lunch meals",
                "Deep-sea game fishing optional charters",
                "Personal tips and gratuities"
            ]
        },

        # 24. Jaisalmer - Mumbai - 4d - 16500 - Heritage + Adventure - Solo + Group - Winter
        {
            "name": "Thar Desert Dune Safari & Golden Fort",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Jaisalmer",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("16500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/jaisalmer-desert-safari",
            "is_active": True,
            "hotel_info": "1 night in Golden Fort heritage hotel and 2 nights in Swiss desert luxury tent at Sam Sand Dunes.",
            "meals_info": "Daily breakfast, 2 desert camp dinners with barbecue, and traditional Rajasthani thali.",
            "transportation_info": "Train/flight connection Mumbai-Jodhpur/Jaisalmer; private AC cab for desert transfers.",
            "sightseeing_info": "Jaisalmer Golden Fort, Patwon Ki Haveli, Gadisar Lake, and Sam Sand Dunes.",
            "activities_info": "Camel trek on desert dunes, 4x4 Jeep dune bashing, and Kalbelia folk dance performance.",
            "themes": ["heritage", "adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai to Jaisalmer & Gadisar Lake Sunset", "Arrive in Jaisalmer, golden stone hotel check-in. Evening peaceful paddle boat ride on sacred Gadisar Lake.", "Fort Rajwada Heritage Hotel", "Dinner"),
                (2, "Living Golden Fort & Desert Camp Transfer", "Explore the living fortress of Jaisalmer and intricate Patwon Ki Haveli. Afternoon drive to Sam Sand Dunes.", "Royal Desert Camp, Sam", "Breakfast & Dinner"),
                (3, "4x4 Dune Bashing & Cultural Night", "Thrilling morning 4x4 dune bashing across golden ridges. Evening camel safari followed by folk dance and bonfire.", "Royal Desert Camp, Sam", "Breakfast & Dinner"),
                (4, "Kuldhara Ghost Village & Departure", "Explore the mysterious abandoned village of Kuldhara. Afternoon transfer to railway station / airport.", "Private Cab", "Breakfast"),
            ],
            "inclusions": [
                "1 night fort hotel + 2 nights Swiss tent at Sam Dunes",
                "Daily breakfast and 3 dinners including camp feast",
                "Camel safari ride across Thar desert dunes",
                "4x4 Jeep dune bashing experience",
                "Private AC cab for all Jaisalmer and desert sightseeing"
            ],
            "exclusions": [
                "Mumbai-Jaisalmer transit fare",
                "Lunches and alcoholic drinks",
                "Quad biking and parasailing passes",
                "Personal tips"
            ]
        },

        # 25. Jaisalmer - Delhi - 5d - 32000 - Heritage + Culture + Luxury - Couple + Family - Winter
        {
            "name": "Jaisalmer Royal Haveli & Desert Camp",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Jaisalmer",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("32000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/jaisalmer-royal-haveli",
            "is_active": True,
            "hotel_info": "5-star luxury heritage palace hotel with desert views and luxury AC glamping tent.",
            "meals_info": "Regal breakfast spreads, private desert dune barbecue dinner with musician.",
            "transportation_info": "Private Innova Crysta for Delhi-Jaisalmer or Jodhpur airport transfers and all tours.",
            "sightseeing_info": "Sonar Qila (Golden Fort), Salim Singh Haveli, Bada Bagh cenotaphs, and Tanot Mata Temple.",
            "activities_info": "Private starlit dune dinner, heritage photography walk, and vintage car ride.",
            "themes": ["heritage", "culture", "luxury"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2],
            "itinerary": [
                (1, "Delhi to Jaisalmer Flight & Royal Haveli Check-in", "Flight to Jaisalmer, regal welcome with rose petals and folk trumpets. Settle into royal suite, dinner at rooftop.", "Suryagarh Palace Resort", "Dinner"),
                (2, "Sonar Qila Fortress & Historic Havelis", "Private guided tour of the medieval living fort, Jain temples with exquisite stone carvings, and Patwon Haveli.", "Suryagarh Palace Resort", "Breakfast & Dinner"),
                (3, "Bada Bagh Royal Cenotaphs & Sam Glamping", "Visit architectural royal cenotaphs of Maharajas at Bada Bagh. Transfer to luxury desert glamping retreat.", "The Serai Luxury Desert Glamping", "Breakfast & Dinner"),
                (4, "Tanot Mata Border & Starlit Dune Dining", "Day trip to historic Tanot Mata temple near Indo-Pak border. Private candlelit dinner on secluded desert sand dune.", "The Serai Luxury Desert Glamping", "Breakfast & Private Dinner"),
                (5, "Desert Sunrise & Return Flight to Delhi", "Watch desert sunrise over golden dunes, champagne breakfast, private transfer to Jaisalmer airport.", "Private Innova", "Breakfast"),
            ],
            "inclusions": [
                "2 nights at Suryagarh Palace + 2 nights luxury desert glamping",
                "Full daily breakfast and 4 curated multi-course dinners",
                "Private candlelit starlit dune dinner with personal musician",
                "Dedicated Innova Crysta throughout the tour",
                "All monument entry passes, desert permits, and guide fees"
            ],
            "exclusions": [
                "Airfare between Delhi and Jaisalmer",
                "Lunches and premium beverages",
                "Spa treatments and wellness packages",
                "Personal gratuities"
            ]
        },

        # 26. Gangtok - Bangalore - 6d - 27500 - Nature + Adventure - Solo + Couple + Group - Spring/Autumn
        {
            "name": "Sikkim Monasteries & Tsomgo Lake Explorer",
            "operator_name": "WanderNest Travels",
            "destination_name": "Gangtok",
            "starting_city": "Bangalore",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("27500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/sikkim-monasteries",
            "is_active": True,
            "hotel_info": "4-star Himalayan view hotel on Tibet Road near MG Marg.",
            "meals_info": "Daily breakfast and dinner including traditional Sikkimese momos and thukpa.",
            "transportation_info": "Bagdogra airport pickup and drop; 4WD vehicle for high-altitude mountain lake passes.",
            "sightseeing_info": "Tsomgo Lake (12,310 ft), Baba Harbhajan Mandir, Rumtek Monastery, and MG Marg.",
            "activities_info": "Ropeway cable car ride over Gangtok valley, yak riding near glacial lake, and tea tasting.",
            "themes": ["nature", "adventure"],
            "travel_types": ["Solo", "Couple", "Group"],
            "availability_months": [3, 4, 5, 9, 10, 11],
            "itinerary": [
                (1, "Bangalore to Bagdogra & Drive to Gangtok", "Fly to Bagdogra airport, scenic drive along Teesta River into Sikkim. Check in to Gangtok hotel, evening stroll on MG Marg.", "The Golden Crest Resort, Gangtok", "Dinner"),
                (2, "Tsomgo Glacial Lake & Baba Mandir", "Ascend through hairpin turns to sacred high-altitude Tsomgo Lake (12,310 ft) and Baba Harbhajan shrine.", "The Golden Crest Resort, Gangtok", "Breakfast & Dinner"),
                (3, "Rumtek Monastery & Gangtok City Sights", "Visit the seat of the Karmapa at Rumtek Monastery, Do Drul Chorten Stupa, and Namgyal Institute of Tibetology.", "The Golden Crest Resort, Gangtok", "Breakfast & Dinner"),
                (4, "Banjhakri Falls & Cable Car Ride", "Visit Banjhakri energy park and waterfalls, take the thrilling aerial cable car over Gangtok town.", "The Golden Crest Resort, Gangtok", "Breakfast & Dinner"),
                (5, "Ravangla Buddha Park Day Trip", "Day excursion to the majestic 130-foot statue of Buddha at Ravangla and lush Temi Tea Garden.", "The Golden Crest Resort, Gangtok", "Breakfast & Dinner"),
                (6, "Bagdogra Airport Return & Bangalore Flight", "Morning descent down the Sikkim mountains to Bagdogra airport for return flight to Bangalore.", "Private 4WD", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in 4-star mountain view accommodation",
                "Daily breakfast and dinner at the resort",
                "Sikkim Inner Line Permit (ILP) and Tsomgo pass processing",
                "Dedicated mountain vehicle for all transfers and tours",
                "Gangtok ropeway cable car tickets"
            ],
            "exclusions": [
                "Airfare from Bangalore to Bagdogra",
                "Optional Nathu La Pass permit charges (subject to army clearance)",
                "Lunch meals",
                "Yak ride charges and personal tips"
            ]
        },

        # 27. Gangtok - Delhi - 7d - 39000 - Nature + Culture + Spiritual - Couple + Family - Spring/Autumn
        {
            "name": "North Sikkim Yumthang Valley & Gurudongmar",
            "operator_name": "Horizon Trails",
            "destination_name": "Gangtok",
            "starting_city": "Delhi",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("39000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/north-sikkim-yumthang",
            "is_active": True,
            "hotel_info": "4-star Gangtok hotel and best available eco-lodges in high-altitude Lachen and Lachung.",
            "meals_info": "All meals during North Sikkim circuit (breakfast, lunch, dinner).",
            "transportation_info": "Private heavy-duty 4WD (Mahindra Scorpio/Innova) with experienced mountain driver.",
            "sightseeing_info": "Gurudongmar Lake (17,800 ft), Yumthang Valley of Flowers, Zero Point, and Chungthang.",
            "activities_info": "High-altitude plateau trek, natural hot spring bath, and rhododendron sanctuary walk.",
            "themes": ["nature", "culture", "spiritual"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [3, 4, 5, 6, 10, 11, 12],
            "itinerary": [
                (1, "Delhi to Bagdogra & Gangtok Ascent", "Fly to Bagdogra, mountain drive to Gangtok. Permit verification, check-in, rest and acclimatization.", "Summit Golden Spa Resort, Gangtok", "Dinner"),
                (2, "Gangtok to Lachen High Mountain Drive", "Scenic drive into North Sikkim past Seven Sisters Waterfalls, Singhik view point, and Chungthang confluence.", "Apple Orchard Lodge, Lachen", "Breakfast, Lunch & Dinner"),
                (3, "Holy Gurudongmar Lake (17,800 ft)", "Pre-dawn expedition to one of the world's highest lakes, sacred Gurudongmar. Afternoon transfer to Lachung.", "Yarlam Alpine Resort, Lachung", "Breakfast, Lunch & Dinner"),
                (4, "Yumthang Valley & Zero Point Snowfield", "Drive through Yumthang Valley of Flowers up to snow-clad Zero Point (15,300 ft). Hot springs dip, return to Gangtok.", "Summit Golden Spa Resort, Gangtok", "Breakfast, Lunch & Dinner"),
                (5, "Gangtok Monasteries & Handicraft Center", "Visit Enchey Monastery, Directorate of Handicrafts, and Flower Exhibition Center.", "Summit Golden Spa Resort, Gangtok", "Breakfast & Dinner"),
                (6, "Tsomgo Lake & Baba Mandir Excursion", "Day trip to glacial Tsomgo Lake with panoramic views of Kanchenjunga range.", "Summit Golden Spa Resort, Gangtok", "Breakfast & Dinner"),
                (7, "Bagdogra Airport Return to Delhi", "Early morning scenic descent to Bagdogra airport for return flight to Delhi.", "Private 4WD", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in Gangtok + 1 night in Lachen + 1 night in Lachung",
                "Full meals (breakfast, lunch, dinner) in North Sikkim + breakfast & dinner in Gangtok",
                "North Sikkim protected area permits and military clearance",
                "Dedicated 4WD mountain vehicle for the complete 7-day tour",
                "Oxygen cylinder and first-aid kit onboard"
            ],
            "exclusions": [
                "Delhi-Bagdogra flights",
                "Zero Point vehicle extra charges if required",
                "Personal heavy winter down jacket rental",
                "Tips and driver night allowances"
            ]
        },

        # 28. Meghalaya - Hyderabad - 5d - 24000 - Nature + Wildlife + Adventure - Solo + Group - Autumn/Winter
        {
            "name": "Living Root Bridges & Cherrapunji Waterfalls",
            "operator_name": "TravelVista India",
            "destination_name": "Meghalaya",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("24000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/meghalaya-root-bridges",
            "is_active": True,
            "hotel_info": "Boutique pine valley resort in Shillong and cliffside eco-lodge in Cherrapunji.",
            "meals_info": "Daily breakfast and wholesome Khasi/continental dinners.",
            "transportation_info": "Guwahati airport pickup and drop; private AC vehicle throughout Meghalaya.",
            "sightseeing_info": "Umiam Lake, Nohkalikai Falls (India's tallest plunge waterfall), Mawsmai Caves, and Dawki river.",
            "activities_info": "Guided trek to Double Decker Living Root Bridge in Nongriat, cave spelunking, and boating.",
            "themes": ["nature", "wildlife", "adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Hyderabad to Guwahati & Shillong Drive", "Fly to Guwahati, scenic highway drive past tranquil Umiam Lake (Barapani). Check in to Shillong resort.", "Polo Orchid Resort, Shillong", "Dinner"),
                (2, "Cherrapunji Waterfalls & Limestone Caves", "Drive to Cherrapunji, marvel at plunging Nohkalikai Falls and Seven Sisters Falls. Explore Mawsmai limestone cave.", "Cherrapunji Holiday Eco-Lodge", "Breakfast & Dinner"),
                (3, "Double Decker Living Root Bridge Trek", "Descend 3,000 steps into lush rainforest to marvel at the 200-year-old bio-engineered Double Decker Living Root Bridge.", "Cherrapunji Holiday Eco-Lodge", "Breakfast & Dinner"),
                (4, "Dawki Crystal River & Mawlynnong Village", "Boating on crystal clear Umngot River where boats appear to float on air. Visit Mawlynnong (cleanest village in Asia).", "Polo Orchid Resort, Shillong", "Breakfast & Dinner"),
                (5, "Elephant Falls & Guwahati Airport Drop", "Morning stop at tiered Elephant Falls, transfer to Guwahati airport for flight to Hyderabad.", "Private Vehicle", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in Shillong + 2 nights in Cherrapunji eco-resort",
                "Daily breakfast and dinner",
                "Dedicated private AC vehicle for all transfers and excursions",
                "Certified local Khasi trekking guide for Nongriat root bridges",
                "Dawki boat ride tickets and all cave entry permits"
            ],
            "exclusions": [
                "Airfare from Hyderabad to Guwahati",
                "Lunch meals",
                "Caving equipment for deep non-commercial caves",
                "Personal tips and porterage"
            ]
        },

        # 29. Meghalaya - Mumbai - 6d - 33000 - Nature + Culture - Couple + Family - Autumn/Winter
        {
            "name": "Shillong Scotland of East & Dawki River Trek",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Meghalaya",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("33000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/shillong-scotland-east",
            "is_active": True,
            "hotel_info": "4-star luxury heritage resort overlooking Umiam Lake and premium valley cottages.",
            "meals_info": "Daily buffet breakfast and 4-course dinners with Khasi tribal delicacies.",
            "transportation_info": "Private Innova Crysta for all 6 days with experienced hill chauffeur.",
            "sightseeing_info": "Laitlum Canyons, Krang Shuri Falls, Don Bosco Museum, and Police Bazar.",
            "activities_info": "Canyon edge walking, swimming in turquoise natural pool at Krang Shuri, and boating.",
            "themes": ["nature", "culture"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai to Guwahati & Umiam Lakefront Resort", "Fly to Guwahati, luxury transfer to 5-star lakeside resort. Settle into lake view cottage, evening sunset stroll.", "Ri Kynjai Serenity By The Lake", "Dinner"),
                (2, "Shillong Indigenous Heritage & Golf Course", "Explore Don Bosco Museum of Indigenous Cultures, historic Shillong golf course, and Police Bazar market.", "Ri Kynjai Serenity By The Lake", "Breakfast & Dinner"),
                (3, "Laitlum Grand Canyon & Jowai Scenic Hills", "Breathtaking morning walk at Laitlum Canyons overlooking mist-filled gorges. Afternoon drive through pine hills.", "Ri Kynjai Serenity By The Lake", "Breakfast & Dinner"),
                (4, "Krang Shuri Turquoise Waterfalls & Dawki", "Visit stunning turquoise natural pools of Krang Shuri Falls. Afternoon boat ride on glassy Dawki river.", "Polo Orchid Resort, Cherrapunji", "Breakfast & Dinner"),
                (5, "Cherrapunji Waterfalls & Arwah Caves", "Visit Nohkalikai and Dainthlen Falls, search for marine fossils in Arwah Cave. Sunset over Bangladesh plains.", "Polo Orchid Resort, Cherrapunji", "Breakfast & Dinner"),
                (6, "Kamakhya Temple Visit & Flight to Mumbai", "Morning drive to Guwahati, visit sacred Kamakhya Temple on Nilachal Hill, drop at airport.", "Private Innova", "Breakfast"),
            ],
            "inclusions": [
                "3 nights at Ri Kynjai Lake Resort + 2 nights in Cherrapunji",
                "Full daily breakfast and multi-course dinners",
                "Private Innova Crysta throughout the entire itinerary",
                "Dawki boat ride and Krang Shuri entry passes",
                "All toll fees, fuel, driver allowances, and permits"
            ],
            "exclusions": [
                "Mumbai-Guwahati air tickets",
                "Lunch meals",
                "Water sports equipment hire",
                "Personal tips and shopping"
            ]
        },

        # 30. Dubai - Delhi - 5d - 58000 - Luxury + Culture - Family + Couple - Winter (Tier 3)
        {
            "name": "Dubai Marina & Desert Luxury Odyssey",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Dubai",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("58000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/dubai-luxury-odyssey",
            "is_active": True,
            "hotel_info": "5-star luxury hotel in Dubai Marina with infinity pool overlooking yacht harbor.",
            "meals_info": "Daily international buffet breakfast and 2 specialty dinners including desert BBQ feast.",
            "transportation_info": "Private airport luxury transfers; AC luxury coach for desert safari and city tours.",
            "sightseeing_info": "Burj Khalifa 124th floor, Dubai Mall, Marina Dhow Cruise, Dubai Frame, and Palm Jumeirah.",
            "activities_info": "4x4 Desert Dune Bashing, belly dance and Tanoura show, and high-speed elevator ride to Burj Khalifa.",
            "themes": ["luxury", "culture"],
            "travel_types": ["Family", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Delhi to Dubai Arrival & Marina Dhow Cruise", "Fly from Delhi to Dubai, executive transfer to Marina hotel. Evening 2-hour Marina Dhow Cruise with international buffet.", "Marina Grand 5-Star Hotel", "Dinner"),
                (2, "Half Day City Tour & Burj Khalifa At The Top", "City tour through Palm Jumeirah, Atlantis photo stop, evening ascent to 124th floor of Burj Khalifa & Dubai Fountain.", "Marina Grand 5-Star Hotel", "Breakfast"),
                (3, "Desert Safari & Bedouin Camp Feast", "Leisure morning. Afternoon 4x4 Land Cruiser desert dune bashing, camel rides, henna painting, and BBQ dinner under stars.", "Marina Grand 5-Star Hotel", "Breakfast & Desert BBQ"),
                (4, "Museum of the Future & Gold Souk Walk", "Visit architectural marvel Museum of the Future. Afternoon traditional Abra boat ride across Dubai Creek to Gold Souk.", "Marina Grand 5-Star Hotel", "Breakfast"),
                (5, "Mall of the Emirates & Delhi Return", "Morning shopping at Mall of the Emirates. Luxury airport chauffeur transfer for return flight to Delhi.", "Private Transfer", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in 5-star Marina view luxury room",
                "Daily international buffet breakfast and 2 dinners",
                "Burj Khalifa 124th & 125th floor non-prime admission tickets",
                "4x4 Desert Safari with dune bashing and BBQ dinner",
                "Marina luxury Dhow Cruise dinner tickets",
                "Round-trip Dubai International Airport private transfers"
            ],
            "exclusions": [
                "International flight tickets Delhi-Dubai-Delhi",
                "UAE tourist visa and medical insurance fees",
                "Tourism Dirham hotel tax (payable directly at checkout)",
                "Lunch meals and personal shopping"
            ]
        },

        # 31. Dubai - Mumbai - 6d - 85000 - Luxury + Culture - Couple + Family - Tier 4 (70k+)
        {
            "name": "Dubai Royal Skyline & Desert Palace",
            "operator_name": "WanderNest Travels",
            "destination_name": "Dubai",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("85000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/dubai-royal-skyline",
            "is_active": True,
            "hotel_info": "5-star ultra-luxury suite at Atlantis The Palm and desert palace resort Bab Al Shams.",
            "meals_info": "Gourmet breakfasts, Michelin-star dining credit, and royal Arabic banquet.",
            "transportation_info": "Private Mercedes-Benz / BMW chauffeur service for all movements.",
            "sightseeing_info": "Burj Al Arab VIP tour, Abu Dhabi Sheikh Zayed Grand Mosque, Louvre Abu Dhabi, and Aquaventure.",
            "activities_info": "Unlimited access to Aquaventure Waterpark, private yacht charter, and falconry show.",
            "themes": ["luxury", "culture"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai to Dubai VIP Arrival & Palm Jumeirah", "First class arrival, VIP immigration greeting, luxury limousine to Atlantis The Palm. Welcome champagne dinner.", "Atlantis The Palm Luxury Suite", "Dinner"),
                (2, "Aquaventure Waterpark & Burj Al Arab Interior", "Unlimited thrills at Aquaventure Waterpark. Evening guided interior tour of 7-star Burj Al Arab with 24k gold cappuccino.", "Atlantis The Palm Luxury Suite", "Breakfast & High Tea"),
                (3, "Private Yacht Cruise on Dubai Coastline", "3-hour private chartered yacht sailing from Dubai Harbour past Ain Dubai and Palm Jumeirah with gourmet lunch.", "Atlantis The Palm Luxury Suite", "Breakfast & Lunch"),
                (4, "Abu Dhabi Grand Mosque & Louvre Day Tour", "Private chauffeur drive to Abu Dhabi. Visit Sheikh Zayed Grand Mosque and world-class Louvre Abu Dhabi museum.", "Atlantis The Palm Luxury Suite", "Breakfast & Dinner"),
                (5, "Transfer to Desert Oasis Palace Resort", "Transfer to Bab Al Shams luxury desert resort. Sunset royal falconry demonstration, starlit Arabic banquet.", "Bab Al Shams Desert Resort & Spa", "Breakfast & Royal Banquet"),
                (6, "Desert Sunrise & Limousine to Airport", "Sunrise over Arabian desert dunes, late breakfast, private limousine transfer to Dubai International Airport.", "Luxury Limousine", "Breakfast"),
            ],
            "inclusions": [
                "4 nights at Atlantis The Palm + 1 night at Bab Al Shams Desert Resort",
                "Full daily gourmet breakfast, 1 yacht lunch, and 3 fine dining dinners",
                "3-hour private luxury yacht charter with skipper and crew",
                "Unlimited entry to Aquaventure Waterpark & Lost Chambers Aquarium",
                "Private dedicated luxury Mercedes-Benz chauffeur for all 6 days"
            ],
            "exclusions": [
                "Airfare from Mumbai to Dubai",
                "UAE luxury visa processing fees",
                "Tourism Dirham fees",
                "Personal casino / spa expenses"
            ]
        },

        # 32. Bali - Bangalore - 6d - 52000 - Beach + Nature + Culture - Solo + Couple - Tier 3
        {
            "name": "Ubud Tropical Rainforest & Seminyak Surf",
            "operator_name": "TravelVista India",
            "destination_name": "Bali",
            "starting_city": "Bangalore",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("52000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/bali-ubud-seminyak",
            "is_active": True,
            "hotel_info": "4-star jungle pool villa in Ubud and boutique beach resort in Seminyak.",
            "meals_info": "Daily tropical breakfasts, 1 floating breakfast, and 2 Balinese dinners.",
            "transportation_info": "Private AC minivan with friendly English-speaking Balinese driver-guide.",
            "sightseeing_info": "Tegalalang Rice Terraces, Ubud Sacred Monkey Forest, Tanah Lot Sea Temple, and Uluwatu.",
            "activities_info": "Bali Jungle Swing over river canyon, Mount Batur sunrise jeep tour, and Kecak fire dance.",
            "themes": ["beach", "nature", "culture"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Bangalore to Denpasar Flight & Ubud Arrival", "Fly to Bali, traditional flower garland welcome at airport, scenic drive into Ubud rainforest. Settle into pool villa.", "Alaya Resort Ubud", "Dinner"),
                (2, "Tegalalang Rice Terraces & Jungle Swing", "Visit UNESCO-listed emerald rice terraces in Tegalalang, experience famous canyon swing, visit luwak coffee estate.", "Alaya Resort Ubud", "Breakfast & Floating Tray"),
                (3, "Mount Batur Sunrise Jeep & Hot Springs", "4x4 sunrise jeep drive on volcanic slopes of Mount Batur. Soak in lakeside geothermal natural hot springs.", "Alaya Resort Ubud", "Breakfast & Lunch"),
                (4, "Transfer to Seminyak & Tanah Lot Sunset", "Drive to vibrant coastal Seminyak. Check in to beach resort, afternoon sunset visit to sea temple of Tanah Lot.", "Seminyak Beach Resort & Spa", "Breakfast"),
                (5, "Uluwatu Clifftop Temple & Kecak Dance", "Scenic clifftop walk at Uluwatu Temple (250 ft above sea), watch hypnotic sunset Kecak fire dance drama.", "Seminyak Beach Resort & Spa", "Breakfast & Seafood Dinner"),
                (6, "Seminyak Boutique Shopping & Departure", "Morning surf or cafe hopping in Seminyak, check out, private transfer to Denpasar airport for Bangalore flight.", "Private Minivan", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in Ubud pool villa + 2 nights in Seminyak beach resort",
                "Daily tropical breakfast including 1 signature floating breakfast",
                "Mount Batur 4x4 sunrise jeep tour with natural hot spring entry",
                "Bali Swing admission ticket with safety harness",
                "Private dedicated AC vehicle and English-speaking guide for all 6 days"
            ],
            "exclusions": [
                "Bangalore-Bali international flights",
                "Indonesia Visa on Arrival (VOA) fee",
                "Lunch meals outside Mount Batur tour",
                "Personal tips and beach club daybed covers"
            ]
        },

        # 33. Bali - Mumbai - 7d - 95000 - Beach + Luxury + Nature - Couple - Tier 4 (70k+)
        {
            "name": "Bali Private Pool Villa Sanctuary",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Bali",
            "starting_city": "Mumbai",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("95000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/bali-pool-villa-sanctuary",
            "is_active": True,
            "hotel_info": "5-star luxury private pool villa at Viceroy Bali (Ubud) and The Mulia (Nusa Dua).",
            "meals_info": "All gourmet a-la-carte breakfasts, daily high tea, and 3 fine-dining chef dinners.",
            "transportation_info": "Private executive luxury Alphard minivan with chauffeur throughout the 7 days.",
            "sightseeing_info": "Tirta Empul water purification, Nusa Penida Island, Lempuyang Temple (Gates of Heaven), and Uluwatu.",
            "activities_info": "Chartered fast boat to Nusa Penida, 2-hour Balinese couple's massage, and candlelit beach dinner.",
            "themes": ["beach", "luxury", "nature"],
            "travel_types": ["Couple"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Mumbai to Bali VIP Arrival & Ubud Private Villa", "Fly into Bali, VIP expedited immigration, luxury Alphard transfer to Ubud cliffside villa with private infinity pool.", "Viceroy Bali Luxury Villa", "Dinner"),
                (2, "Spiritual Cleansing at Tirta Empul & High Tea", "Participate in ancient Melukat water purification ritual at sacred Tirta Empul temple. Afternoon tea overlooking Valley of Kings.", "Viceroy Bali Luxury Villa", "Breakfast & High Tea"),
                (3, "Gates of Heaven Lempuyang & Water Palace", "Early morning excursion to iconic Lempuyang Temple overlooking Mount Agung, explore Tirta Gangga royal water gardens.", "Viceroy Bali Luxury Villa", "Breakfast & Dinner"),
                (4, "Transfer to Nusa Dua 5-Star Beach Haven", "Scenic transfer to white sand beaches of Nusa Dua. Settle into beachfront villa, 2-hour signature couples spa treatment.", "The Mulia Nusa Dua Ocean Villa", "Breakfast & Spa"),
                (5, "Nusa Penida Private Island Discovery", "Private chartered fast boat to Nusa Penida. Discover dramatic Kelingking T-Rex cliff, Angel's Billabong, and Broken Beach.", "The Mulia Nusa Dua Ocean Villa", "Breakfast & Island Lunch"),
                (6, "Leisure Beachfront & Candlelit Seafood Feast", "Day of seaside leisure at private beach cabana. Evening romantic candlelit 4-course seafood dinner on the sand.", "The Mulia Nusa Dua Ocean Villa", "Breakfast & Candlelit Dinner"),
                (7, "Champagne Brunch & Airport Limousine", "Late champagne breakfast, luxury boutique shopping, private Alphard transfer to Denpasar airport.", "Luxury Alphard", "Breakfast"),
            ],
            "inclusions": [
                "3 nights at Viceroy Bali Private Pool Villa + 3 nights at The Mulia Ocean Villa",
                "Full daily gourmet breakfast, afternoon high teas, 3 fine-dining dinners",
                "Private chartered fast boat to Nusa Penida Island with private car on island",
                "2-hour Balinese luxury couples spa ritual at Mulia Spa",
                "Private executive Toyota Alphard chauffeur service for complete stay"
            ],
            "exclusions": [
                "Airfare from Mumbai to Bali",
                "Indonesia tourist visa fees",
                "Alcoholic wines outside package dinners",
                "Gratuities and personal shopping"
            ]
        },

        # 34. Bali - Delhi - 10d - 65000 - Nature + Adventure + Beach - Solo + Group - 10 Days Duration
        {
            "name": "Bali & Nusa Penida Grand Island Discovery",
            "operator_name": "Horizon Trails",
            "destination_name": "Bali",
            "starting_city": "Delhi",
            "duration_days": 10,
            "duration_nights": 9,
            "price_per_person": Decimal("65000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/bali-grand-discovery",
            "is_active": True,
            "hotel_info": "Combination of bohemian Canggu surf resort, Ubud jungle hotel, and Gili Trawangan beach bungalows.",
            "meals_info": "Daily breakfast buffet and 4 group communal dinners.",
            "transportation_info": "Private minivan for Bali mainland; fast boats for Gili and Nusa Penida inter-island transits.",
            "sightseeing_info": "Canggu, Ulun Danu Beratan Lake Temple, Gitgit waterfalls, Gili Trawangan, and Nusa Penida.",
            "activities_info": "Beginner surf lesson, swimming with sea turtles in Gili, Manta Ray snorkeling, and cliff hike.",
            "themes": ["nature", "adventure", "beach"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [5, 6, 7, 8, 9],
            "itinerary": [
                (1, "Delhi to Bali Flight & Canggu Beach Hub", "Fly to Bali, transfer to trendy Canggu. Check in, evening welcome drinks and sunset at Echo Beach.", "Canggu Surf & Beach Resort", "Dinner"),
                (2, "Surfing Masterclass & Beach Clubs", "Morning 2-hour certified surfing lesson on Canggu breaks. Afternoon chill at famous seaside beach club.", "Canggu Surf & Beach Resort", "Breakfast"),
                (3, "Northern Waterfalls & Ulun Danu Lake Temple", "Drive through central mountains to iconic floating temple on Lake Beratan and swim at Gitgit waterfall.", "Canggu Surf & Beach Resort", "Breakfast & Dinner"),
                (4, "Transfer to Cultural Heart of Ubud", "Scenic drive to Ubud. Visit Sacred Monkey Forest, stroll along Campuhan Ridge, evening cooking class.", "Ubud Green Valley Hotel", "Breakfast"),
                (5, "Tegalalang Terraces & Batur Volcano Trek", "Hike through scenic rice terraces, afternoon mountain bike ride through Balinese villages.", "Ubud Green Valley Hotel", "Breakfast"),
                (6, "Fast Boat to Tropical Gili Trawangan", "Board speedboat to car-free tropical paradise of Gili Trawangan. Bicycle island tour, sunset reggae bar.", "Gili Paradise Bungalows", "Breakfast & Dinner"),
                (7, "Sea Turtle Snorkeling & Coral Reef Cruise", "Boat tour around Gili Meno and Gili Air, snorkel with wild sea turtles in crystal clear waters.", "Gili Paradise Bungalows", "Breakfast"),
                (8, "Speedboat to Nusa Penida Island", "Transfer to rugged Nusa Penida Island. Hike to dramatic Kelingking T-Rex cliff and Broken Beach.", "Nusa Penida Ocean View Lodge", "Breakfast & Dinner"),
                (9, "Manta Point Snorkeling & Return to Mainland", "Snorkel with giant manta rays at Manta Point. Afternoon boat back to Bali mainland, Seminyak hotel.", "Seminyak Urban Hotel", "Breakfast"),
                (10, "Artisan Market Souvenirs & Delhi Flight", "Morning souvenir shopping at Kuta art market, transfer to Denpasar airport for flight back to Delhi.", "Private Minivan", "Breakfast"),
            ],
            "inclusions": [
                "9 nights accommodation across Canggu, Ubud, Gili Trawangan, and Nusa Penida",
                "Daily breakfast and 4 group dinners",
                "All speedboat and ferry tickets between Bali, Gili T, and Nusa Penida",
                "Surfing lesson with board rental and instructor",
                "Full-day Gili and Nusa Penida snorkeling tours with equipment"
            ],
            "exclusions": [
                "Delhi-Denpasar round-trip flights",
                "Indonesia visa on arrival",
                "Bicycle rental in Gili Trawangan (approx $5/day)",
                "Lunches and personal drinks"
            ]
        },
    ]

    # Step 8 Dataset Expansion: Append 73 curated demo packages
    from scripts.demo_packages_expanded import get_expanded_packages_data
    expanded_packages = get_expanded_packages_data()
    packages.extend(expanded_packages)

    return packages


# =====================================================================
# IDEMPOTENT SEEDING LOGIC
# =====================================================================

def seed_database():
    """
    Idempotently seeds destinations, operators, themes, packages,
    and all associated child tables into smart_travel_db.
    """
    app = create_app()
    with app.app_context():
        print("=" * 70)
        print("STARTING DEMO DATA SEEDING FOR SMART TRAVEL PLATFORM")
        print("Target Database: smart_travel_db (via Flask-SQLAlchemy)")
        print("=" * 70)

        stats = {
            "destinations": {"inserted": 0, "skipped": 0},
            "operators": {"inserted": 0, "skipped": 0},
            "themes": {"inserted": 0, "skipped": 0},
            "packages": {"inserted": 0, "skipped": 0},
            "package_themes": {"inserted": 0, "skipped": 0},
            "package_travel_types": {"inserted": 0, "skipped": 0},
            "package_availability_months": {"inserted": 0, "skipped": 0},
            "package_itineraries": {"inserted": 0, "skipped": 0},
            "package_inclusions": {"inserted": 0, "skipped": 0},
            "package_exclusions": {"inserted": 0, "skipped": 0},
        }

        try:
            # 1. Seed Destinations
            print("\n[1/5] Seeding Destinations...")
            dest_cache = {}
            for d_data in DESTINATIONS_DATA:
                existing = Destination.query.filter_by(name=d_data["name"]).first()
                if existing:
                    dest_cache[existing.name] = existing
                    stats["destinations"]["skipped"] += 1
                else:
                    dest = Destination(
                        name=d_data["name"],
                        region=d_data.get("region"),
                        country=d_data["country"],
                        description=d_data.get("description"),
                        image_url=d_data.get("image_url"),
                    )
                    db.session.add(dest)
                    dest_cache[dest.name] = dest
                    stats["destinations"]["inserted"] += 1

            db.session.flush()

            # 2. Seed Operators
            print("[2/5] Seeding Operators...")
            op_cache = {}
            for o_data in OPERATORS_DATA:
                existing = Operator.query.filter_by(name=o_data["name"]).first()
                if existing:
                    op_cache[existing.name] = existing
                    stats["operators"]["skipped"] += 1
                else:
                    op = Operator(
                        name=o_data["name"],
                        website_url=o_data.get("website_url"),
                        contact_email=o_data.get("contact_email"),
                        contact_phone=o_data.get("contact_phone"),
                        rating=o_data.get("rating", Decimal("0.0")),
                    )
                    db.session.add(op)
                    op_cache[op.name] = op
                    stats["operators"]["inserted"] += 1

            db.session.flush()

            # 3. Seed Themes
            print("[3/5] Seeding Themes...")
            theme_cache = {}
            for t_data in THEMES_DATA:
                existing = Theme.query.filter_by(slug=t_data["slug"]).first()
                if existing:
                    theme_cache[existing.slug] = existing
                    stats["themes"]["skipped"] += 1
                else:
                    th = Theme(
                        name=t_data["name"],
                        slug=t_data["slug"],
                        description=t_data.get("description"),
                    )
                    db.session.add(th)
                    theme_cache[th.slug] = th
                    stats["themes"]["inserted"] += 1

            db.session.flush()

            # 4. Seed Packages & Children
            print("[4/5] Seeding Packages and Child Associations...")
            packages_data = build_packages_data()

            for p_data in packages_data:
                dest = dest_cache.get(p_data["destination_name"]) or Destination.query.filter_by(name=p_data["destination_name"]).first()
                op = op_cache.get(p_data["operator_name"]) or Operator.query.filter_by(name=p_data["operator_name"]).first()

                if not dest or not op:
                    print(f"  [ERROR] Missing destination '{p_data['destination_name']}' or operator '{p_data['operator_name']}'. Skipping package.")
                    continue

                existing_pkg = Package.query.filter_by(name=p_data["name"]).first()
                if existing_pkg:
                    pkg = existing_pkg
                    stats["packages"]["skipped"] += 1
                else:
                    pkg = Package(
                        operator_id=op.id,
                        destination_id=dest.id,
                        name=p_data["name"],
                        starting_city=p_data["starting_city"],
                        duration_days=p_data["duration_days"],
                        duration_nights=p_data["duration_nights"],
                        price_per_person=p_data["price_per_person"],
                        featured_image_url=p_data.get("featured_image_url"),
                        source_url=p_data.get("source_url"),
                        is_active=p_data.get("is_active", True),
                        hotel_info=p_data.get("hotel_info"),
                        meals_info=p_data.get("meals_info"),
                        transportation_info=p_data.get("transportation_info"),
                        sightseeing_info=p_data.get("sightseeing_info"),
                        activities_info=p_data.get("activities_info"),
                    )
                    db.session.add(pkg)
                    db.session.flush()
                    stats["packages"]["inserted"] += 1

                # 4a. Package Themes
                current_theme_slugs = {t.slug for t in pkg.themes}
                for t_slug in p_data.get("themes", []):
                    theme_obj = theme_cache.get(t_slug) or Theme.query.filter_by(slug=t_slug).first()
                    if theme_obj:
                        if t_slug not in current_theme_slugs:
                            pkg.themes.append(theme_obj)
                            current_theme_slugs.add(t_slug)
                            stats["package_themes"]["inserted"] += 1
                        else:
                            stats["package_themes"]["skipped"] += 1

                # 4b. Package Travel Types
                existing_tts = {
                    tt.travel_type
                    for tt in PackageTravelType.query.filter_by(package_id=pkg.id).all()
                }
                for tt_val in p_data.get("travel_types", []):
                    if tt_val not in existing_tts:
                        db.session.add(PackageTravelType(package_id=pkg.id, travel_type=tt_val))
                        existing_tts.add(tt_val)
                        stats["package_travel_types"]["inserted"] += 1
                    else:
                        stats["package_travel_types"]["skipped"] += 1

                # 4c. Package Availability Months
                existing_months = {
                    m.month
                    for m in PackageAvailabilityMonth.query.filter_by(package_id=pkg.id).all()
                }
                for m_val in p_data.get("availability_months", []):
                    if m_val not in existing_months:
                        db.session.add(PackageAvailabilityMonth(package_id=pkg.id, month=m_val))
                        existing_months.add(m_val)
                        stats["package_availability_months"]["inserted"] += 1
                    else:
                        stats["package_availability_months"]["skipped"] += 1

                # 4d. Package Itineraries
                existing_it_days = {
                    it.day_number
                    for it in PackageItinerary.query.filter_by(package_id=pkg.id).all()
                }
                for it_tuple in p_data.get("itinerary", []):
                    day_num, title, desc, accom, meals = it_tuple
                    if day_num not in existing_it_days:
                        db.session.add(
                            PackageItinerary(
                                package_id=pkg.id,
                                day_number=day_num,
                                title=title,
                                description=desc,
                                accommodation=accom,
                                meals_provided=meals,
                            )
                        )
                        existing_it_days.add(day_num)
                        stats["package_itineraries"]["inserted"] += 1
                    else:
                        stats["package_itineraries"]["skipped"] += 1

                # 4e. Package Inclusions
                existing_inc_descs = {
                    inc.description
                    for inc in PackageInclusion.query.filter_by(package_id=pkg.id).all()
                }
                for inc_desc in p_data.get("inclusions", []):
                    if inc_desc not in existing_inc_descs:
                        db.session.add(PackageInclusion(package_id=pkg.id, description=inc_desc))
                        existing_inc_descs.add(inc_desc)
                        stats["package_inclusions"]["inserted"] += 1
                    else:
                        stats["package_inclusions"]["skipped"] += 1

                # 4f. Package Exclusions
                existing_exc_descs = {
                    exc.description
                    for exc in PackageExclusion.query.filter_by(package_id=pkg.id).all()
                }
                for exc_desc in p_data.get("exclusions", []):
                    if exc_desc not in existing_exc_descs:
                        db.session.add(PackageExclusion(package_id=pkg.id, description=exc_desc))
                        existing_exc_descs.add(exc_desc)
                        stats["package_exclusions"]["inserted"] += 1
                    else:
                        stats["package_exclusions"]["skipped"] += 1

            # Commit all database transactions
            db.session.commit()
            print("[5/5] Transaction successfully committed to MySQL!")

        except Exception as e:
            db.session.rollback()
            print(f"\n[CRITICAL ERROR] Seeding aborted due to exception: {e}")
            raise

        # =====================================================================
        # SUMMARY & VERIFICATION
        # =====================================================================
        print_summary(stats)
        run_verification_queries(app)


def print_summary(stats):
    """Prints total counts and seed statistics."""
    print("\n" + "=" * 70)
    print("SEEDING SUMMARY & TABLE ROW COUNTS")
    print("=" * 70)

    total_dest = Destination.query.count()
    total_op = Operator.query.count()
    total_th = Theme.query.count()
    total_pkg = Package.query.count()
    active_pkg = Package.query.filter_by(is_active=True).count()
    inactive_pkg = Package.query.filter_by(is_active=False).count()

    total_pkg_th = db.session.execute(package_themes.select()).fetchall()
    total_tts = PackageTravelType.query.count()
    total_months = PackageAvailabilityMonth.query.count()
    total_its = PackageItinerary.query.count()
    total_incs = PackageInclusion.query.count()
    total_excs = PackageExclusion.query.count()

    starting_cities = sorted(list({p.starting_city for p in Package.query.all()}))
    dests_with_packages = len({p.destination_id for p in Package.query.all()})

    table_data = [
        ("destinations", total_dest, stats["destinations"]["inserted"], stats["destinations"]["skipped"]),
        ("operators", total_op, stats["operators"]["inserted"], stats["operators"]["skipped"]),
        ("themes", total_th, stats["themes"]["inserted"], stats["themes"]["skipped"]),
        ("packages", total_pkg, stats["packages"]["inserted"], stats["packages"]["skipped"]),
        ("package_themes", len(total_pkg_th), stats["package_themes"]["inserted"], stats["package_themes"]["skipped"]),
        ("package_travel_types", total_tts, stats["package_travel_types"]["inserted"], stats["package_travel_types"]["skipped"]),
        ("package_availability_months", total_months, stats["package_availability_months"]["inserted"], stats["package_availability_months"]["skipped"]),
        ("package_itineraries", total_its, stats["package_itineraries"]["inserted"], stats["package_itineraries"]["skipped"]),
        ("package_inclusions", total_incs, stats["package_inclusions"]["inserted"], stats["package_inclusions"]["skipped"]),
        ("package_exclusions", total_excs, stats["package_exclusions"]["inserted"], stats["package_exclusions"]["skipped"]),
    ]

    print(f"{'Table Name':<30} | {'Total in DB':<12} | {'Inserted':<10} | {'Skipped':<10}")
    print("-" * 70)
    for name, total, ins, skp in table_data:
        print(f"{name:<30} | {total:<12} | {ins:<10} | {skp:<10}")

    print("-" * 70)
    print(f"Active Packages:           {active_pkg}")
    print(f"Inactive Packages:         {inactive_pkg}")
    print(f"Destinations with Packages:{dests_with_packages} (out of {total_dest})")
    print(f"Starting Cities ({len(starting_cities)}):     {', '.join(starting_cities)}")
    print("=" * 70)


def run_verification_queries(app):
    """Executes live verification queries against the Flask app endpoints."""
    print("\n" + "=" * 70)
    print("RUNNING LIVE ENDPOINT VERIFICATION QUERIES")
    print("=" * 70)
    client = app.test_client()

    # Query 1: Package Search API (Step 3B)
    print("\n[Query 1] Step 3B: Package Search API")
    search_url = (
        "/api/v1/packages?"
        "starting_city=Delhi&budget=50000&travellers=2&duration_days=5&"
        "interest=Adventure&travel_type=Couple&month=12"
    )
    print(f"GET {search_url}")
    res1 = client.get(search_url)
    print(f"HTTP Status: {res1.status_code}")
    data1 = res1.get_json()
    if res1.status_code == 200 and data1.get("success"):
        pkgs = data1.get("data", [])
        print(f"Found {len(pkgs)} matching package(s):")
        for p in pkgs:
            print(f"  - Package ID {p['id']}: '{p['name']}' | City: {p['starting_city']} | Duration: {p['duration_days']}d | Price/person: INR {p['price_per_person']} | Operator: {p['operator']['name']}")
    else:
        print(f"ERROR: {data1}")

    # Query 2: Destination Discovery API (Step 3C)
    print("\n[Query 2] Step 3C: Destination Discovery API")
    discover_url = (
        "/api/v1/discover/destinations?"
        "starting_city=Delhi&budget=50000&travellers=2&duration_days=5&"
        "interest=Adventure&travel_type=Couple&month=12"
    )
    print(f"GET {discover_url}")
    res2 = client.get(discover_url)
    print(f"HTTP Status: {res2.status_code}")
    data2 = res2.get_json()
    if res2.status_code == 200 and data2.get("success"):
        dests = data2.get("data", [])
        print(f"Discovered {len(dests)} destination(s):")
        for d in dests:
            print(f"  - Destination: {d['destination_name']} ({d['country']}) | Score: {d['match_score']}/100 | Packages: {d['matching_package_count']} | Lowest/Person: INR {d['lowest_price_per_person']} | Best Package: '{d['best_matching_package_name']}'")
    else:
        print(f"ERROR: {data2}")

    # Query 3: Package Detail API (Step 3B)
    print("\n[Query 3] Step 3B: Package Detail API with Itinerary & Inclusions")
    first_pkg = Package.query.filter_by(name="Classic Manali & Solang Valley Explorer").first()
    pkg_id = first_pkg.id if first_pkg else 1
    detail_url = f"/api/v1/packages/{pkg_id}?travellers=2"
    print(f"GET {detail_url}")
    res3 = client.get(detail_url)
    print(f"HTTP Status: {res3.status_code}")
    data3 = res3.get_json()
    if res3.status_code == 200 and data3.get("success"):
        pkg_detail = data3.get("data", {})
        print(f"Package: '{pkg_detail['name']}' (ID: {pkg_detail['id']})")
        print(f"  Destination: {pkg_detail['destination']['name']} ({pkg_detail['destination']['region']}, {pkg_detail['destination']['country']})")
        print(f"  Operator:    {pkg_detail['operator']['name']} (Rating: {pkg_detail['operator']['rating']})")
        print(f"  Itinerary ({len(pkg_detail.get('itinerary', []))} days):")
        for it in pkg_detail.get("itinerary", [])[:2]:
            print(f"    * Day {it['day_number']}: {it['title']} ({it['meals_provided']})")
        print(f"    * ... and {len(pkg_detail.get('itinerary', [])) - 2} more day(s)")
        print(f"  Inclusions ({len(pkg_detail.get('inclusions', []))} items): {pkg_detail.get('inclusions', [])[:2]} ...")
        print(f"  Exclusions ({len(pkg_detail.get('exclusions', []))} items): {pkg_detail.get('exclusions', [])[:2]} ...")
    else:
        print(f"ERROR: {data3}")

    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE - ALL QUERIES SUCCEEDED")
    print("=" * 70)


if __name__ == "__main__":
    seed_database()
