"""
Expanded Demo Travel Packages Dataset for Step 8.
Contains 73 additional curated, realistic demo packages across 25 destinations,
10 demo operators, and varied travel themes, durations, starting cities, and price points.
"""

from decimal import Decimal


def get_expanded_packages_data():
    """Returns a list of 73 additional high-quality, fully detailed demo travel packages."""
    return [
        # =====================================================================
        # 1. UDAIPUR (Rajasthan, India) - 4 Packages
        # =====================================================================
        {
            "name": "Udaipur Romantic Lake Palace Sojourn",
            "operator_name": "WanderNest Travels",
            "destination_name": "Udaipur",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("45000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/udaipur-romantic-sojourn",
            "is_active": True,
            "hotel_info": "5-star luxury heritage haveli on the banks of Lake Pichola with private jharokha balconies.",
            "meals_info": "Daily royal breakfast and candlelit 4-course rooftop dinner overlooking the illuminated lake.",
            "transportation_info": "Private chauffeur-driven AC sedan for airport transfers and regional sightseeing.",
            "sightseeing_info": "City Palace, Jag Mandir island, Saheliyon-ki-Bari, Bagore Ki Haveli, and Monsoon Palace.",
            "activities_info": "Private sunset boat cruise on Lake Pichola, evening Dharohar folk dance show, and artisan shopping.",
            "themes": ["luxury", "romantic", "heritage"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Arrival & Sunset Boat Ride", "Arrive in Udaipur. Private check-in at lakeside heritage haveli. Sunset motorboat cruise around Jag Mandir.", "Fateh Garh Heritage Haveli", "Dinner"),
                (2, "City Palace & Royal Heritage Walk", "Morning guided tour of the sprawling City Palace complex and crystal gallery. Afternoon stroll in Saheliyon-ki-Bari.", "Fateh Garh Heritage Haveli", "Breakfast & Dinner"),
                (3, "Monsoon Palace & Cultural Folk Night", "Drive to Sajjangarh Monsoon Palace for panoramic Aravalli sunset. Evening Dharohar folk dance at Bagore Ki Haveli.", "Fateh Garh Heritage Haveli", "Breakfast & Dinner"),
                (4, "Artisan Bazaars & Departure", "Morning visit to local miniature painting studios and Hathi Pol markets. Afternoon transfer to airport.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in lake-facing heritage suite",
                "Daily champagne breakfast and candlelit lakeside dinners",
                "Private sunset charter boat on Lake Pichola",
                "All monument entry passes and royal guide services",
                "Airport transfers and private AC vehicle throughout"
            ],
            "exclusions": [
                "Domestic flights to and from Udaipur",
                "Camera and video permits at royal monuments",
                "Personal spa therapies and alcoholic beverages",
                "Travel insurance"
            ]
        },
        {
            "name": "Royal Mewar Forts & Lake Pichola Getaway",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Udaipur",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("16500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/udaipur-mewar-getaway",
            "is_active": True,
            "hotel_info": "4-star Rajasthani boutique resort near Lake Swaroop Sagar with traditional courtyards.",
            "meals_info": "Daily buffet breakfast and authentic Mewari thali dinners.",
            "transportation_info": "Roundtrip AC train/sleeper transit support and private local AC cab.",
            "sightseeing_info": "City Palace, Jagdish Temple, Fateh Sagar Lake, and Vintage Car Museum.",
            "activities_info": "Heritage walking tour, boat ride on Fateh Sagar, and traditional pottery workshop.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Family", "Couple"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Lake City Welcome & Jagdish Temple", "Arrival in Udaipur, transfer to boutique resort. Afternoon visit to historic 1651 AD Jagdish Temple and Gangaur Ghat.", "Radisson Swaroop Sagar Resort", "Dinner"),
                (2, "City Palace & Fateh Sagar Promenade", "Comprehensive guided walk through City Palace museums. Evening drive around scenic Fateh Sagar Lake.", "Radisson Swaroop Sagar Resort", "Breakfast & Dinner"),
                (3, "Vintage Cars & Bazaars", "Morning visit to the Vintage and Classic Car Collection followed by shopping at Bada Bazaar before departure.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in deluxe heritage courtyard room",
                "Breakfast and dinner on both days",
                "Dedicated private AC car for sightseeing",
                "Boat tickets for Fateh Sagar Lake",
                "All toll charges and driver allowances"
            ],
            "exclusions": [
                "Lunch meals and personal snack purchases",
                "Monument entry tickets and camera fees",
                "Personal tips and laundry charges",
                "Optional sound and light show tickets"
            ]
        },
        {
            "name": "Udaipur Weekend Culture & Heritage Trail",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Udaipur",
            "starting_city": "Pune",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("12000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/udaipur-weekend-trail",
            "is_active": True,
            "hotel_info": "Cozy heritage guesthouse in Old City with rooftop dining and Aravalli mountain views.",
            "meals_info": "Daily vegetarian breakfast and homestyle Rajasthani dinners.",
            "transportation_info": "AC Volvo sleeper Pune - Udaipur - Pune; auto/cab tours in town.",
            "sightseeing_info": "Bagore Ki Haveli, Lake Pichola Ghats, Shilpgram craft village, and Ahar Cenotaphs.",
            "activities_info": "Rural arts workshop at Shilpgram, ghat photography walk, and Rajasthani cooking class.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [10, 11, 12, 1, 2],
            "itinerary": [
                (1, "Overnight Arrival & Old City Ghats", "Arrival by morning Volvo. Check into heritage guesthouse. Evening exploration of Ambrai Ghat and evening tea.", "Amet Haveli Traditional Stay", "Dinner"),
                (2, "Shilpgram Craft Village & Folk Heritage", "Full day cultural immersion at Shilpgram rural arts complex. Evening puppet show at Bagore Ki Haveli.", "Amet Haveli Traditional Stay", "Breakfast & Dinner"),
                (3, "Ahar Cenotaphs & Pune Return", "Explore the royal memorial cenotaphs of Mewar maharanas at Ahar. Evening Volvo return journey.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in authentic Rajasthani heritage guesthouse",
                "Daily breakfast and traditional dinners",
                "Roundtrip AC Volvo sleeper bus tickets from Pune",
                "Guided photography and heritage walk",
                "Shilpgram entry and workshop passes"
            ],
            "exclusions": [
                "Meals during bus travel",
                "Monument entrance fees",
                "Personal expenses and porter charges",
                "Travel insurance"
            ]
        },
        {
            "name": "Grand Udaipur Luxury Heritage Palace Experience",
            "operator_name": "JourneyMint",
            "destination_name": "Udaipur",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("72000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/udaipur-grand-luxury",
            "is_active": True,
            "hotel_info": "5-star luxury palace property with marble courtyards, private royal butler, and infinity pool.",
            "meals_info": "Full royal breakfast buffet, afternoon high tea, and 5-course gourmet dining experiences.",
            "transportation_info": "Luxury BMW/Audi airport transfers and private luxury SUV on disposal throughout.",
            "sightseeing_info": "Private access City Palace chambers, Kumbhalgarh Fort day-trip, Ranakpur Jain Temples.",
            "activities_info": "Private champagne boat tour, royal astrology session, and couples Ayurvedic spa therapies.",
            "themes": ["luxury", "heritage", "romantic"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Royal Welcome & Lake Pichola Arrival", "VIP airport reception with luxury car transfer. Rose petal welcome at palace hotel. Evening champagne sunset boat cruise.", "The Leela Palace Lakefront", "Dinner"),
                (2, "Curated City Palace & Private Royal Quarters", "Exclusive guided walkthrough of City Palace with royal historian. Afternoon high tea on royal terrace.", "The Leela Palace Lakefront", "Breakfast & Dinner"),
                (3, "Kumbhalgarh Fort & Great Wall of India", "Day excursion to the UNESCO World Heritage Kumbhalgarh Fort and ancient Ranakpur marble temples.", "The Leela Palace Lakefront", "Breakfast & Dinner"),
                (4, "Ayurvedic Rejuvenation & Private Banquet", "Morning wellness massage session at signature spa. Evening private candlelit dinner under royal pavilions.", "The Leela Palace Lakefront", "Breakfast & Dinner"),
                (5, "Leisure Morning & VIP Departure", "Leisure morning by the lakeside infinity pool. Private luxury transfer to Udaipur airport for Hyderabad flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in ultra-luxury palace lake suite",
                "All gourmet meals, royal afternoon tea, and tasting menus",
                "Private chauffeured luxury vehicle at full disposal",
                "Private historian guide for all palace excursions",
                "Signature spa treatment session for each guest"
            ],
            "exclusions": [
                "Airfare tickets Hyderabad - Udaipur - Hyderabad",
                "Imported vintage champagne and cellar reserve wines",
                "Helicopter transfer add-on options",
                "Personal tips and gratuities"
            ]
        },

        # =====================================================================
        # 2. AMRITSAR (Punjab, India) - 3 Packages
        # =====================================================================
        {
            "name": "Golden Temple Spiritual & Heritage Immersion",
            "operator_name": "RoamRise Tours",
            "destination_name": "Amritsar",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("9500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/amritsar-spiritual-immersion",
            "is_active": True,
            "hotel_info": "Comfortable 3-star hotel within walking distance of the Golden Temple heritage walkway.",
            "meals_info": "Daily buffet breakfast and community Langar dining experience at the Golden Temple.",
            "transportation_info": "Vande Bharat / Shatabdi Express train Delhi - Amritsar - Delhi; private AC local car.",
            "sightseeing_info": "Sri Harmandir Sahib (Golden Temple), Jallianwala Bagh, Partition Museum, and Wagah Border.",
            "activities_info": "Early morning Palki Sahib ceremony, volunteer seva in community kitchen, and Wagah retreat ceremony.",
            "themes": ["spiritual", "culture", "heritage"],
            "travel_types": ["Solo", "Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Vande Bharat Arrival & Golden Temple Night View", "Board morning Vande Bharat express from Delhi. Check-in hotel. Evening visit to witness illuminated Golden Temple.", "Hotel Golden Sarovar Portico", "Dinner"),
                (2, "Partition Museum & Wagah Border Ceremony", "Morning visit to Jallianwala Bagh and Partition Museum. Afternoon drive to Indo-Pak Wagah Border for military retreat ceremony.", "Hotel Golden Sarovar Portico", "Breakfast & Dinner"),
                (3, "Palki Sahib Dawn & Delhi Return", "Dawn visit for Palki Sahib sacred procession. Morning shopping for Amritsari kulchas and juttis. Evening train return to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights accommodation near Golden Temple corridor",
                "Daily breakfast and welcome traditional dinner",
                "Roundtrip AC train tickets from Delhi",
                "Private vehicle for Wagah Border excursion and transfers",
                "Guided audio tour at Partition Museum"
            ],
            "exclusions": [
                "Lunch meals during sightseeing",
                "Personal tips to guides and drivers",
                "Souvenirs and personal shopping",
                "Special seating passes at Wagah (free seating included)"
            ]
        },
        {
            "name": "Amritsar Culinary & Wagah Border Discovery",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Amritsar",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("18000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/amritsar-culinary-wagah",
            "is_active": True,
            "hotel_info": "4-star boutique hotel located in the city center with authentic Punjabi specialty restaurant.",
            "meals_info": "Daily breakfast, Amritsari food tasting trail, and traditional dhaba dinners.",
            "transportation_info": "Private AC sedan for all airport transfers, city tours, and Wagah Border trip.",
            "sightseeing_info": "Golden Temple, Gobindgarh Fort, Ram Bagh gardens, and Katra Jaimal Singh bazaar.",
            "activities_info": "Guided street food trail tasting Amritsari kulcha, makki di roti, lassi, and jalebi; 7D show at Gobindgarh Fort.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Couple", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai Arrival & Street Food Trail", "Arrive in Amritsar from Mumbai. Transfer to hotel. Evening food walk through old town tasting world-famous Amritsari kulchas.", "Hyatt Regency Amritsar", "Dinner"),
                (2, "Golden Temple Immersion & Heritage Walk", "Comprehensive morning tour of Golden Temple and Jallianwala Bagh. Community meal (Langar). Evening at leisure on Heritage Street.", "Hyatt Regency Amritsar", "Breakfast & Dinner"),
                (3, "Gobindgarh Fort & Wagah Border", "Explore military history at Maharaja Ranjit Singh's Gobindgarh Fort. Afternoon drive to Wagah Border for ceremony.", "Hyatt Regency Amritsar", "Breakfast & Dinner"),
                (4, "Flea Markets & Return Flight", "Morning shopping for Phulkari dupattas and Punjabi papads. Transfer to Amritsar airport for flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in deluxe 4-star room",
                "Daily breakfast and curated culinary food trail",
                "Private dedicated cab for all 4 days",
                "Entry tickets to Gobindgarh Fort and cultural shows",
                "Airport pick-up and drop-off"
            ],
            "exclusions": [
                "Flights Mumbai - Amritsar - Mumbai",
                "Alcoholic beverages and personal expenses",
                "Porterage and laundry",
                "Travel insurance"
            ]
        },
        {
            "name": "Amritsar & Punjab Rural Cultural Odyssey",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Amritsar",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("24000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/punjab-rural-cultural-odyssey",
            "is_active": True,
            "hotel_info": "Eco-friendly heritage farmstay in rural Punjab surrounded by mustard fields and village orchards.",
            "meals_info": "Farm-fresh organic Punjabi meals cooked on traditional mud chulhas with fresh makhan and lassi.",
            "transportation_info": "Private AC Innova for all touring, farm transfers, and airport pickup.",
            "sightseeing_info": "Golden Temple, Sadda Pind cultural village, Wagah Border, and Pul Kanjari border post.",
            "activities_info": "Tractor rides through mustard fields, Bhangra dance workshop, pottery making, and farm walk.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Hyderabad Arrival & Farmstay Check-in", "Flight arrival in Amritsar. Welcome with fresh sugarcane juice and dhol beats at rural farmstay.", "Punjabiyat Rural Heritage Farmstay", "Dinner"),
                (2, "Golden Temple & Sadda Pind Village", "Morning visit to Golden Temple. Afternoon cultural immersion at Sadda Pind living museum with live folk arts.", "Punjabiyat Rural Heritage Farmstay", "Breakfast & Dinner"),
                (3, "Tractor Safari & Wagah Patriotic Border", "Morning tractor safari across mustard fields. Afternoon drive to Wagah border retreat ceremony.", "Punjabiyat Rural Heritage Farmstay", "Breakfast & Dinner"),
                (4, "Village Crafts & Return Journey", "Morning pottery and turban tying session. Check out and transfer to airport for Hyderabad flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in luxury heritage mud cottage at rural farmstay",
                "All meals included with farm-to-table organic preparations",
                "Private Innova vehicle throughout the itinerary",
                "All village activities, tractor rides, and cultural shows",
                "Dedicated tour host throughout"
            ],
            "exclusions": [
                "Airfare tickets Hyderabad - Amritsar - Hyderabad",
                "Personal shopping and souvenirs",
                "Extra laundry or personal orders",
                "Emergency medical costs"
            ]
        },

        # =====================================================================
        # 3. LEH (Ladakh, India) - 4 Packages
        # =====================================================================
        {
            "name": "High Passes of Ladakh & Pangong Lake Expedition",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Leh",
            "starting_city": "Delhi",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("34000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/leh-high-passes-expedition",
            "is_active": True,
            "hotel_info": "Comfortable 3-star boutique hotel in Leh town and lakeside deluxe tents at Pangong Tso.",
            "meals_info": "Buffet breakfast and dinner daily, tailored for high-altitude acclimatization.",
            "transportation_info": "Private non-AC Scorpio/Innova as per Ladakh transport union norms.",
            "sightseeing_info": "Shanti Stupa, Leh Palace, Khardung La (17,982 ft), Nubra Valley, Diskit Monastery, and Pangong Lake.",
            "activities_info": "Double-humped Bactrian camel ride at Hunder dunes, high pass crossing, and stargazing at Pangong.",
            "themes": ["adventure", "mountain", "nature"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [5, 6, 7, 8, 9],
            "itinerary": [
                (1, "Delhi Flight Arrival & Acclimatization", "Morning flight into Leh (11,500 ft). Complete rest day for altitude acclimatization. Evening stroll to Shanti Stupa.", "Grand Dragon Himalayan View Hotel", "Dinner"),
                (2, "Monasteries & Hall of Fame", "Visit Shey Palace, Thiksey Monastery, and the Indian Army Hall of Fame museum.", "Grand Dragon Himalayan View Hotel", "Breakfast & Dinner"),
                (3, "Khardung La to Nubra Valley", "Drive across Khardung La pass (17,982 ft) into the Nubra Valley. Sunset camel safari at Hunder sand dunes.", "Nubra Organic Retreat Camps", "Breakfast & Dinner"),
                (4, "Diskit Monastery & Shyok Route to Pangong", "Visit giant Maitreya Buddha statue at Diskit. Drive along the scenic Shyok river to Pangong Tso (14,270 ft).", "Pangong Starview Deluxe Camps", "Breakfast & Dinner"),
                (5, "Pangong Sunrise to Leh via Chang La", "Witness mesmerizing sunrise over Pangong Lake. Return to Leh driving across Chang La pass (17,590 ft).", "Grand Dragon Himalayan View Hotel", "Breakfast & Dinner"),
                (6, "Magnetic Hill & Sangam Confluence", "Day excursion to the confluence of Indus and Zanskar rivers, Magnetic Hill, and Gurudwara Pathar Sahib.", "Grand Dragon Himalayan View Hotel", "Breakfast & Dinner"),
                (7, "Leh Airport Farewell", "Morning transfer to Kushok Bakula Rimpochee Airport for onward flight back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "6 nights accommodation (4N Leh, 1N Nubra, 1N Pangong)",
                "Daily breakfast and dinner throughout",
                "Inner line permits and wildlife fees for restricted zones",
                "Dedicated private vehicle for all transfers and tours",
                "Emergency oxygen cylinder support in vehicle"
            ],
            "exclusions": [
                "Airfare Delhi - Leh - Delhi",
                "Camel safari charges at Hunder dunes",
                "Personal acclimatization medicines and snacks",
                "Any expenses caused by roadblocks or landslides"
            ]
        },
        {
            "name": "Ultimate Leh-Ladakh Mountain Safari",
            "operator_name": "Horizon Trails",
            "destination_name": "Leh",
            "starting_city": "Mumbai",
            "duration_days": 8,
            "duration_nights": 7,
            "price_per_person": Decimal("52000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/leh-mountain-safari",
            "is_active": True,
            "hotel_info": "4-star eco-luxury hotel in Leh, Swiss luxury tents in Nubra, and boutique cottages near Pangong.",
            "meals_info": "Nutritious mountain breakfast and dinners including Ladakhi thukpa and momo specialties.",
            "transportation_info": "Dedicated private AC Innova vehicle for all regional touring and high mountain passes.",
            "sightseeing_info": "Khardung La, Turtuk border village, Nubra Valley, Pangong Tso, Hemis Monastery, and Zanskar Sangam.",
            "activities_info": "Balti culture exploration in Turtuk, stargazing under clear skies, and river rafting at Sangam.",
            "themes": ["adventure", "nature", "mountain"],
            "travel_types": ["Couple", "Group"],
            "availability_months": [6, 7, 8, 9],
            "itinerary": [
                (1, "Mumbai to Leh Arrival & Acclimatization", "Early flight arrival. Rest day for oxygen acclimatization at hotel. Gentle evening visit to Leh Main Bazaar.", "Zen Ladakh Eco Resort", "Dinner"),
                (2, "Sham Valley & Indus Confluence", "Drive to Sangam (confluence of Indus and Zanskar rivers), Magnetic Hill, and Likir Monastery.", "Zen Ladakh Eco Resort", "Breakfast & Dinner"),
                (3, "Across Khardung La to Hunder Dunes", "Ascend through Khardung La pass down into the Nubra Valley. Double-humped camel safari at Hunder dunes.", "Hunder Sand Dunes Camp", "Breakfast & Dinner"),
                (4, "Turtuk Indo-Pak Border Village Day-Trip", "Excursion to the northernmost village of Turtuk, exploring unique Balti culture and apricot orchards.", "Hunder Sand Dunes Camp", "Breakfast & Dinner"),
                (5, "Shyok River Valley to Pangong Lake", "Traverse picturesque mountain gorges to reach the sparkling blue waters of Pangong Tso.", "Pangong Lake Luxury Cottages", "Breakfast & Dinner"),
                (6, "Chang La Pass to Leh & Thiksey Monastery", "Scenic return drive over Chang La pass. Visit majestic 12-storey Thiksey Monastery en route.", "Zen Ladakh Eco Resort", "Breakfast & Dinner"),
                (7, "Hemis Monastery & High Altitude Shopping", "Morning visit to Hemis Gompa, largest monastery in Ladakh. Afternoon at leisure for pashmina shopping.", "Zen Ladakh Eco Resort", "Breakfast & Dinner"),
                (8, "Leh Departure", "Check-out and transfer to Leh airport for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "7 nights deluxe accommodation across Ladakh circuit",
                "Breakfast and dinner daily",
                "Inner line permits, environmental fees, and wildlife passes",
                "Dedicated private SUV with experienced mountain driver",
                "Portable oxygen kit on board at all times"
            ],
            "exclusions": [
                "Flights Mumbai - Leh - Mumbai",
                "Rafting fees at Zanskar river",
                "Personal tips and driver gratuities",
                "Insurance coverage for high-altitude illness"
            ]
        },
        {
            "name": "Nubra Valley & Hemis Monasteries Trek",
            "operator_name": "WanderNest Travels",
            "destination_name": "Leh",
            "starting_city": "Pune",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("29000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/nubra-hemis-trek",
            "is_active": True,
            "hotel_info": "Boutique Tibetan-style guesthouse in Leh and riverside camping tents in Nubra.",
            "meals_info": "Daily healthy mountain breakfast and wholesome home-cooked Ladakhi dinners.",
            "transportation_info": "Shared mountain tempo traveler / private cab for group safety on mountain roads.",
            "sightseeing_info": "Shanti Stupa, Khardung La, Diskit Gompa, Panamik Hot Springs, and Hemis Monastery.",
            "activities_info": "Guided day hikes along mountain trails, hot sulfur spring dip, and evening monk chants.",
            "themes": ["adventure", "mountain", "culture"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [6, 7, 8, 9],
            "itinerary": [
                (1, "Pune to Leh & Rest Day", "Flight arrival via Delhi. Check into Tibetan guesthouse. Rest completely to adjust to 3,500m altitude.", "Singge Palace Guesthouse", "Dinner"),
                (2, "Leh Heritage & Monastic Culture", "Morning walk to Shanti Stupa and Leh Palace. Afternoon orientation briefing on mountain safety.", "Singge Palace Guesthouse", "Breakfast & Dinner"),
                (3, "Khardung La Crossing to Nubra", "Cross the famous Khardung La pass. Arrive in Nubra Valley and camp beside the river.", "Nubra River Camp", "Breakfast & Dinner"),
                (4, "Panamik Hot Springs & Diskit Hike", "Hike up to Diskit Monastery, explore Panamik natural sulfur springs, and evening campfire.", "Nubra River Camp", "Breakfast & Dinner"),
                (5, "Return to Leh via Hemis Gompa", "Drive back over mountain passes with stop at ancient Hemis Monastery for afternoon chants.", "Singge Palace Guesthouse", "Breakfast & Dinner"),
                (6, "Departure from Leh", "Morning transfer to airport for connecting flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights accommodation in guesthouse and camp tents",
                "Breakfast and dinner on all trekking days",
                "Inner line permits and red tape clearances",
                "Certified mountain guide and oxygen canister support",
                "All transport and toll charges included"
            ],
            "exclusions": [
                "Airfare tickets from Pune",
                "Personal trekking gear (boots, rucksacks)",
                "Lunch meals along the highway",
                "Travel and emergency evacuation insurance"
            ]
        },
        {
            "name": "Luxury Ladakh Glamping & High Altitude Retreat",
            "operator_name": "JourneyMint",
            "destination_name": "Leh",
            "starting_city": "Bangalore",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("78000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/luxury-ladakh-glamping",
            "is_active": True,
            "hotel_info": "5-star luxury glamping pavilions with private heating, en-suite bathrooms, and panoramic mountain decks.",
            "meals_info": "Chef-curated farm-to-table cuisine, organic orchard breakfasts, and sunset cocktail pairings.",
            "transportation_info": "Dedicated luxury Toyota Fortuner / Land Cruiser with oxygen-assisted climate control.",
            "sightseeing_info": "Thiksey sunrise prayer ceremony, Alchi 1000-year-old murals, Pangong Lake, and Stok Palace.",
            "activities_info": "Exclusive private sunrise chanting session with monastery head lama, private astronomy star show, and glamping picnics.",
            "themes": ["luxury", "mountain", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [6, 7, 8, 9],
            "itinerary": [
                (1, "Bangalore Arrival & Luxury Oxygen Chamber Rest", "Warm VIP airport welcome in Leh. Settle into heated luxury pavilion with medical acclimatization check.", "The Chamba Camp Thiksey", "Dinner"),
                (2, "Thiksey Sunrise Chants & Royal Stok Palace", "Early dawn private prayer ceremony with monks at Thiksey. Afternoon visit to royal museum at Stok Palace.", "The Chamba Camp Thiksey", "Breakfast & Dinner"),
                (3, "Scenic Helicopter/Private Drive to Pangong", "Luxury excursion across mountain ranges to private luxury glamping setup overlooking Pangong Tso.", "The Ultimate Travelling Camp Pangong", "Breakfast & Dinner"),
                (4, "Pangong Stargazing & High Altitude Gourmet Picnic", "Morning photography walk along turquoise lake shore. Evening guided stargazing through high-powered telescope.", "The Ultimate Travelling Camp Pangong", "Breakfast & Dinner"),
                (5, "Alchi UNESCO Heritage Murals", "Scenic drive to ancient Alchi village to view pristine 11th-century Buddhist frescoes.", "The Chamba Camp Thiksey", "Breakfast & Dinner"),
                (6, "Private Polo Match & Farewell Banquet", "Witness traditional Ladakhi polo match in afternoon followed by gourmet farewell dinner under mountain stars.", "The Chamba Camp Thiksey", "Breakfast & Dinner"),
                (7, "VIP Farewell to Bangalore", "Private luxury transfer to Leh airport for flight back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "6 nights in ultra-luxury glamping pavilions with heated beds",
                "All gourmet meals, outdoor picnics, and artisanal beverages",
                "Private luxury 4x4 vehicle with dedicated personal driver and concierge",
                "All VIP monastery access passes and private lama sessions",
                "Continuous on-call doctor and oxygen support"
            ],
            "exclusions": [
                "Airfare tickets Bangalore - Leh - Bangalore",
                "Cellar vintage alcoholic reserves",
                "Spa therapies and personal boutique shopping",
                "Personal tips and driver gratuities"
            ]
        },

        # =====================================================================
        # 4. DARJEELING (West Bengal, India) - 3 Packages
        # =====================================================================
        {
            "name": "Darjeeling Himalayan Tea Country Sunrise",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Darjeeling",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("21000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/darjeeling-tea-country",
            "is_active": True,
            "hotel_info": "Colonial-era heritage hotel overlooking Kanchenjunga with cozy fireplaces and tea lounges.",
            "meals_info": "Daily buffet breakfast and 3-course dinners featuring Tibetan and Anglo-Indian recipes.",
            "transportation_info": "Dedicated AC private sedan for Bagdogra airport pick-up and hill excursions.",
            "sightseeing_info": "Tiger Hill, Batasia Loop, Himalayan Mountaineering Institute, and Happy Valley Tea Estate.",
            "activities_info": "Tiger Hill dawn sunrise over Mount Kanchenjunga, tea tasting workshop, and Toy Train ride.",
            "themes": ["mountain", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [3, 4, 5, 6, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bagdogra Arrival & Scenic Hill Climb", "Arrive at Bagdogra airport from Delhi. Scenic 3-hour drive past emerald tea hills to Darjeeling. Check-in hotel.", "Windamere Colonial Heritage Hotel", "Dinner"),
                (2, "Tiger Hill Sunrise & Himalayan Zoo", "Pre-dawn drive to Tiger Hill for sunrise over Mount Kanchenjunga. Visit Padmaja Naidu Himalayan Zoological Park and Snow Leopard center.", "Windamere Colonial Heritage Hotel", "Breakfast & Dinner"),
                (3, "Happy Valley Tea Tasting & Toy Train", "Guided walk through historic Happy Valley Tea Estate. Afternoon joy ride on the UNESCO World Heritage Darjeeling Himalayan Toy Train.", "Windamere Colonial Heritage Hotel", "Breakfast & Dinner"),
                (4, "Ghoom Monastery & Mall Road Stroll", "Morning visit to sacred Ghoom Monastery and Batasia Loop war memorial. Afternoon leisure on Chowrasta Mall Road.", "Windamere Colonial Heritage Hotel", "Breakfast & Dinner"),
                (5, "Descent to Bagdogra & Flight Return", "Scenic descent to Bagdogra airport for afternoon flight back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in colonial heritage room with mountain views",
                "Daily breakfast and chef-prepared dinners",
                "UNESCO Toy Train joyride first-class tickets",
                "Dedicated private vehicle for all transfers and tours",
                "Tea garden visit and tasting session fees"
            ],
            "exclusions": [
                "Flights Delhi - Bagdogra - Delhi",
                "Lunch meals and personal refreshments",
                "Camera permits at zoo and museums",
                "Personal tips and porter charges"
            ]
        },
        {
            "name": "Queen of Hills Scenic Mountain Discovery",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Darjeeling",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("19500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/darjeeling-queen-of-hills",
            "is_active": True,
            "hotel_info": "4-star modern hill resort near Mall Road with glass elevators and pine valley views.",
            "meals_info": "Buffet breakfast and North Indian / Nepali dinner spreads.",
            "transportation_info": "Private AC Innova from Bagdogra airport and for all mountain sightseeing.",
            "sightseeing_info": "Peace Pagoda, Japanese Temple, Rock Garden, and Darjeeling Ropeway.",
            "activities_info": "Cable car ropeway ride over tea valleys, Tibetan refugee self-help center visit, and momo tasting.",
            "themes": ["nature", "mountain", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [3, 4, 5, 6, 10, 11, 12],
            "itinerary": [
                (1, "Flight to Bagdogra & Darjeeling Transfer", "Flight arrival from Mumbai. Scenic drive up through Kurseong hills to Darjeeling. Check-in resort.", "Mayfair Hill Resort", "Dinner"),
                (2, "Darjeeling Ropeway & Rock Garden", "Ride the Darjeeling Ropeway cable car across lush tea gardens. Afternoon visit to the cascading Rock Garden waterfalls.", "Mayfair Hill Resort", "Breakfast & Dinner"),
                (3, "Peace Pagoda & Tibetan Crafts", "Visit the serene Japanese Peace Pagoda and Tibetan Refugee Self-Help Centre to witness carpet weaving.", "Mayfair Hill Resort", "Breakfast & Dinner"),
                (4, "Chowrasta Morning & Bagdogra Return", "Morning stroll at Chowrasta square. Scenic drive down to Bagdogra for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in premium valley room",
                "Daily breakfast and dinner",
                "Private Innova for airport pickup and sightseeing",
                "Ropeway cable car tickets",
                "All toll charges and driver allowances"
            ],
            "exclusions": [
                "Airfare tickets Mumbai - Bagdogra - Mumbai",
                "Lunch meals and personal drinks",
                "Toy train ride (optional add-on)",
                "Travel insurance"
            ]
        },
        {
            "name": "Darjeeling Colonial Heritage & Toy Train Escape",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Darjeeling",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("26000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/darjeeling-colonial-heritage",
            "is_active": True,
            "hotel_info": "Historic British colonial planter's club converted to luxury heritage suites.",
            "meals_info": "Full English breakfasts and colonial dinners with afternoon high tea service.",
            "transportation_info": "Private chauffeur-driven sedan for all excursions and Bagdogra transfers.",
            "sightseeing_info": "St. Andrew's Church, Lloyd's Botanical Garden, Batasia Loop, and Glenary's bakery.",
            "activities_info": "Steam Toy Train heritage charter, tea auction history tour, and evening bakery hopping.",
            "themes": ["heritage", "mountain"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [3, 4, 5, 6, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore Arrival & Planter's Welcome", "Arrive via Bagdogra. Transfer to colonial planters club. Evening tea tasting at iconic Glenary's bakery.", "The Planters Club Heritage Stay", "Dinner"),
                (2, "Steam Toy Train & Ghoom Monasteries", "Board historic steam-engine Toy Train joyride to Ghoom and back around Batasia Loop. Visit century-old St. Andrew's Church.", "The Planters Club Heritage Stay", "Breakfast & Dinner"),
                (3, "Botanical Gardens & Tea History", "Morning stroll through Lloyd's Botanical Garden containing rare Himalayan orchids. Afternoon tea masterclass.", "The Planters Club Heritage Stay", "Breakfast & Dinner"),
                (4, "Kanchenjunga Sunrise & Bagdogra Drop", "Final dawn view of Kanchenjunga peaks from room balcony. Transfer down to Bagdogra for flight back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in heritage colonial suite with working fireplace",
                "Breakfast, high tea, and dinner daily",
                "First-class steam Toy Train ticket passes",
                "Private vehicle for all travel and transfers",
                "Tea sommelier masterclass session"
            ],
            "exclusions": [
                "Airfare Bangalore - Bagdogra - Bangalore",
                "Alcoholic drinks and bar bills",
                "Personal tips to estate staff",
                "Luggage porter charges"
            ]
        },

        # =====================================================================
        # 5. OOTY (Tamil Nadu, India) - 4 Packages
        # =====================================================================
        {
            "name": "Nilgiri Tea Hills & Botanical Escape",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Ooty",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("11500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/ooty-tea-hills-escape",
            "is_active": True,
            "hotel_info": "Charming colonial-style hillside resort overlooking the Ooty valley with landscaped gardens.",
            "meals_info": "Daily buffet breakfast and South/North Indian dinner buffet.",
            "transportation_info": "Roundtrip private AC sedan transfer directly from Bangalore and for all local sightseeing.",
            "sightseeing_info": "Government Botanical Garden, Ooty Lake, Doddabetta Peak, and Rose Garden.",
            "activities_info": "Boating on Ooty Lake, visiting Doddabetta telescope house, and homemade chocolate shopping.",
            "themes": ["nature", "mountain"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore to Ooty Scenic Drive", "Morning pickup in Bangalore. Drive through Bandipur forest and 36 hairpin bends to Ooty. Afternoon boating at Ooty Lake.", "Savoy - IHCL SeleQtions Ooty", "Dinner"),
                (2, "Doddabetta Peak & Botanical Gardens", "Ascend to Doddabetta Peak (8,650 ft), highest point in Nilgiris. Visit Government Botanical Garden and Rose Garden.", "Savoy - IHCL SeleQtions Ooty", "Breakfast & Dinner"),
                (3, "Tea Factory & Return to Bangalore", "Morning tour of Dodabetta Tea Factory and chocolate showroom. Return scenic drive back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in deluxe garden room in Ooty",
                "Breakfast and dinner on both days",
                "Private dedicated AC car from Bangalore to Bangalore",
                "Ooty Lake boat ride tickets and garden entries",
                "Toll taxes, parking fees, and driver allowances"
            ],
            "exclusions": [
                "Lunch meals along the highway",
                "Toy train tickets (optional add-on)",
                "Personal shopping and souvenirs",
                "Travel insurance"
            ]
        },
        {
            "name": "Ooty & Coonoor Scenic Mountain Rail Break",
            "operator_name": "WanderNest Travels",
            "destination_name": "Ooty",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("18500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/ooty-coonoor-rail-break",
            "is_active": True,
            "hotel_info": "Heritage tea estate bungalow nestled amidst rolling tea plantations near Coonoor.",
            "meals_info": "Daily breakfast and home-cooked 3-course dinners including authentic Nilgiri curries.",
            "transportation_info": "Coimbatore airport/station pickup in private AC cab; dedicated car for all tours.",
            "sightseeing_info": "Sim's Park Coonoor, Dolphin's Nose viewpoint, Nilgiri Mountain Toy Train, and Pykara Lake.",
            "activities_info": "UNESCO Nilgiri Mountain Railway toy train ride through mountain tunnels, Pykara speed boat ride, and tea walks.",
            "themes": ["romantic", "nature", "mountain"],
            "travel_types": ["Couple"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Coimbatore Arrival & Nilgiri Hill Drive", "Pick up from Coimbatore. Drive up Nilgiri hills to Coonoor tea estate bungalow. Evening stroll in private tea gardens.", "Tea Nest Heritage Plantation Stay", "Dinner"),
                (2, "UNESCO Mountain Toy Train to Ooty", "Board the iconic Nilgiri Mountain Railway toy train from Coonoor to Ooty. Afternoon visit to Botanical Gardens and Lake.", "Tea Nest Heritage Plantation Stay", "Breakfast & Dinner"),
                (3, "Pykara Waterfalls & Dolphin's Nose", "Excursion to pristine Pykara Lake and waterfalls with speedboating. Sunset at Dolphin's Nose viewpoint.", "Tea Nest Heritage Plantation Stay", "Breakfast & Dinner"),
                (4, "Sim's Park & Coimbatore Return", "Morning walk through Sim's Park botanical arboretum. Drive back to Coimbatore for return transit to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in heritage tea planter's cottage",
                "Daily breakfast and candlelit plantation dinners",
                "Confirmed UNESCO Toy Train tickets",
                "Private AC vehicle for all transfers and excursions",
                "Entry tickets to Pykara and Sim's Park"
            ],
            "exclusions": [
                "Flights/trains Pune - Coimbatore - Pune",
                "Lunch meals and personal trail snacks",
                "Speedboat fees at Pykara lake",
                "Personal tips and driver gratuities"
            ]
        },
        {
            "name": "Mudumalai Wildlife & Ooty Pine Forest Tour",
            "operator_name": "RoamRise Tours",
            "destination_name": "Ooty",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("16000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/mudumalai-ooty-wildlife",
            "is_active": True,
            "hotel_info": "Eco-friendly jungle resort at Mudumalai buffer zone (1N) and cozy mountain resort in Ooty (2N).",
            "meals_info": "All meals during jungle stay; breakfast and dinner in Ooty.",
            "transportation_info": "Private AC Ertiga/Innova from Bangalore covering entire jungle and hill circuit.",
            "sightseeing_info": "Mudumalai Tiger Reserve, Theppakadu Elephant Camp, Pine Forest shooting point, and Avalanche Lake.",
            "activities_info": "Open jeep jungle safari in Mudumalai, elephant interaction, and nature walk through Avalanche Lake pine forests.",
            "themes": ["wildlife", "nature"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Bangalore to Mudumalai Jungle Sanctuary", "Drive from Bangalore to Mudumalai Tiger Reserve. Afternoon forest jeep safari looking for wild elephants, deer, and leopards.", "Wildwoods Jungle Resort Mudumalai", "Lunch & Dinner"),
                (2, "Elephant Camp & Ascent to Ooty", "Morning visit to Theppakadu Elephant Camp. Drive up the 36 hairpin bends to Ooty. Afternoon walk in Pine Forest.", "Sterling Ooty Fern Hill", "Breakfast & Dinner"),
                (3, "Avalanche Lake & Emerald Valley", "Full day excursion to pristine Avalanche Lake and scenic Emerald Lake nestled in rolling shola grasslands.", "Sterling Ooty Fern Hill", "Breakfast & Dinner"),
                (4, "Botanical Walk & Bangalore Return", "Morning stroll at Government Botanical Garden. Scenic descent and drive back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation (1N Mudumalai resort, 2N Ooty resort)",
                "Meals as specified in itinerary",
                "Mudumalai jungle safari entry passes and jeep permits",
                "Private dedicated vehicle for the entire Bangalore-to-Bangalore trip",
                "All toll charges and forest entry fees"
            ],
            "exclusions": [
                "Camera charges inside tiger reserve",
                "Personal snacks and extra beverages",
                "Boating charges at lakes",
                "Medical and personal insurance"
            ]
        },
        {
            "name": "Ooty Luxury Heritage Colonial Bungalow Stay",
            "operator_name": "TravelVista India",
            "destination_name": "Ooty",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("48000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/ooty-luxury-heritage",
            "is_active": True,
            "hotel_info": "5-star historic British Raj palace retreat built in 1829 with private fireplaces and manicured lawns.",
            "meals_info": "Daily royal breakfast, English afternoon tea on the lawn, and 4-course gourmet dinner.",
            "transportation_info": "Chauffeured luxury SUV for Coimbatore airport transfers and private hill touring.",
            "sightseeing_info": "Doddabetta Peak, Glenmorgan tea estate, Pykara Lake, and Ooty Club.",
            "activities_info": "Private tea tasting with estate master, private motorboat ride on Pykara, and evening golf/billiards.",
            "themes": ["luxury", "mountain", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Coimbatore Arrival & Heritage Check-in", "Flight arrival in Coimbatore from Hyderabad. Luxury car transfer to Ooty. Welcome tea at 1829 heritage property.", "Taj Savoy Colonial Hotel", "Dinner"),
                (2, "Private Tea Estate & Glenmorgan Views", "Private tour of Glenmorgan tea plantation. Afternoon high tea and lawn croquet.", "Taj Savoy Colonial Hotel", "Breakfast & Dinner"),
                (3, "Pykara Private Cruise & Shola Forest", "Chauffeured drive to Pykara Lake for private boat cruise followed by walk in ancient Shola woodlands.", "Taj Savoy Colonial Hotel", "Breakfast & Dinner"),
                (4, "Doddabetta Panorama & Spa Relaxation", "Morning visit to Doddabetta Peak with private guide. Afternoon signature herbal spa treatment.", "Taj Savoy Colonial Hotel", "Breakfast & Dinner"),
                (5, "Leisure Breakfast & Coimbatore Drop", "Relaxing breakfast by the colonial fireplace. Private transfer to Coimbatore for flight to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in luxury heritage suite with working fireplace",
                "Daily champagne breakfast and multi-course dinners",
                "Private luxury vehicle throughout",
                "Private boat charter at Pykara Lake",
                "Spa therapy session for two guests"
            ],
            "exclusions": [
                "Airfare Hyderabad - Coimbatore - Hyderabad",
                "Vintage wines and bar orders",
                "Golf course green fees at Ooty Golf Club",
                "Gratuities and personal expenses"
            ]
        },

        # =====================================================================
        # 6. COORG (Karnataka, India) - 4 Packages
        # =====================================================================
        {
            "name": "Coorg Coffee Plantation & Misty Valley Weekend",
            "operator_name": "Horizon Trails",
            "destination_name": "Coorg",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("9800.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/coorg-coffee-weekend",
            "is_active": True,
            "hotel_info": "Charming coffee estate homestay surrounded by pepper vines and silver oak trees.",
            "meals_info": "Daily breakfast and home-cooked Kodava specialties (pandi curry, akki roti, and filter coffee).",
            "transportation_info": "Roundtrip private AC sedan transfer directly from Bangalore and for all tours.",
            "sightseeing_info": "Abbey Falls, Raja's Seat, Madikeri Fort, and Omkareshwara Temple.",
            "activities_info": "Guided coffee plantation walk with bean-to-cup brewing workshop and sunset views at Raja's Seat.",
            "themes": ["nature", "romantic"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore to Coorg & Raja's Seat Sunset", "Morning pickup in Bangalore. Drive through Mysore highway to Coorg (5.5 hrs). Check-in homestay. Sunset at Raja's Seat musical fountain.", "Misty Woods Estate Homestay", "Dinner"),
                (2, "Abbey Falls & Coffee Plantation Tour", "Morning hike to scenic Abbey Falls amidst spice groves. Afternoon walking tour of coffee estate with bean picking and roasting demo.", "Misty Woods Estate Homestay", "Breakfast & Dinner"),
                (3, "Madikeri Fort & Bangalore Return", "Visit historic 17th-century Madikeri Fort and Gothic-Islamic Omkareshwara temple. Return drive to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in plantation cottage on working coffee estate",
                "Daily Kodava breakfast and home-cooked dinners",
                "Private dedicated AC car from Bangalore to Bangalore",
                "Coffee tasting and plantation tour fees",
                "All toll charges, parking, and driver allowances"
            ],
            "exclusions": [
                "Lunch meals along the highway",
                "Personal spice and coffee purchases",
                "Entry fees to private spice parks",
                "Travel insurance"
            ]
        },
        {
            "name": "Coorg Wilderness & Nagarhole Safari Adventure",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Coorg",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("19000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/coorg-nagarhole-safari",
            "is_active": True,
            "hotel_info": "Eco-wilderness resort situated near Nagarhole National Park border with outdoor pool.",
            "meals_info": "Buffet breakfast, lunch, and dinner included throughout the stay.",
            "transportation_info": "Private AC SUV from Bangalore covering entire jungle and coffee circuit.",
            "sightseeing_info": "Nagarhole National Park, Dubare Elephant Camp, Iruppu Falls, and Cauvery Nisargadhama.",
            "activities_info": "Open jeep jungle safari in Nagarhole, elephant bathing at Dubare, and trek to Iruppu Waterfalls.",
            "themes": ["wildlife", "nature"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Bangalore to Nagarhole Safari Gateway", "Morning departure from Bangalore. Check into wilderness resort near Nagarhole. Evening guided nature trail and campfire.", "Kabini Wilderness Eco Resort", "Lunch & Dinner"),
                (2, "Nagarhole Tiger Safari & Dubare Camp", "Early morning jungle safari in Nagarhole. Afternoon visit to Dubare Elephant Camp along river Cauvery.", "Kabini Wilderness Eco Resort", "Breakfast, Lunch & Dinner"),
                (3, "Iruppu Falls & Brahmagiri Foothills", "Trek through lush Brahmagiri forest to scenic Iruppu Falls. Visit Cauvery Nisargadhama bamboo island.", "Kabini Wilderness Eco Resort", "Breakfast, Lunch & Dinner"),
                (4, "Morning Bird Walk & Bangalore Return", "Guided early morning bird watching walk. Check out and return drive back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in eco-resort cottage",
                "All meals included (3 breakfasts, 3 lunches, 3 dinners)",
                "Nagarhole National Park safari permit and jeep passes",
                "Private AC vehicle for entire trip from Bangalore",
                "Naturalist guide for nature and birding walks"
            ],
            "exclusions": [
                "Elephant interaction/bathing fees at Dubare",
                "Camera fees inside National Park",
                "Personal tips and driver gratuities",
                "Travel and health insurance"
            ]
        },
        {
            "name": "Coorg Romance in the Rainforest",
            "operator_name": "JourneyMint",
            "destination_name": "Coorg",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("36000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/coorg-romance-rainforest",
            "is_active": True,
            "hotel_info": "5-star luxury rainforest resort with private plunge pool villas and canopy views.",
            "meals_info": "Daily gourmet breakfast, private candlelit dinner under the stars, and evening wine tasting.",
            "transportation_info": "Private luxury car transfer from Mangalore/Bangalore airport to Coorg.",
            "sightseeing_info": "Tadiandamol Peak foothills, Chelavara Falls, and private estate nature sanctuaries.",
            "activities_info": "Couples coffee scrub spa ritual, private forest dining, and plantation birdwatching.",
            "themes": ["romantic", "nature", "luxury"],
            "travel_types": ["Couple"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Arrival & Rainforest Villa Check-in", "Flight arrival in Mangalore from Pune. Private scenic transfer to luxury resort nestled in 300-acre rainforest. Evening welcome cocktail.", "Evolve Back Kuruba Safari Lodge", "Dinner"),
                (2, "Private Plantation Walk & Spa Ritual", "Morning guided plantation walk. Afternoon signature coffee-infused couples massage and relaxation by private plunge pool.", "Evolve Back Kuruba Safari Lodge", "Breakfast & Dinner"),
                (3, "Chelavara Falls & Candlelit Dining", "Scenic drive to secluded Chelavara Falls. Evening bespoke private 5-course candlelit dinner beside the forest stream.", "Evolve Back Kuruba Safari Lodge", "Breakfast & Dinner"),
                (4, "Morning Mist Walk & Airport Departure", "Morning canopy birding walk. Leisurely gourmet breakfast before private transfer to airport for Pune flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in private luxury pool villa",
                "Breakfast daily and one bespoke 5-course private dinner",
                "Private luxury vehicle for all airport transfers and outings",
                "Couples signature spa therapy session",
                "Guided private naturalist walks"
            ],
            "exclusions": [
                "Airfare tickets Pune - Mangalore - Pune",
                "Alcoholic beverage orders beyond welcome cocktail",
                "Personal laundry and boutique expenses",
                "Travel insurance"
            ]
        },
        {
            "name": "Coorg Spice Country & Western Ghats Trail",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Coorg",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("28000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/coorg-spice-country-trail",
            "is_active": True,
            "hotel_info": "4-star eco-heritage resort amidst cardamom and vanilla plantations near Kushalnagar.",
            "meals_info": "Daily buffet breakfast and regional South Indian / Coorg specialty dinners.",
            "transportation_info": "Private AC vehicle from Bangalore airport/station to Coorg and for all excursions.",
            "sightseeing_info": "Namdroling Monastery (Golden Temple), Dubare Elephant Reserve, Talacauvery, and Bhagamandala.",
            "activities_info": "Tibetan prayer wheel experience, holy dip at origin of river Cauvery (Talacauvery), and spice shopping.",
            "themes": ["nature", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Hyderabad to Bangalore & Coorg Drive", "Flight arrival in Bangalore from Hyderabad. Drive through coffee country to Coorg. Evening Tibetan monastery visit at Bylakuppe.", "The Windflower Resort & Spa Coorg", "Dinner"),
                (2, "Golden Temple & Dubare Elephants", "Explore the magnificent Namdroling Golden Temple. Afternoon elephant interaction at Dubare Reserve along the river.", "The Windflower Resort & Spa Coorg", "Breakfast & Dinner"),
                (3, "Talacauvery & Brahmagiri Hills", "Pilgrimage drive to Talacauvery, sacred birthplace of River Cauvery on Brahmagiri slopes. Scenic views over Western Ghats.", "The Windflower Resort & Spa Coorg", "Breakfast & Dinner"),
                (4, "Abbey Falls & Coffee Tasting", "Morning visit to Abbey Falls. Afternoon guided coffee and cardamom tasting session with local planters.", "The Windflower Resort & Spa Coorg", "Breakfast & Dinner"),
                (5, "Shopping & Bangalore Airport Return", "Morning purchase of fresh spices and coffee beans. Drive back to Bangalore for evening flight to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in premium plantation villa",
                "Daily breakfast and dinner",
                "Dedicated private AC vehicle for all transfers and tours",
                "All toll fees, parking, and driver allowances",
                "Guided plantation tour and monastery entry passes"
            ],
            "exclusions": [
                "Flights Hyderabad - Bangalore - Hyderabad",
                "Lunch meals during transit and sightseeing",
                "Elephant ride/bathing charges",
                "Personal shopping expenses"
            ]
        },

        # =====================================================================
        # 7. AGRA (Uttar Pradesh, India) - 3 Packages
        # =====================================================================
        {
            "name": "Taj Mahal & Imperial Mughal Heritage Express",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Agra",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("8500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/taj-mahal-express",
            "is_active": True,
            "hotel_info": "3-star comfortable hotel located 1 km from the Taj Mahal East Gate.",
            "meals_info": "Daily breakfast and authentic Mughlai dinners (chicken tikka, biryani, and petha).",
            "transportation_info": "Gatimaan Express / Yamuna Expressway private AC car from Delhi and for local touring.",
            "sightseeing_info": "Taj Mahal, Agra Fort, Mehtab Bagh, and Itmad-ud-Daulah (Baby Taj).",
            "activities_info": "Sunrise photography tour at Taj Mahal, sunset view from Mehtab Bagh across the Yamuna, and marble inlay demo.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Solo", "Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Delhi to Agra & Sunset at Mehtab Bagh", "Morning drive or Gatimaan Express to Agra. Hotel check-in. Evening sunset view of Taj Mahal from across River Yamuna at Mehtab Bagh.", "Howard Plaza The Fern Agra", "Dinner"),
                (2, "Taj Mahal Sunrise & Agra Fort", "Dawn entry to Taj Mahal for sunrise light. Return for breakfast. Afternoon guided exploration of the grand Agra Fort red sandstone palace.", "Howard Plaza The Fern Agra", "Breakfast & Dinner"),
                (3, "Baby Taj, Marble Crafts & Delhi Return", "Morning visit to exquisite tomb of Itmad-ud-Daulah. Visit traditional marble inlay artisans before returning to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights accommodation near Taj East Gate",
                "Daily breakfast and traditional Mughlai dinners",
                "Roundtrip private AC car or Gatimaan train tickets from Delhi",
                "Certified ASI heritage monument guide for Taj and Fort",
                "All toll taxes and parking charges"
            ],
            "exclusions": [
                "Monument entry tickets (approx. Rs 50-250)",
                "Lunch meals and personal drinks",
                "Personal shopping for marble souvenirs",
                "Travel insurance"
            ]
        },
        {
            "name": "Agra Fort & Fatehpur Sikri Historical Immersion",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Agra",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("21000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/agra-fatehpur-sikri-immersion",
            "is_active": True,
            "hotel_info": "4-star modern hotel on Fatehabad Road with swimming pool and view of the Taj Mahal silhouette.",
            "meals_info": "Daily buffet breakfast and chef-crafted Mughlai dinners.",
            "transportation_info": "Private dedicated AC vehicle for airport transfers, city tours, and Fatehpur Sikri excursion.",
            "sightseeing_info": "Taj Mahal, Agra Fort, Fatehpur Sikri, Buland Darwaza, and Akbar's Tomb at Sikandra.",
            "activities_info": "Walking through Akbar's abandoned capital at Fatehpur Sikri, Sufi shrine visit at Salim Chishti, and heritage bazaar walk.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Delhi/Agra Arrival & Evening Mohabbat The Taj", "Flight arrival from Hyderabad. Private transfer to Agra hotel. Evening cultural theatrical dance show 'Mohabbat The Taj'.", "Courtyard by Marriott Agra", "Dinner"),
                (2, "Taj Mahal at Sunrise & Imperial Agra Fort", "Early sunrise tour of the Taj Mahal. Afternoon guided tour of the massive halls of Jahangir Palace inside Agra Fort.", "Courtyard by Marriott Agra", "Breakfast & Dinner"),
                (3, "Fatehpur Sikri & Buland Darwaza Excursion", "Day excursion to the UNESCO ghost city of Fatehpur Sikri, Buland Darwaza gate of victory, and Sheikh Salim Chishti dargah.", "Courtyard by Marriott Agra", "Breakfast & Dinner"),
                (4, "Sikandra Tomb & Return Flight", "Morning visit to Emperor Akbar's Tomb at Sikandra with peaceful deer gardens. Transfer to airport for flight to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in deluxe room",
                "Daily buffet breakfast and dinner",
                "Private dedicated AC car for all transfers and excursions",
                "Professional English/Hindi speaking ASI guide",
                "All toll taxes, interstate permits, and driver charges"
            ],
            "exclusions": [
                "Airfare tickets Hyderabad - Delhi/Agra - Hyderabad",
                "Monument entry tickets and battery bus charges",
                "Tickets to Mohabbat The Taj live show",
                "Personal tips and laundry expenses"
            ]
        },
        {
            "name": "Royal Agra Luxury Heritage & Private Taj Sunrise",
            "operator_name": "JourneyMint",
            "destination_name": "Agra",
            "starting_city": "Mumbai",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("42000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/royal-agra-luxury",
            "is_active": True,
            "hotel_info": "5-star ultra-luxury resort where every room offers uninterrupted direct views of the Taj Mahal.",
            "meals_info": "Gourmet breakfasts, poolside high tea, and fine dining Mughal banquet with live sitar music.",
            "transportation_info": "Private luxury BMW/Mercedes transfers and electric golf cart direct to Taj entrance.",
            "sightseeing_info": "Taj Mahal, Agra Fort private quarters, and exclusive moonlight view from private terrace.",
            "activities_info": "VIP early-morning Taj Mahal entry with professional photographer, private royal cooking demo, and Mughal spa session.",
            "themes": ["luxury", "heritage", "romantic"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai to Agra Luxury Arrival", "Flight to Delhi/Agra with luxury chauffeur transfer. Welcome royal garlands at 5-star palace hotel. Sunset high tea overlooking the Taj.", "The Oberoi Amarvilas Agra", "Dinner"),
                (2, "VIP Taj Sunrise & Royal Banquet", "VIP early morning entry to the Taj Mahal with private historian and photographer. Afternoon couples spa. Evening poolside Mughal banquet.", "The Oberoi Amarvilas Agra", "Breakfast & Dinner"),
                (3, "Agra Fort Heritage Walk & Return", "Morning tour of Agra Fort's Musamman Burj. Private transfer for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in Premier Room with direct Taj Mahal views",
                "All gourmet breakfasts and royal banquet dinners",
                "Private luxury vehicle with dedicated chauffeur",
                "Private professional photographer for Taj photoshoot",
                "VIP entry tickets and royal historian accompaniment"
            ],
            "exclusions": [
                "Flights Mumbai - Delhi/Agra - Mumbai",
                "Spa treatments and salon services",
                "Cellar champagne and imported liquors",
                "Personal tips and driver gratuities"
            ]
        },

        # =====================================================================
        # 8. VARANASI (Uttar Pradesh, India) - 4 Packages
        # =====================================================================
        {
            "name": "Sacred Ghats & Ganga Aarti Spiritual Dawn",
            "operator_name": "RoamRise Tours",
            "destination_name": "Varanasi",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("10500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/varanasi-sacred-ghats",
            "is_active": True,
            "hotel_info": "Heritage hotel on the holy riverfront with panoramic views of the sacred Ganges.",
            "meals_info": "Daily pure vegetarian breakfast and Banarasi thali dinners.",
            "transportation_info": "Vande Bharat Express train from Delhi; private boat and AC car in Varanasi.",
            "sightseeing_info": "Dashashwamedh Ghat, Kashi Vishwanath Temple, Assi Ghat, and Manikarnika Ghat.",
            "activities_info": "Evening Dashashwamedh Ganga Aarti from boat, dawn rowboat cruise along historic ghats, and temple darshan.",
            "themes": ["spiritual", "culture"],
            "travel_types": ["Solo", "Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Vande Bharat Arrival & Evening Ganga Aarti", "Morning Vande Bharat train from Delhi. Riverfront hotel check-in. Evening boat ride to witness the grand Dashashwamedh Ganga Aarti.", "BrijRama Palace Heritage Ghat Hotel", "Dinner"),
                (2, "Subah-e-Banaras Dawn Cruise & Kashi Darshan", "Sunrise boat ride along 84 sacred ghats witnessing morning rituals. Visit the new Kashi Vishwanath Corridor and Annapurna Temple.", "BrijRama Palace Heritage Ghat Hotel", "Breakfast & Dinner"),
                (3, "Banaras Hindu University & Delhi Return", "Morning visit to Bharat Kala Bhavan museum and New Vishwanath Temple inside BHU. Afternoon train back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in authentic riverfront heritage hotel",
                "Daily vegetarian breakfast and traditional thali dinners",
                "Roundtrip AC train tickets from Delhi",
                "Private evening and dawn boat rides on the Ganges",
                "Local priest/guide for temple darshan"
            ],
            "exclusions": [
                "Lunch meals and street food snacks",
                "Special puja donation charges",
                "Personal tips and boatmen gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Varanasi Living Heritage & Sarnath Pilgrimage",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Varanasi",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("18500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/varanasi-sarnath-pilgrimage",
            "is_active": True,
            "hotel_info": "4-star riverside hotel featuring tranquil courtyards and vegetarian fine dining.",
            "meals_info": "Buffet breakfast daily and satvik vegetarian dinners.",
            "transportation_info": "Private dedicated AC car for all airport transfers, city tours, and Sarnath excursion.",
            "sightseeing_info": "Sarnath Dhamek Stupa, Ashoka Pillar, Mulagandha Kuti Vihar, Kashi Vishwanath, and Ramnagar Fort.",
            "activities_info": "Exploring Buddha's first sermon site at Sarnath, archaeological museum visit, and boat tour on the Ganges.",
            "themes": ["spiritual", "heritage", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Hyderabad Arrival & Sacred Ghats Welcome", "Flight arrival from Hyderabad. Hotel check-in. Evening boat excursion for sunset Ganga Aarti at Dashashwamedh Ghat.", "Taj Ganges Varanasi", "Dinner"),
                (2, "Sunrise Boat Cruise & Kashi Corridor", "Dawn boat ride along the ghats. Walk through the historic Kashi Vishwanath corridor and ancient alleyways.", "Taj Ganges Varanasi", "Breakfast & Dinner"),
                (3, "Sarnath Buddhist Pilgrimage & Ramnagar Fort", "Half-day excursion to Sarnath to view Dhamek Stupa and Ashoka Lion capital. Afternoon visit to Ramnagar Fort across the river.", "Taj Ganges Varanasi", "Breakfast & Dinner"),
                (4, "Weavers Colony & Return Flight", "Morning visit to traditional Banarasi silk weavers colony. Afternoon transfer to airport for Hyderabad flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in 4-star room",
                "Daily breakfast and dinner",
                "Dedicated private AC vehicle throughout",
                "Private chartered boat for Ganga Aarti and morning cruise",
                "Sarnath archaeological site entry tickets"
            ],
            "exclusions": [
                "Airfare tickets Hyderabad - Varanasi - Hyderabad",
                "Lunch meals and street food expenses",
                "Camera fees at museums",
                "Personal tips and driver gratuities"
            ]
        },
        {
            "name": "Varanasi Classical Music & Silk Weavers Culture Trail",
            "operator_name": "WanderNest Travels",
            "destination_name": "Varanasi",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("22000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/varanasi-silk-weavers-trail",
            "is_active": True,
            "hotel_info": "Boutique heritage palace with antique furnishings and traditional Indian courtyard music sessions.",
            "meals_info": "Daily breakfast, traditional street food tasting tour (tamatar chaat, kachori, thandai), and royal dinners.",
            "transportation_info": "Private AC sedan for transfers and local transit.",
            "sightseeing_info": "Assi Ghat, Tulsi Manas Temple, Kabir Chaura music quarter, and Sarai Mohana silk weaving village.",
            "activities_info": "Private evening sitar and tabla concert, hands-on handloom weaving masterclass, and boat photography session.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai Arrival & Assi Ghat Subah Session", "Flight to Varanasi from Mumbai. Check into boutique heritage haveli. Sunset musical gathering at Assi Ghat.", "Suryauday Haveli by Shibani", "Dinner"),
                (2, "Kabir Chaura Music Quarter & Street Food", "Guided cultural exploration of Kabir Chaura, birthplace of classical legends. Afternoon culinary trail tasting Banaras chaats.", "Suryauday Haveli by Shibani", "Breakfast & Dinner"),
                (3, "Silk Weaving Village & Private Sitar Concert", "Visit Sarai Mohana artisan village to observe master weavers crafting Banarasi brocades. Evening private classical sitar recital.", "Suryauday Haveli by Shibani", "Breakfast & Dinner"),
                (4, "Dawn Boat Ride & Return Flight", "Early morning boat ride capturing mist over ancient palatial ghats. Transfer to Varanasi airport for flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in boutique riverfront heritage suite",
                "Daily breakfast and curated culinary dinners",
                "Private evening classical Indian music recital",
                "Silk weaving workshop and guided cultural tour",
                "Private chartered sunrise boat on the Ganges"
            ],
            "exclusions": [
                "Flights Mumbai - Varanasi - Mumbai",
                "Personal purchases of Banarasi silk sarees",
                "Alcoholic beverages",
                "Travel insurance"
            ]
        },
        {
            "name": "Ancient Kashi Luxury Riverside Retreat",
            "operator_name": "TravelVista India",
            "destination_name": "Varanasi",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("48000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1561359313-0639aad49ca6?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/ancient-kashi-luxury-retreat",
            "is_active": True,
            "hotel_info": "5-star 210-year-old palace on Darbhanga Ghat, accessible exclusively by private royal barge.",
            "meals_info": "Gourmet vegetarian satvik dining, royal high tea with Ganges views, and Ayurvedic wellness menus.",
            "transportation_info": "Private luxury airport transfers and exclusive electric royal boat on 24-hour disposal.",
            "sightseeing_info": "Darbhanga Ghat, Chet Singh Fort, private temple sanctums, and Sarnath deer park.",
            "activities_info": "Private Vedic blessing ceremony with senior Sanskrit scholar, couples Ayurvedic massage, and royal barge dinner.",
            "themes": ["luxury", "spiritual", "culture"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune Arrival & Royal Barge Check-in", "Flight arrival from Pune. Chauffeur transfer to jetty and royal private barge transfer to palace. Evening Ganga Aarti from private deck.", "Brijrama Palace Luxury Ghat Heritage", "Dinner"),
                (2, "Vedic Blessing & Ancient City Exploration", "Private sunrise Vedic chanting ceremony. VIP guided walking tour of ancient sacred alleyways and private temple sanctums.", "Brijrama Palace Luxury Ghat Heritage", "Breakfast & Dinner"),
                (3, "Gourmet Royal Barge Dinner Cruise", "Day at leisure enjoying Ayurvedic spa. Evening private dinner cruise on royal barge with live instrumental music.", "Brijrama Palace Luxury Ghat Heritage", "Breakfast & Dinner"),
                (4, "Dawn Yoga & Luxury Departure", "Dawn rooftop yoga overlooking the holy river. Royal breakfast followed by private transfer to airport for Pune flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in luxury palace suite with Ganges river views",
                "All gourmet satvik meals and royal afternoon tea",
                "Private luxury airport transfers and private barge at disposal",
                "VIP temple entry clearances and private Vedic scholar",
                "Full Ayurvedic spa treatment for guests"
            ],
            "exclusions": [
                "Airfare tickets Pune - Varanasi - Pune",
                "Custom jewelry and luxury silk purchases",
                "Personal tips and royal butler gratuities",
                "Comprehensive travel insurance"
            ]
        },

        # =====================================================================
        # 9. LAKSHADWEEP (India) - 4 Packages (BEACH!)
        # =====================================================================
        {
            "name": "Bangaram Atoll Coral Diving & Beach Escape",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Lakshadweep",
            "starting_city": "Mumbai",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("38000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/bangaram-atoll-beach-escape",
            "is_active": True,
            "hotel_info": "Eco-friendly beachfront cottages on uninhabited Bangaram Island surrounded by a turquoise lagoon.",
            "meals_info": "All meals included: tropical breakfast, fresh seafood lunch, and beach barbecue dinners.",
            "transportation_info": "Speedboat transfers from Agatti airstrip to Bangaram Island resort.",
            "sightseeing_info": "Bangaram Atoll, Thinnakara Island, Parali I and II islets, and ship wreck diving site.",
            "activities_info": "Scuba diving at coral reefs, sea turtle snorkeling, kayaking in shallow lagoon, and sunset beach walks.",
            "themes": ["beach", "adventure", "nature"],
            "travel_types": ["Couple", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Agatti & Bangaram Speedboat", "Flight from Mumbai via Kochi to Agatti. 45-min speedboat transfer across turquoise waters to Bangaram Island. Beach sunset walk.", "Bangaram Island Beach Resort", "Lunch & Dinner"),
                (2, "Coral Reef Snorkeling & Sea Turtles", "Morning guided boat trip to outer coral reef for snorkeling with sea turtles and manta rays. Afternoon lagoon kayaking.", "Bangaram Island Beach Resort", "Breakfast, Lunch & Dinner"),
                (3, "Thinnakara Uninhabited Island Excursion", "Day boat excursion to uninhabited Thinnakara island. Picnic lunch under coconut palms and shipwreck snorkeling.", "Bangaram Island Beach Resort", "Breakfast, Lunch & Dinner"),
                (4, "Scuba Diving & Starlit Beach Barbecue", "Introductory scuba dive with PADI certified instructor. Evening bonfire beach barbecue under tropical stars.", "Bangaram Island Beach Resort", "Breakfast, Lunch & Dinner"),
                (5, "Speedboat to Agatti & Return Flight", "Early morning speedboat transfer to Agatti airport for onward connecting flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in beach-facing wooden cottage",
                "All meals included (breakfast, lunch, dinner, and afternoon tea)",
                "Lakshadweep mandatory entry permit and clearance processing",
                "Speedboat transfers between Agatti and Bangaram Island",
                "Snorkeling gear hire and guided reef excursion"
            ],
            "exclusions": [
                "Flights Mumbai - Agatti - Mumbai",
                "PADI scuba diving certification fees (optional)",
                "Personal tips and watersports equipment hire",
                "Travel and watersports insurance"
            ]
        },
        {
            "name": "Agatti Island Turquoise Lagoon Getaway",
            "operator_name": "RoamRise Tours",
            "destination_name": "Lakshadweep",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("28000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/agatti-lagoon-getaway",
            "is_active": True,
            "hotel_info": "Beachside air-conditioned cottages located right on Agatti Island's powdery white sand beach.",
            "meals_info": "All meals included: wholesome South Indian and coastal seafood preparations with fresh coconut.",
            "transportation_info": "Airport pickup on Agatti island and private motorized island boats.",
            "sightseeing_info": "Agatti coral lagoon, Kalpitti Island, marine museum, and southern beach point.",
            "activities_info": "Glass-bottom boat ride, lagoon swimming, deep sea fishing, and sunset beach cycling.",
            "themes": ["beach", "nature"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Flight to Agatti & Lagoon Check-in", "Flight arrival from Bangalore. 5-min transfer to beachfront cottage. Afternoon relaxing in the azure waters of the lagoon.", "Agatti Island Beach Resort", "Lunch & Dinner"),
                (2, "Glass-Bottom Boat & Coral Gardens", "Morning glass-bottom boat tour viewing living corals and exotic reef fish. Afternoon cycling around the narrow island.", "Agatti Island Beach Resort", "Breakfast, Lunch & Dinner"),
                (3, "Kalpitti Island Excursion & Snorkeling", "Boat excursion to nearby uninhabited Kalpitti islet for beach beachcombing and coral snorkeling.", "Agatti Island Beach Resort", "Breakfast, Lunch & Dinner"),
                (4, "Morning Beach Dip & Bangalore Flight", "Early sunrise swim in the calm lagoon. Short transfer to Agatti airport for flight to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in AC beach cottage",
                "All meals (breakfast, lunch, and dinner daily)",
                "Lakshadweep Tourism entry permit and documentation",
                "Glass-bottom boat ride and Kalpitti island excursion",
                "Complimentary bicycle usage on Agatti island"
            ],
            "exclusions": [
                "Flights Bangalore - Agatti - Bangalore",
                "Deep sea fishing gear charges",
                "Personal expenses and bottled refreshments",
                "Medical and baggage insurance"
            ]
        },
        {
            "name": "Lakshadweep Watersports & Scuba Odyssey",
            "operator_name": "Horizon Trails",
            "destination_name": "Lakshadweep",
            "starting_city": "Pune",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("34000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/lakshadweep-watersports-odyssey",
            "is_active": True,
            "hotel_info": "Comfortable beach cottages with direct water sports dock access in Agatti and Bangaram.",
            "meals_info": "All meals included with protein-rich coastal cuisine and refreshing tropical juices.",
            "transportation_info": "Inter-island speedboats and airport transfers included.",
            "sightseeing_info": "Agatti reef, Bangaram lagoon, and shallow ship wreck coral gardens.",
            "activities_info": "Two guided scuba dives, windsurfing, stand-up paddleboarding, and night reef walk.",
            "themes": ["beach", "adventure"],
            "travel_types": ["Group", "Solo"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Pune to Agatti Island Arrival", "Flight from Pune via Kochi into Agatti. Check-in to dive camp. Water sports safety and gear fitting session.", "Agatti Adventure Watersports Camp", "Lunch & Dinner"),
                (2, "Scuba Dive 1 & Paddleboarding", "First ocean scuba dive exploring coral overhangs and reef sharks. Afternoon stand-up paddleboarding across the lagoon.", "Agatti Adventure Watersports Camp", "Breakfast, Lunch & Dinner"),
                (3, "Speedboat to Bangaram & Dive 2", "Speedboat transfer to Bangaram Atoll. Second scuba dive at the famous ship wreck dive site. Sunset windsurfing.", "Agatti Adventure Watersports Camp", "Breakfast, Lunch & Dinner"),
                (4, "Deep Sea Kayaking & Beach Bonfire", "Morning open sea kayaking safari. Afternoon volleyball and evening seafood bonfire on the sand.", "Agatti Adventure Watersports Camp", "Breakfast, Lunch & Dinner"),
                (5, "Agatti Departure to Pune", "Morning transfer to Agatti airstrip for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in adventure beach cottage accommodation",
                "All daily meals (breakfast, lunch, dinner)",
                "2 guided scuba dives with full equipment and PADI divemaster",
                "Speedboat transfers and all island entry permits",
                "Unlimited use of kayaks and paddleboards"
            ],
            "exclusions": [
                "Flights Pune - Agatti - Pune",
                "Advanced PADI certification course upgrades",
                "Personal tips and gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Lakshadweep Private Atoll Luxury Beach Break",
            "operator_name": "JourneyMint",
            "destination_name": "Lakshadweep",
            "starting_city": "Delhi",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("85000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/lakshadweep-luxury-beach",
            "is_active": True,
            "hotel_info": "5-star private luxury villa on pristine atoll with open-air bathrooms and ocean deck.",
            "meals_info": "All inclusive gourmet tropical dining, private beach candlelit dinners, and fresh coconut cocktails.",
            "transportation_info": "VIP airport reception and private twin-engine speedboat charter.",
            "sightseeing_info": "Private atolls, deserted sandbanks, turquoise coral gardens, and sunset points.",
            "activities_info": "Private yacht sandbank picnic, sunset dolphin cruise, and couples bioluminescence night walk.",
            "themes": ["beach", "luxury", "romantic"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Delhi Flight Arrival & Private Speedboat", "Flight arrival in Agatti. Private yacht charter transfer to secluded atoll villa. Sunset champagne on private deck.", "The Bangaram Island Luxury Sanctuary", "Lunch & Dinner"),
                (2, "Sandbank Castaway Picnic", "Private boat ride to an uninhabited tidal sandbank for an exclusive castaway lunch with personal chef.", "The Bangaram Island Luxury Sanctuary", "Breakfast, Lunch & Dinner"),
                (3, "Coral Reef Diving & Spa Rejuvenation", "Private guided coral reef scuba dive followed by restorative coconut milk spa massage on the beach.", "The Bangaram Island Luxury Sanctuary", "Breakfast, Lunch & Dinner"),
                (4, "Sunset Dolphin Cruise & Candlelit Feast", "Evening catamaran cruise spotting spinner dolphins followed by a 5-course candlelit dinner on the sand.", "The Bangaram Island Luxury Sanctuary", "Breakfast, Lunch & Dinner"),
                (5, "Leisure Beach Day & Bioluminescence", "Leisure morning sunbathing and snorkeling. Night walk along the tide to witness glowing bioluminescent plankton.", "The Bangaram Island Luxury Sanctuary", "Breakfast, Lunch & Dinner"),
                (6, "Private Yacht to Agatti & Flight Home", "Private yacht return to Agatti airstrip for flight back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in ultra-luxury beach villa",
                "All gourmet meals, private sandbank picnic, and beach banquets",
                "Private speedboat transfers and yacht cruises",
                "All Lakshadweep VIP permits and island clearances",
                "Private PADI instructor and spa sessions"
            ],
            "exclusions": [
                "Airfare Delhi - Agatti - Delhi",
                "Vintage French champagnes and private cellar orders",
                "Personal tips and butler gratuities",
                "Comprehensive travel insurance"
            ]
        },

        # =====================================================================
        # 10. MYSORE (Karnataka, India) - 3 Packages
        # =====================================================================
        {
            "name": "Mysore Palace & Silk Weaving Heritage Tour",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Mysore",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("8200.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/mysore-palace-heritage-tour",
            "is_active": True,
            "hotel_info": "3-star comfortable heritage hotel near Mysore Palace with authentic South Indian restaurant.",
            "meals_info": "Daily breakfast and traditional royal Mysore thali dinners (Mylari dosa, Mysore pak, and thali).",
            "transportation_info": "Private AC sedan for Bangalore - Mysore - Bangalore transfer and local tours.",
            "sightseeing_info": "Mysore Palace, Chamundi Hills, Brindavan Gardens, and Devaraja Market.",
            "activities_info": "Evening viewing of 100,000 illuminated palace bulbs, sandalwood carving demo, and silk weaving tour.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Solo", "Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore to Mysore & Palace Illumination", "Morning pickup in Bangalore (3 hrs via Expressway). Check-in hotel. Evening visit to witness Mysore Palace illuminated by thousands of lights.", "Royal Orchid Metropole Mysore", "Dinner"),
                (2, "Chamundi Hill & Silk Weaving Factory", "Morning climb to Sri Chamundeshwari Temple on Chamundi Hill. Afternoon visit to the Government Silk Weaving Factory and Brindavan Gardens.", "Royal Orchid Metropole Mysore", "Breakfast & Dinner"),
                (3, "Devaraja Market & Bangalore Return", "Morning walk through vibrant Devaraja spice and flower market. Taste authentic Mysore Pak before returning to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights accommodation near palace corridor",
                "Daily breakfast and traditional dinners",
                "Private dedicated AC car from Bangalore to Bangalore",
                "Mysore Palace entry tickets and audio guide",
                "All highway tolls and driver charges"
            ],
            "exclusions": [
                "Lunch meals along the highway",
                "Camera tickets at monuments",
                "Personal shopping for sandalwood and silk",
                "Travel insurance"
            ]
        },
        {
            "name": "Royal Mysore & Srirangapatna Heritage Trail",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Mysore",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("16500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/royal-mysore-srirangapatna-trail",
            "is_active": True,
            "hotel_info": "4-star heritage hotel with colonial architecture, lush courtyard gardens, and swimming pool.",
            "meals_info": "Buffet breakfast daily and multi-course South Indian culinary dinners.",
            "transportation_info": "Private AC vehicle for all transfers from Bangalore/Mysore airport and touring.",
            "sightseeing_info": "Mysore Palace, Srirangapatna Fort, Tipu Sultan Summer Palace, Ranganathittu Bird Sanctuary, and St. Philomena's Church.",
            "activities_info": "Boat safari in Ranganathittu bird sanctuary, exploring Tipu Sultan's rocket launching sites, and palace walk.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Flight to Bangalore & Mysore Drive", "Flight arrival in Bangalore from Hyderabad. Scenic drive to Mysore. Check-in heritage hotel. Evening musical fountain at Brindavan Gardens.", "Fortune JP Palace Mysore", "Dinner"),
                (2, "Mysore Palace & St. Philomena's Church", "Comprehensive guided tour of the Golden Throne and Durbar Hall at Mysore Palace. Visit Neo-Gothic St. Philomena's Cathedral.", "Fortune JP Palace Mysore", "Breakfast & Dinner"),
                (3, "Srirangapatna Fort & Ranganathittu Birds", "Excursion to Tipu Sultan's capital Srirangapatna and boat safari among painted storks and crocodiles at Ranganathittu.", "Fortune JP Palace Mysore", "Breakfast & Dinner"),
                (4, "Artisan Markets & Return Flight", "Morning heritage walk through century-old Devaraja market. Return drive to Bangalore airport for Hyderabad flight.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in deluxe heritage room",
                "Daily breakfast and dinner",
                "Dedicated private AC vehicle for all 4 days",
                "Ranganathittu boat safari tickets",
                "All monument entry passes and guide charges"
            ],
            "exclusions": [
                "Airfare tickets Hyderabad - Bangalore - Hyderabad",
                "Lunch meals and personal drinks",
                "Personal tips and driver gratuities",
                "Medical and baggage insurance"
            ]
        },
        {
            "name": "Mysore Luxury Heritage Palace Experience",
            "operator_name": "WanderNest Travels",
            "destination_name": "Mysore",
            "starting_city": "Pune",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("32000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/mysore-luxury-palace-experience",
            "is_active": True,
            "hotel_info": "5-star royal palace hotel built by the Maharaja of Mysore in 1920 set amidst 39 acres of gardens.",
            "meals_info": "Royal champagne breakfast, afternoon tea on palace terrace, and chef-curated royal banquet.",
            "transportation_info": "Chauffeured luxury sedan from Bangalore airport directly to the palace.",
            "sightseeing_info": "Private tour of Mysore Palace royal art galleries, Jaganmohan Palace, and Lalitha Mahal.",
            "activities_info": "Private classical Carnatic veena performance, royal carriage ride, and Ayurvedic rejuvenation massage.",
            "themes": ["luxury", "heritage", "romantic"],
            "travel_types": ["Couple"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Pune to Mysore & Royal Welcome", "Flight to Bangalore from Pune, private luxury car to Lalitha Mahal Palace. Royal garland welcome. Sunset tea on the palace terrace.", "Lalitha Mahal Palace Hotel", "Dinner"),
                (2, "VIP Palace Access & Royal Banquet", "VIP guided visit of Mysore Palace and art museum with palace historian. Evening private candlelit dinner under crystal chandeliers.", "Lalitha Mahal Palace Hotel", "Breakfast & Dinner"),
                (3, "Ayurvedic Spa & Return Transit", "Morning Ayurvedic herbal rejuvenation treatment. Royal breakfast and luxury car return to airport for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in historic Maharaja Suite with royal furnishings",
                "All gourmet meals, afternoon teas, and champagne breakfast",
                "Private luxury car for entire journey from Bangalore",
                "VIP fast-track entries and private historian guide",
                "Ayurvedic wellness therapy session for two"
            ],
            "exclusions": [
                "Airfare Pune - Bangalore - Pune",
                "Cellar wines and spirits",
                "Personal tips and royal staff gratuities",
                "Travel insurance"
            ]
        },

        # =====================================================================
        # 11. PONDICHERRY (Puducherry, India) - 4 Packages (BEACH & CULTURE!)
        # =====================================================================
        {
            "name": "French Quarter Heritage & Promenade Beach Break",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Pondicherry",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("11000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/pondicherry-french-quarter",
            "is_active": True,
            "hotel_info": "French colonial boutique hotel in White Town with bougainvillea courtyards and French cafe.",
            "meals_info": "Daily French continental breakfast (croissants, café au lait) and Franco-Tamil fusion dinners.",
            "transportation_info": "Roundtrip private AC sedan from Bangalore and for all local coastal excursions.",
            "sightseeing_info": "White Town, Promenade Beach, French War Memorial, Sri Aurobindo Ashram, and Paradise Beach.",
            "activities_info": "Heritage walking tour through French Quarter, ferry boat ride to Paradise Beach, and vintage cycle tour.",
            "themes": ["beach", "culture", "heritage"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Bangalore to Pondicherry & Promenade Walk", "Morning drive from Bangalore (6 hrs). Check-in White Town colonial hotel. Sunset stroll along Promenade Beach by the Bay of Bengal.", "Villa Shanti French Heritage Hotel", "Dinner"),
                (2, "White Town French Walk & Paradise Beach", "Morning guided walking tour among pastel yellow villas and Sri Aurobindo Ashram. Afternoon ferry ride to Paradise Beach.", "Villa Shanti French Heritage Hotel", "Breakfast & Dinner"),
                (3, "French Bakeries & Bangalore Return", "Morning breakfast at iconic French bakeries. Souvenir shopping for handmade paper and pottery. Return drive to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in boutique French colonial room in White Town",
                "Daily breakfast and Franco-Tamil specialty dinners",
                "Private dedicated AC car from Bangalore to Bangalore",
                "Paradise Beach ferry boat tickets",
                "All toll taxes, parking, and driver allowances"
            ],
            "exclusions": [
                "Lunch meals and cafe snacking",
                "Watersports fees at Paradise Beach",
                "Personal tips and driver gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Pondicherry Coastal Yoga & Auroville Spiritual Retreat",
            "operator_name": "WanderNest Travels",
            "destination_name": "Pondicherry",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("19000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/pondicherry-coastal-yoga-auroville",
            "is_active": True,
            "hotel_info": "Serene eco-resort nestled near Serenity Beach with beachfront yoga shala and organic gardens.",
            "meals_info": "Healthy organic vegetarian breakfast, herbal tonics, and Mediterranean / Tamil fusion dinners.",
            "transportation_info": "Chennai airport pickup in private AC cab; dedicated car for all touring.",
            "sightseeing_info": "Auroville Matrimandir, Serenity Beach, Aurobindo Ashram, and Goubert Avenue.",
            "activities_info": "Matrimandir meditation viewing, sunrise beach yoga sessions, surfing lessons, and pottery workshop.",
            "themes": ["beach", "spiritual", "culture"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Mumbai to Chennai & Pondicherry Arrival", "Flight to Chennai from Mumbai. Drive along East Coast Road (ECR) to Serenity Beach resort. Evening meditation walk.", "Dune Eco Village & Beach Spa", "Dinner"),
                (2, "Auroville Matrimandir & Organic Farms", "Visit the international township of Auroville and view the golden Matrimandir sphere. Tour sustainable organic farms and bakeries.", "Dune Eco Village & Beach Spa", "Breakfast & Dinner"),
                (3, "Sunrise Yoga & White Town Heritage", "Early sunrise yoga class on Serenity Beach. Afternoon exploration of French Quarter galleries, antique shops, and cafes.", "Dune Eco Village & Beach Spa", "Breakfast & Dinner"),
                (4, "Morning Surf & Chennai Airport Drop", "Morning introductory surf session on waves. Check out and drive along scenic coastal road to Chennai for flight back.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in eco-beach cottage near the sea",
                "Daily organic breakfasts and wholesome dinners",
                "Private dedicated AC car for all transfers and tours",
                "Auroville passes and meditation booking clearances",
                "Daily morning yoga and meditation sessions"
            ],
            "exclusions": [
                "Flights Mumbai - Chennai - Mumbai",
                "Surfboard rental and private surf instructor fees",
                "Personal spa treatments and healing therapies",
                "Personal tips and driver gratuities"
            ]
        },
        {
            "name": "Bohemian French Riviera of the East",
            "operator_name": "RoamRise Tours",
            "destination_name": "Pondicherry",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("15500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/bohemian-french-riviera",
            "is_active": True,
            "hotel_info": "Vibrant boutique hotel near Rock Beach with rooftop plunge pool and bicycle rentals.",
            "meals_info": "Daily breakfast and seaside dining experiences at French bistros and creperies.",
            "transportation_info": "AC sleeper bus / train support to Chennai and private AC transfer to Pondicherry.",
            "sightseeing_info": "Rock Beach, French Quarter, Arikamedu archaeological ruins, and Chunnambar boat house.",
            "activities_info": "Vintage bicycle tours, beach volleyball, kayaking through mangrove backwaters, and cafe hopping.",
            "themes": ["beach", "culture"],
            "travel_types": ["Group", "Solo"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune Arrival & Rock Beach Evening", "Arrival in Pondicherry. Check into boutique hotel. Evening gathering at Rock Beach watching Arabian waves and eating gelato.", "Palais de Mahe Boutique Hotel", "Dinner"),
                (2, "Vintage Bicycle Tour & French Cafes", "Morning cycling tour through Rue Suffren and Rue Dumas. Visit artisan studios, bakeries, and historical churches.", "Palais de Mahe Boutique Hotel", "Breakfast & Dinner"),
                (3, "Chunnambar Mangroves & Paradise Sands", "Boat safari through Chunnambar backwaters to the golden sands of Paradise Beach. Afternoon swimming and sunbathing.", "Palais de Mahe Boutique Hotel", "Breakfast & Dinner"),
                (4, "Arikamedu Ruins & Departure", "Explore ancient Roman trading post ruins at Arikamedu before transfer to Chennai for return transit to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in boutique hotel",
                "Breakfast daily and dinner vouchers at partner bistros",
                "Complimentary bicycle usage throughout stay",
                "Chunnambar boat cruise tickets to Paradise Beach",
                "Private transfer from/to Chennai"
            ],
            "exclusions": [
                "Transit tickets Pune - Chennai - Pune",
                "Lunch meals and extra cafe orders",
                "Watersports rentals",
                "Travel insurance"
            ]
        },
        {
            "name": "Pondicherry Colonial Villa Luxury Beach Holiday",
            "operator_name": "JourneyMint",
            "destination_name": "Pondicherry",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("44000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/pondicherry-colonial-luxury",
            "is_active": True,
            "hotel_info": "5-star 18th-century French governor's residence with private courtyards, plunge pool, and butler.",
            "meals_info": "Daily French champagne breakfast, high tea on the veranda, and 5-course seafood degustation menus.",
            "transportation_info": "Private luxury Audi/BMW from Chennai airport directly to Pondicherry and on disposal.",
            "sightseeing_info": "Private access to French Institute archives, private boat to secluded sandbanks, and Auroville.",
            "activities_info": "Private catamaran cruise on Bay of Bengal, French pastry masterclass, and couples marine clay spa.",
            "themes": ["beach", "luxury", "romantic"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Hyderabad to Chennai & Luxury Coastal Drive", "Flight to Chennai. Private luxury car transfer along coastal East Coast Road. Welcome champagne at French governor's villa.", "La Villa French Quarter Luxury", "Dinner"),
                (2, "White Town Heritage & Private Boat Cruise", "Private guided architectural walking tour. Sunset catamaran cruise with champagne along the Coromandel coast.", "La Villa French Quarter Luxury", "Breakfast & Dinner"),
                (3, "Auroville VIP Access & French Gastronomy", "Exclusive VIP meditation booking at Matrimandir Inner Chamber. 5-course French seafood dinner by visiting master chef.", "La Villa French Quarter Luxury", "Breakfast & Dinner"),
                (4, "Secluded Beach Day & Couples Marine Spa", "Chauffeured trip to private secluded beach cove. Afternoon ocean minerals spa therapy for couples.", "La Villa French Quarter Luxury", "Breakfast & Dinner"),
                (5, "Veranda Breakfast & Chennai Departure", "Leisure breakfast in private courtyard. Luxury chauffeured drive to Chennai airport for flight to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in private luxury suite in restored 18th-century French mansion",
                "All gourmet breakfasts, afternoon teas, and fine dining banquets",
                "Private luxury vehicle with dedicated chauffeur for all days",
                "Private catamaran coastal cruise passes",
                "Couples marine clay spa therapy"
            ],
            "exclusions": [
                "Airfare Hyderabad - Chennai - Hyderabad",
                "Vintage French cellar wines",
                "Personal antique purchases",
                "Gratuities and personal tips"
            ]
        },

        # =====================================================================
        # 12. JIM CORBETT (Uttarakhand, India) - 4 Packages (WILDLIFE!)
        # =====================================================================
        {
            "name": "Jim Corbett Royal Bengal Tiger Jungle Safari",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Jim Corbett",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("12500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/corbett-tiger-safari",
            "is_active": True,
            "hotel_info": "Wilderness eco-lodge bordering the dense sal forests of Corbett with swimming pool and bonfires.",
            "meals_info": "All meals included: buffet breakfast, lunch, and jungle dinner by the bonfire.",
            "transportation_info": "Private AC sedan Delhi - Jim Corbett - Delhi; open 4x4 Maruti Gypsy for jungle safaris.",
            "sightseeing_info": "Bijrani / Dhikala zone, Garjiya Devi Temple, Corbett Waterfall, and Kosi River.",
            "activities_info": "Two open-top 4x4 jeep safaris into tiger reserve core zones, riverbed birdwatching, and wildlife film screening.",
            "themes": ["wildlife", "nature"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4, 5, 6],
            "itinerary": [
                (1, "Delhi to Corbett & Kosi River Walk", "Morning drive from Delhi (5.5 hrs). Check into wilderness lodge. Afternoon nature walk along rocky Kosi riverbed. Evening bonfire.", "Corbett Riverside Jungle Resort", "Lunch & Dinner"),
                (2, "Core Zone Tiger Safari & Garjiya Temple", "Early morning 4x4 open jeep safari in Bijrani/Dhela zone in search of Royal Bengal Tigers and wild elephants. Afternoon visit to sacred Garjiya Temple.", "Corbett Riverside Jungle Resort", "Breakfast, Lunch & Dinner"),
                (3, "Second Morning Safari & Delhi Return", "Dawn safari in Jhirna zone for leopard and bird sightings. Return for breakfast. Check out and drive back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights accommodation in forest resort cottage",
                "All meals included (2 breakfasts, 2 lunches, 2 dinners)",
                "2 open 4x4 jeep safaris with registered naturalist and forest permits",
                "Roundtrip private AC car transfer from Delhi to Delhi",
                "All Corbett Tiger Reserve entry permits and road taxes"
            ],
            "exclusions": [
                "Camera fees inside national park",
                "Personal tips to driver and forest tracker",
                "Alcoholic beverages and personal snacks",
                "Travel insurance"
            ]
        },
        {
            "name": "Corbett Wilderness Trail & Jeep Expedition",
            "operator_name": "Horizon Trails",
            "destination_name": "Jim Corbett",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("22000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/corbett-wilderness-jeep-trail",
            "is_active": True,
            "hotel_info": "Rustic riverside stone cottages located along the Ramganga river in northern Corbett.",
            "meals_info": "All meals included with hearty mountain dishes and live barbecue dinners.",
            "transportation_info": "Delhi airport pickup in private vehicle and open 4x4 Gypsies for all jungle safaris.",
            "sightseeing_info": "Dhikala grasslands, Ramganga reservoir, Marchula suspension bridge, and Corbett Falls.",
            "activities_info": "Three jeep safaris across different zones, gharial crocodile spotting on river, and stargazing.",
            "themes": ["wildlife", "adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Pune to Delhi & Drive to Ramganga", "Flight from Pune to Delhi. Private drive to Corbett northern gate. Check into rustic stone cottages by the Ramganga river.", "Ramganga Forest Camp", "Dinner"),
                (2, "Dhikala Forest Safari & Crocodile Sighting", "Full day safari in Dhikala zone observing wild elephant herds, sambar deer, and gharials in the reservoir.", "Ramganga Forest Camp", "Breakfast, Lunch & Dinner"),
                (3, "Bijrani Morning Safari & Forest Trek", "Morning open jeep safari in Bijrani zone. Afternoon guided walking safari in the buffer forest with naturalist.", "Ramganga Forest Camp", "Breakfast, Lunch & Dinner"),
                (4, "Corbett Falls & Delhi Airport Return", "Morning visit to scenic Corbett Falls in dense teak forests. Return drive to Delhi for evening flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in riverside forest cottages",
                "All meals included throughout the jungle itinerary",
                "3 open 4x4 Gypsy jungle safaris with expert tracker",
                "Private AC vehicle for Delhi airport transfers and tours",
                "Park entry fees and mandatory forest guide charges"
            ],
            "exclusions": [
                "Flights Pune - Delhi - Pune",
                "Binocular and telephoto lens hire",
                "Personal tips and driver allowances",
                "Travel insurance"
            ]
        },
        {
            "name": "Corbett Eco-Lodge Wildlife & Birding Tour",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Jim Corbett",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("27000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/corbett-eco-lodge-birding",
            "is_active": True,
            "hotel_info": "Certified green eco-lodge built with stone and thatch, surrounded by organic orchards and jungle.",
            "meals_info": "Farm-fresh organic buffet meals with Himalayan grain breads and fresh river trout preparations.",
            "transportation_info": "Private dedicated AC Innova from Delhi airport to Corbett and on disposal.",
            "sightseeing_info": "Sitabani landscape, Kosi River, Dhangarhi Museum, and Corbett Heritage Trail.",
            "activities_info": "Bird watching walking safari (over 300 avian species), two jeep safaris, and organic farming experience.",
            "themes": ["wildlife", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Bangalore to Delhi & Corbett Eco-Lodge", "Flight from Bangalore to Delhi. Chauffeur drive to Jim Corbett. Check-in eco-lodge. Orientation bird walk around the lodge grounds.", "Jim's Jungle Retreat Eco Lodge", "Dinner"),
                (2, "Jeep Safari & Wildlife Museum", "Morning 4x4 jeep safari in Dhela zone. Afternoon visit to Dhangarhi Heritage Museum and elephant interpretation center.", "Jim's Jungle Retreat Eco Lodge", "Breakfast, Lunch & Dinner"),
                (3, "Sitabani Birding Trail & Second Safari", "Dawn birding trail spotting great hornbills and kingfishers. Afternoon jeep safari into dense sal forests.", "Jim's Jungle Retreat Eco Lodge", "Breakfast, Lunch & Dinner"),
                (4, "Morning Farm Walk & Delhi Flight", "Morning organic farm walk and fresh fruit breakfast. Drive back to Delhi airport for flight to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in luxury eco-cottage with verandah",
                "All organic meals included",
                "2 jeep safaris with expert ornithologist/naturalist",
                "Private dedicated AC car for all transfers from Delhi",
                "All tiger reserve entry permits and camera fees"
            ],
            "exclusions": [
                "Airfare tickets Bangalore - Delhi - Bangalore",
                "Personal alcoholic beverages and bar orders",
                "Personal tips and driver gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Corbett Luxury Riverside Jungle Resort",
            "operator_name": "TravelVista India",
            "destination_name": "Jim Corbett",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("54000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/corbett-luxury-riverside-resort",
            "is_active": True,
            "hotel_info": "5-star luxury jungle resort on the banks of Kosi river with private pool villas and signature spa.",
            "meals_info": "Gourmet breakfasts, open-air riverside lunches, and candlelit multi-course dinners by the water.",
            "transportation_info": "Private luxury SUV transfers from Delhi airport directly to the resort; private custom Gypsy.",
            "sightseeing_info": "Dhikala / Bijrani premium zones, private river deck, and Corbett heritage estate.",
            "activities_info": "Exclusive private jeep safari with senior wildlife photographer, riverbed dining, and deep-tissue spa.",
            "themes": ["luxury", "wildlife", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Delhi & Luxury Drive to Corbett", "Flight to Delhi from Mumbai. Private luxury SUV transfer to 5-star riverside resort. Sunset cocktail on river deck.", "Taj Corbett Resort & Spa", "Dinner"),
                (2, "Exclusive Tiger Safari & Luxury Spa", "Private morning 4x4 Gypsy safari in prime zone with personal wildlife tracker. Afternoon signature Swedish/Ayurvedic spa treatment.", "Taj Corbett Resort & Spa", "Breakfast, Lunch & Dinner"),
                (3, "Second Safari & Private Riverside Banquet", "Dawn safari tracking tigers and wild elephants. Evening private table set on the pebble riverbed under lantern lights.", "Taj Corbett Resort & Spa", "Breakfast, Lunch & Dinner"),
                (4, "Leisure River Morning & Return Flight", "Champagne breakfast on private villa deck. Luxury transfer back to Delhi airport for flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in luxury river-facing villa with private deck",
                "All gourmet meals, private riverside dinners, and breakfasts",
                "2 private 4x4 jeep safaris with dedicated senior naturalist",
                "Private luxury vehicle Delhi - Corbett - Delhi",
                "One 60-min signature spa therapy session per guest"
            ],
            "exclusions": [
                "Airfare Mumbai - Delhi - Mumbai",
                "Imported cellar wines and spirits",
                "Personal tips and butler gratuities",
                "Comprehensive travel insurance"
            ]
        },

        # =====================================================================
        # 13. MUNNAR (Kerala, India) - 4 Packages (NATURE & MOUNTAIN!)
        # =====================================================================
        {
            "name": "Munnar Misty Tea Hills & Eravikulam Nature Break",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Munnar",
            "starting_city": "Bangalore",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("10500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/munnar-tea-hills-break",
            "is_active": True,
            "hotel_info": "3-star mountain view resort surrounded by tea plantations with private balconies.",
            "meals_info": "Daily buffet breakfast and traditional Kerala dinners (appam, stew, and fish curry).",
            "transportation_info": "Roundtrip private AC car transfer from Kochi airport/station and for local touring.",
            "sightseeing_info": "Eravikulam National Park, Mattupetty Dam, Echo Point, and Tea Museum.",
            "activities_info": "Nilgiri Tahr mountain goat spotting at Rajamalai, boat cruise on Mattupetty Dam, and tea tasting.",
            "themes": ["nature", "mountain"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "itinerary": [
                (1, "Kochi to Munnar & Cheeyappara Falls", "Pick up from Kochi airport/station. Scenic mountain drive past Cheeyappara and Valara waterfalls. Evening tea plantation walk.", "Tea County Resort Munnar", "Dinner"),
                (2, "Eravikulam National Park & Mattupetty", "Morning safari bus inside Eravikulam National Park to view endangered Nilgiri Tahr. Afternoon speedboating at Mattupetty Dam and Echo Point.", "Tea County Resort Munnar", "Breakfast & Dinner"),
                (3, "Tata Tea Museum & Kochi Return", "Morning visit to historic Tata Tea Museum to learn tea processing. Scenic descent and drive back to Kochi for departure.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in deluxe tea-view room in Munnar",
                "Daily breakfast and dinner",
                "Private dedicated AC car for all transfers from Kochi",
                "Eravikulam National Park entry and safari bus passes",
                "All toll charges, parking, and driver allowances"
            ],
            "exclusions": [
                "Transit tickets to and from Kochi",
                "Lunch meals along the highway",
                "Boating charges at Mattupetty dam",
                "Personal tips and driver gratuities"
            ]
        },
        {
            "name": "Munnar Western Ghats Trekking & Waterfalls",
            "operator_name": "Horizon Trails",
            "destination_name": "Munnar",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("16000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/munnar-trekking-waterfalls",
            "is_active": True,
            "hotel_info": "Eco-friendly mountain lodge perched on a cliff edge with private trekking access.",
            "meals_info": "Wholesome mountain breakfasts and hot home-cooked Kerala dinners by the fireplace.",
            "transportation_info": "AC vehicle from Kochi airport to Munnar and local 4x4 jeep for rough mountain trails.",
            "sightseeing_info": "Meesapulimala foothills, Anamudi Shola, Attukal Waterfalls, and Top Station.",
            "activities_info": "Guided ridge trek through high-altitude shola grasslands, waterfall rappelling, and Top Station valley views.",
            "themes": ["nature", "adventure", "mountain"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Pune to Kochi & Munnar Foothills", "Flight from Pune to Kochi. Scenic drive up the Ghats to Munnar. Trek orientation and gear check.", "Camp Footprint Mountain Lodge", "Dinner"),
                (2, "High Ridge Mountain Trek", "Full day guided trek across shola forests and tea estate ridges with packed lunch at mountain peak.", "Camp Footprint Mountain Lodge", "Breakfast & Dinner"),
                (3, "Top Station & Attukal Falls", "Drive through highest tea gardens in India to Top Station overlooking Tamil Nadu plains. Afternoon walk at Attukal waterfalls.", "Camp Footprint Mountain Lodge", "Breakfast & Dinner"),
                (4, "Spice Garden Tour & Kochi Departure", "Morning walk through medicinal spice plantation. Drive down to Kochi airport for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in mountain eco-lodge",
                "Breakfast, trail lunch, and dinners on trekking days",
                "Certified wilderness trekking guide",
                "Private AC vehicle for all transfers from Kochi",
                "All forest permits and entry clearances"
            ],
            "exclusions": [
                "Flights Pune - Kochi - Pune",
                "Personal trekking footwear and apparel",
                "Personal tips to guides and drivers",
                "Travel and adventure sports insurance"
            ]
        },
        {
            "name": "Romantic Munnar Treehouse & Tea Estate Sanctuary",
            "operator_name": "JourneyMint",
            "destination_name": "Munnar",
            "starting_city": "Mumbai",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("42000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/romantic-munnar-treehouse",
            "is_active": True,
            "hotel_info": "5-star luxury treehouse perched 60 feet above the rainforest canopy with private jacuzzi.",
            "meals_info": "Gourmet breakfasts on the treehouse deck, private candlelit waterfall dinners, and tea tastings.",
            "transportation_info": "Private luxury AC SUV from Kochi airport with panoramic sunroof.",
            "sightseeing_info": "Private tea estate trails, Kundala Lake, Lakkom Falls, and Pothamedu Viewpoint.",
            "activities_info": "Private shikara boat ride on Kundala Lake, couples Ayurvedic spice massage, and tea plucking with local harvesters.",
            "themes": ["romantic", "nature", "luxury"],
            "travel_types": ["Couple"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Kochi & Treehouse Check-in", "Flight from Mumbai to Kochi. Chauffeur drive to Munnar. Settle into luxury canopy treehouse with panoramic tea slope views.", "Nature Zone Jungle Resort & Treehouse", "Dinner"),
                (2, "Tea Plucking Experience & Couples Spa", "Morning private stroll through tea bushes with traditional plucking baskets. Afternoon couples Ayurvedic rejuvenation spa.", "Nature Zone Jungle Resort & Treehouse", "Breakfast & Dinner"),
                (3, "Kundala Lake Shikara & Waterfall Picnic", "Private romantic shikara boat cruise on tranquil Kundala Dam. Gourmet picnic lunch beside Lakkom Waterfalls.", "Nature Zone Jungle Resort & Treehouse", "Breakfast & Dinner"),
                (4, "Pothamedu Sunset & Candlelit Dinner", "Sunset photography session at Pothamedu Viewpoint. Private candlelit dinner served on the treehouse deck under stars.", "Nature Zone Jungle Resort & Treehouse", "Breakfast & Dinner"),
                (5, "Morning Bird Chorus & Kochi Flight Return", "Wake up to bird songs and breakfast in the clouds. Scenic transfer to Kochi airport for flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in luxury canopy treehouse suite with jacuzzi",
                "All gourmet breakfasts and candlelit private dinners",
                "Dedicated luxury SUV for all 5 days with chauffeur",
                "Couples signature Ayurvedic spa treatment",
                "Private shikara boat ride on Kundala lake"
            ],
            "exclusions": [
                "Airfare tickets Mumbai - Kochi - Mumbai",
                "Premium champagne and wine orders",
                "Personal tips and driver gratuities",
                "Comprehensive travel insurance"
            ]
        },
        {
            "name": "Munnar Flora & Nilgiri Tahr Wildlife Discovery",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Munnar",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("23000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/munnar-flora-wildlife-discovery",
            "is_active": True,
            "hotel_info": "4-star eco-resort situated near Eravikulam boundary with sprawling botanical gardens.",
            "meals_info": "Daily breakfast and Kerala/South Indian buffet dinners with fresh tropical fruits.",
            "transportation_info": "Private AC vehicle from Kochi airport covering all hill station destinations.",
            "sightseeing_info": "Eravikulam National Park, Rose Garden, Floriculture Centre, and Mattupetty Dam.",
            "activities_info": "Guided wildlife photography tour of Nilgiri Tahr, botanical garden walk, and boating.",
            "themes": ["nature", "wildlife"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Flight to Kochi & Munnar Ascent", "Flight from Hyderabad to Kochi. Scenic drive climbing the Western Ghats to Munnar. Evening botanical garden walk.", "Fragrant Nature Munnar Resort", "Dinner"),
                (2, "Eravikulam National Park Wildlife Trail", "Early morning safari inside Eravikulam National Park spotting herds of Nilgiri Tahr and endemic Western Ghats birds.", "Fragrant Nature Munnar Resort", "Breakfast & Dinner"),
                (3, "Mattupetty Lake & Floriculture Centre", "Visit Floriculture Centre displaying exotic mountain orchids. Afternoon boat ride on Mattupetty Lake.", "Fragrant Nature Munnar Resort", "Breakfast & Dinner"),
                (4, "Tea Museum & Return Flight", "Morning tour of the Tea Museum. Drive down to Kochi airport for flight back to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in deluxe mountain-view room",
                "Daily breakfast and dinner",
                "Private dedicated AC car for all transfers and tours",
                "Eravikulam National Park entry and safari tickets",
                "All toll charges, parking, and driver allowances"
            ],
            "exclusions": [
                "Airfare Hyderabad - Kochi - Hyderabad",
                "Lunch meals along the highway",
                "Camera fees inside national park",
                "Personal tips and driver gratuities"
            ]
        },

        # =====================================================================
        # 14. ADDITIONAL PACKAGES FOR EXISTING DESTINATIONS (Goa, Manali, Jaipur, etc.)
        # =====================================================================
        # Goa (3 new packages - Beach)
        {
            "name": "Goa Budget Beach Party & Watersports",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Goa",
            "starting_city": "Pune",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("8500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/goa-budget-beach-party",
            "is_active": True,
            "hotel_info": "Youthful 3-star beach resort located 200m from Baga Beach with swimming pool.",
            "meals_info": "Daily buffet breakfast and Goan shack dinner voucher.",
            "transportation_info": "AC sleeper bus Pune - Goa - Pune; two-wheeler rental included.",
            "sightseeing_info": "Baga Beach, Calangute Beach, Anjuna flea market, and Chapora Fort.",
            "activities_info": "Parasailing, jet ski, banana boat ride on Baga Beach, and beach shack party nights.",
            "themes": ["beach", "adventure"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Pune Overnight Arrival & Baga Beach", "Arrive in North Goa by morning sleeper bus. Hotel check-in. Afternoon on Baga Beach. Evening sunset at iconic Curlies in Anjuna.", "Baga Marina Beach Resort", "Dinner"),
                (2, "Watersports Combo & Chapora Fort Sunset", "Full morning 5-in-1 watersports package at Calangute Beach (parasailing, jet ski, banana ride, bumper ride). Sunset at Dil Chahta Hai Chapora Fort.", "Baga Marina Beach Resort", "Breakfast & Dinner"),
                (3, "Flea Market & Evening Bus Return", "Morning shopping at Tibetan market and beach shacks. Check out and board evening AC sleeper bus back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights accommodation near Baga Beach",
                "Daily breakfast and beach shack dinner",
                "Roundtrip AC sleeper bus tickets from Pune",
                "5-in-1 watersports combo pass at Calangute",
                "Two-wheeler rental for 2 days with helmets"
            ],
            "exclusions": [
                "Fuel for rented two-wheeler",
                "Lunch meals and alcoholic drinks at clubs",
                "Club entry fees (Tito's / Mambo's)",
                "Personal tips and baggage porterage"
            ]
        },
        {
            "name": "Romantic South Goa Sunset Beach Villa",
            "operator_name": "JourneyMint",
            "destination_name": "Goa",
            "starting_city": "Delhi",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("42000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/romantic-south-goa-villa",
            "is_active": True,
            "hotel_info": "5-star boutique beachfront villa on quiet Varca Beach with private beach cabanas.",
            "meals_info": "Daily champagne breakfast and candlelit 4-course seafood dinners on the sand.",
            "transportation_info": "Private chauffeured luxury sedan for all airport transfers and private touring.",
            "sightseeing_info": "Varca Beach, Palolem Beach, Cabo de Rama fort, and historic churches of Chandor.",
            "activities_info": "Private sunset catamaran sailing, couple's Ayurvedic massage, and candlelit beach picnic.",
            "themes": ["beach", "romantic", "luxury"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Delhi Flight Arrival & Varca Villa Welcome", "Flight to Goa from Delhi. Chauffeur transfer to luxury beachfront resort in South Goa. Sunset champagne in private beach cabana.", "The Zuri White Sands Resort & Casino", "Dinner"),
                (2, "Catamaran Sailing & Palolem Beach", "Morning private catamaran sail with dolphin watching. Afternoon drive to crescent-shaped Palolem Beach and silent disco evening.", "The Zuri White Sands Resort & Casino", "Breakfast & Dinner"),
                (3, "Cabo de Rama Fort & Candlelit Beach Feast", "Scenic drive to ancient clifftop Cabo de Rama fort overlooking the sea. Evening private candlelit 5-course lobster banquet on the sand.", "The Zuri White Sands Resort & Casino", "Breakfast & Dinner"),
                (4, "Morning Beach Walk & Delhi Return", "Morning beach stroll and leisurely breakfast by the pool. Private transfer to Goa airport for return flight to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in luxury beachfront villa suite",
                "Daily champagne breakfast and candlelit dinners",
                "Private dedicated luxury AC car for all 4 days",
                "Private sunset catamaran charter cruise",
                "Couples signature wellness massage"
            ],
            "exclusions": [
                "Airfare Delhi - Goa - Delhi",
                "Vintage wines and casino chips",
                "Personal tips and driver gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Goa Family Coastal Heritage & Dolphin Safari",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Goa",
            "starting_city": "Hyderabad",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("24000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/goa-family-coastal-heritage",
            "is_active": True,
            "hotel_info": "4-star family resort in Candolim with children's pool, water slides, and garden lawns.",
            "meals_info": "Daily buffet breakfast and multi-cuisine dinners with live music.",
            "transportation_info": "Private AC Innova on disposal for all transfers and family sightseeing.",
            "sightseeing_info": "Fort Aguada, Basilica of Bom Jesus, Old Goa churches, Miramar Beach, and Dudhsagar Waterfalls.",
            "activities_info": "Morning boat dolphin safari, spice plantation tour with traditional lunch, and Dudhsagar jeep safari.",
            "themes": ["beach", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Hyderabad to Goa Flight & Candolim Welcome", "Flight to Goa from Hyderabad. Private transfer to family resort in Candolim. Evening relax on Candolim beach.", "Novotel Goa Candolim", "Dinner"),
                (2, "Fort Aguada & Dolphin Spotting Boat", "Early morning boat safari to spot wild Indo-Pacific dolphins. Visit 17th-century Portuguese Fort Aguada and lighthouse.", "Novotel Goa Candolim", "Breakfast & Dinner"),
                (3, "Old Goa UNESCO Churches & Spice Plantation", "Tour the Basilica of Bom Jesus housing relics of St. Francis Xavier. Afternoon guided spice farm tour with buffet lunch on banana leaf.", "Novotel Goa Candolim", "Breakfast, Lunch & Dinner"),
                (4, "Dudhsagar Waterfalls Jeep Safari", "Full day 4x4 jeep safari through Mollem National Park to the roaring Dudhsagar waterfalls with swimming in natural pool.", "Novotel Goa Candolim", "Breakfast & Dinner"),
                (5, "Souvenirs & Hyderabad Departure", "Morning souvenir shopping for cashews and feni. Transfer to Goa airport for return flight to Hyderabad.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in deluxe family room",
                "Daily breakfast, one buffet lunch, and dinners",
                "Private dedicated AC Innova throughout",
                "Dolphin boat safari tickets and Dudhsagar jeep permits",
                "Spice plantation entry and traditional buffet fees"
            ],
            "exclusions": [
                "Airfare Hyderabad - Goa - Hyderabad",
                "Personal water sports activities",
                "Life jacket rental at Dudhsagar pool",
                "Personal tips and driver gratuities"
            ]
        },

        # Manali (3 new packages - Adventure, Romantic, Nature)
        {
            "name": "Manali Rohtang Pass Snow Adventure",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Manali",
            "starting_city": "Pune",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("21000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/manali-rohtang-snow-adventure",
            "is_active": True,
            "hotel_info": "3-star mountain alpine resort in Aleo with snow-capped valley views.",
            "meals_info": "Daily buffet breakfast and warm Himachali dinners with live tandoor.",
            "transportation_info": "Delhi transit connection and private AC vehicle for mountain sightseeing.",
            "sightseeing_info": "Rohtang Pass (13,058 ft), Solang Valley, Gulaba, and Kothi village.",
            "activities_info": "Snow scooter riding, skiing on Rohtang slopes, paragliding at Solang, and snow trekking.",
            "themes": ["adventure", "mountain"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [11, 12, 1, 2, 3, 4, 5, 6],
            "itinerary": [
                (1, "Pune to Delhi & Overnight Volvo to Manali", "Flight from Pune to Delhi. Board evening AC Volvo bus to Manali through mountain highway.", "Overnight AC Volvo", "None"),
                (2, "Manali Arrival & Solang Valley Action", "Morning check-in resort. Afternoon paragliding and zorbing at Solang Valley. Evening stroll on Mall Road.", "Honeymoon Inn Alpine Resort", "Dinner"),
                (3, "Rohtang Pass High Altitude Snow Day", "Full day excursion to Rohtang Pass (13,058 ft) for skiing, snow scootering, and panoramic Himalayan glacier views.", "Honeymoon Inn Alpine Resort", "Breakfast & Dinner"),
                (4, "Jogini Waterfalls & Vashisht Hot Springs", "Morning trek to Jogini Waterfalls through pine forests. Soak in natural sulfur hot springs at Vashisht.", "Honeymoon Inn Alpine Resort", "Breakfast & Dinner"),
                (5, "Old Manali Cafes & Return Transit", "Morning cafe hopping in Old Manali. Board evening Volvo back to Delhi for return flight to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in deluxe mountain-view room (plus 1 night Volvo transit)",
                "Daily breakfast and dinner at resort",
                "Roundtrip AC Volvo tickets Delhi - Manali - Delhi",
                "Private dedicated cab for Rohtang Pass and Solang Valley",
                "Rohtang Pass NGT permits and green cess fees"
            ],
            "exclusions": [
                "Airfare Pune - Delhi - Pune",
                "Snow suit and snow boot rental fees",
                "Skiing and snow scooter activity charges",
                "Personal tips and driver gratuities"
            ]
        },
        {
            "name": "Manali Valley Romantic Honeymoon Escape",
            "operator_name": "WanderNest Travels",
            "destination_name": "Manali",
            "starting_city": "Delhi",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("32000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/manali-romantic-honeymoon",
            "is_active": True,
            "hotel_info": "4-star luxury wooden chalet resort with private jacuzzi and apple orchard views.",
            "meals_info": "Daily breakfast, afternoon tea, and candlelit dinners with complimentary honeymoon cake.",
            "transportation_info": "Private dedicated AC sedan Delhi - Manali - Delhi with experienced hill driver.",
            "sightseeing_info": "Hadimba Temple, Naggar Castle, Solang Valley, Jana Waterfall, and Kasol valley.",
            "activities_info": "Candlelit dinner in apple orchard, cable car ride at Solang, and day excursion to scenic Parvati Valley.",
            "themes": ["romantic", "mountain", "nature"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Delhi to Manali Scenic Drive", "Morning private sedan pickup from Delhi. Scenic drive along Beas river. Evening check-in at luxury wooden chalet.", "The Orchard Greens Resort & Spa", "Dinner"),
                (2, "Hadimba Temple & Solang Snow Valley", "Visit 500-year-old Hadimba wooden temple. Afternoon scenic cable car ride at Solang Valley.", "The Orchard Greens Resort & Spa", "Breakfast & Dinner"),
                (3, "Naggar Castle & Heritage Art Gallery", "Scenic drive to medieval Naggar Castle and Nicholas Roerich Russian art estate. Evening couples dinner.", "The Orchard Greens Resort & Spa", "Breakfast & Dinner"),
                (4, "Kasol & Parvati Valley Day Excursion", "Full day romantic excursion to bohemian Kasol and Manikaran hot springs in the scenic Parvati valley.", "The Orchard Greens Resort & Spa", "Breakfast & Dinner"),
                (5, "Orchard Stroll & Candlelit Dinner", "Day at leisure enjoying in-room jacuzzi and apple orchard walk. Special 4-course candlelit dinner with cake.", "The Orchard Greens Resort & Spa", "Breakfast & Dinner"),
                (6, "Mall Road Shopping & Delhi Return", "Morning purchase of Kullu shawls and honey. Drive back to Delhi for evening drop-off.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in luxury honeymoon chalet with jacuzzi",
                "Daily buffet breakfast and candlelit dinners",
                "Honeymoon special: flower bed decoration and celebration cake",
                "Private dedicated AC car from Delhi to Delhi",
                "All toll taxes, parking, and driver allowances"
            ],
            "exclusions": [
                "Adventure sports activity passes",
                "Lunch meals along the highway",
                "Personal tips and driver gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Manali Family Apple Valley Tour",
            "operator_name": "TravelVista India",
            "destination_name": "Manali",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("28000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/manali-family-apple-valley",
            "is_active": True,
            "hotel_info": "Family-friendly 4-star mountain resort with games room, bonfire lawn, and family suites.",
            "meals_info": "Buffet breakfast and multi-cuisine family dinners daily.",
            "transportation_info": "Chandigarh/Delhi airport pickup in private AC Innova on disposal throughout.",
            "sightseeing_info": "Atal Tunnel, Sissu waterfalls, Manali Mall Road, Club House, and Vashisht Village.",
            "activities_info": "River crossing at Club House, exploring Lahaul valley via Atal Tunnel, and apple picking.",
            "themes": ["nature", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [4, 5, 6, 7, 10, 11, 12, 1],
            "itinerary": [
                (1, "Mumbai to Chandigarh & Manali Scenic Drive", "Flight to Chandigarh from Mumbai. Private Innova transfer up the mountains to Manali. Evening check-in resort.", "Manuallaya The Resort Spa in the Himalayas", "Dinner"),
                (2, "Manali Sightseeing & Club House", "Morning visit to Hadimba temple and Club House for family games and river crossing. Afternoon Mall Road walk.", "Manuallaya The Resort Spa in the Himalayas", "Breakfast & Dinner"),
                (3, "Atal Tunnel & Sissu Lahaul Valley", "Drive through the 9km engineering wonder Atal Tunnel into Lahaul Valley to witness Sissu waterfalls.", "Manuallaya The Resort Spa in the Himalayas", "Breakfast & Dinner"),
                (4, "Solang Valley Family Adventure", "Full day at Solang Valley for ropeway ride, zorbing, and panoramic mountain vistas.", "Manuallaya The Resort Spa in the Himalayas", "Breakfast & Dinner"),
                (5, "Naggar Art Village & Local Craft Center", "Visit Naggar Castle and local Himalayan handloom weavers cooperative for authentic Kullu shawls.", "Manuallaya The Resort Spa in the Himalayas", "Breakfast & Dinner"),
                (6, "Descent to Chandigarh & Flight Home", "Early morning scenic drive back to Chandigarh airport for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in family deluxe valley suite",
                "Daily breakfast and dinner",
                "Private dedicated AC Innova vehicle for all 6 days",
                "Atal Tunnel and Solang Valley excursion permits",
                "All toll charges, parking, and driver allowances"
            ],
            "exclusions": [
                "Airfare tickets Mumbai - Chandigarh - Mumbai",
                "Lunch meals and personal snack purchases",
                "Activity tickets at Club House and Solang",
                "Personal tips and driver gratuities"
            ]
        },

        # Jaipur (2 new packages - Heritage, Culture)
        {
            "name": "Jaipur Royal Haveli Heritage Weekend",
            "operator_name": "WanderNest Travels",
            "destination_name": "Jaipur",
            "starting_city": "Pune",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("14000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/jaipur-royal-haveli-weekend",
            "is_active": True,
            "hotel_info": "Restored 19th-century royal haveli in the Pink City with frescoed walls and courtyard pool.",
            "meals_info": "Daily royal breakfast and authentic Rajasthani dinners (dal baati churma and laal maas).",
            "transportation_info": "Private dedicated AC car for airport pickup and all Pink City tours.",
            "sightseeing_info": "Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, and Jal Mahal.",
            "activities_info": "Elephant/jeep ride up to Amber Fort, sound and light show, and gemstone market walk.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune to Jaipur & City Palace Welcome", "Flight from Pune to Jaipur. Heritage haveli check-in with traditional garland. Afternoon visit to City Palace and Jantar Mantar observatory.", "Alsisar Haveli Heritage Hotel", "Dinner"),
                (2, "Amber Fort & Jal Mahal Photo Stop", "Morning jeep ascent to majestic Amber Fort. Photo stop at Jal Mahal water palace. Afternoon Hawa Mahal facade tour.", "Alsisar Haveli Heritage Hotel", "Breakfast & Dinner"),
                (3, "Bazaars & Pune Return Flight", "Morning shopping for blue pottery, block-printed textiles at Johari Bazaar. Transfer to airport for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in authentic heritage haveli deluxe room",
                "Daily breakfast and traditional Rajasthani dinner",
                "Private dedicated AC sedan throughout",
                "Composite entry passes to all Jaipur heritage monuments",
                "Government licensed heritage guide"
            ],
            "exclusions": [
                "Airfare Pune - Jaipur - Pune",
                "Lunch meals and street food",
                "Personal shopping expenses",
                "Travel insurance"
            ]
        },
        {
            "name": "Pink City Arts, Bazaars & Folk Culture Trail",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Jaipur",
            "starting_city": "Hyderabad",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("17500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/pink-city-arts-bazaars",
            "is_active": True,
            "hotel_info": "4-star modern boutique hotel near MI Road with rooftop restaurant and cultural terrace.",
            "meals_info": "Buffet breakfast daily and dinners at Chokhi Dhani ethnic village and local specialty dhabas.",
            "transportation_info": "Private AC vehicle on disposal for airport pickup, city touring, and Chokhi Dhani.",
            "sightseeing_info": "Nahargarh Fort, Albert Hall Museum, Jaigarh Fort, Hawa Mahal, and Chokhi Dhani.",
            "activities_info": "Block printing workshop in Sanganer village, sunset over Pink City from Nahargarh, and folk dance night at Chokhi Dhani.",
            "themes": ["culture", "heritage"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Hyderabad Arrival & Albert Hall Museum", "Flight to Jaipur from Hyderabad. Check-in hotel. Afternoon visit to Indo-Saracenic Albert Hall Museum. Evening illuminated view of Hawa Mahal.", "Shahpura House Heritage Hotel", "Dinner"),
                (2, "Nahargarh Fort & Sanganer Print Workshop", "Morning visit to Nahargarh and Jaigarh forts (world's largest cannon on wheels). Afternoon hands-on block printing workshop in Sanganer.", "Shahpura House Heritage Hotel", "Breakfast & Dinner"),
                (3, "Amber Fort & Chokhi Dhani Cultural Village", "Guided tour of Amber Fort's Sheesh Mahal mirror palace. Evening full cultural immersion with camel rides and folk dance at Chokhi Dhani.", "Shahpura House Heritage Hotel", "Breakfast & Dinner"),
                (4, "Bapu Bazaar & Hyderabad Departure", "Morning walk through colorful Bapu Bazaar for lac bangles and mojari leather shoes. Transfer to Jaipur airport for flight home.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in boutique heritage room",
                "Daily breakfast and dinner (including Chokhi Dhani royal entry and dining)",
                "Private dedicated AC car for all 4 days",
                "Block printing workshop material fees",
                "All monument entry passes and city taxes"
            ],
            "exclusions": [
                "Flights Hyderabad - Jaipur - Hyderabad",
                "Lunch meals and street food",
                "Personal shopping expenses",
                "Travel insurance"
            ]
        },

        # Kerala (2 new packages - Wildlife, Beach)
        {
            "name": "Wayanad Wildlife & Spice Plantation Safari",
            "operator_name": "RoamRise Tours",
            "destination_name": "Kerala",
            "starting_city": "Bangalore",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("18000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/wayanad-wildlife-spice-safari",
            "is_active": True,
            "hotel_info": "Eco-resort nestled in the rainforest buffer of Wayanad Wildlife Sanctuary.",
            "meals_info": "All meals included: authentic Malabar breakfast, Kerala banana-leaf lunch, and barbecue dinner.",
            "transportation_info": "Private dedicated AC Innova Bangalore - Wayanad - Bangalore and open jeep for safari.",
            "sightseeing_info": "Wayanad Wildlife Sanctuary, Edakkal Caves, Banasura Sagar Dam, and Soochipara Waterfalls.",
            "activities_info": "Muthanga jungle jeep safari for wild elephant sightings, prehistoric Edakkal rock art trek, and bamboo rafting.",
            "themes": ["wildlife", "nature"],
            "travel_types": ["Family", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Bangalore to Wayanad Rainforest Drive", "Morning pickup in Bangalore. Drive through Bandipur/Muthanga forest to Wayanad. Check-in eco-resort. Evening spice garden walk.", "Vythiri Village Resort Wayanad", "Lunch & Dinner"),
                (2, "Muthanga Wildlife Safari & Edakkal Caves", "Dawn jeep safari in Muthanga Wildlife Sanctuary spotting wild elephant herds and bison. Afternoon hike up to Neolithic Edakkal Caves.", "Vythiri Village Resort Wayanad", "Breakfast, Lunch & Dinner"),
                (3, "Banasura Dam & Soochipara Waterfalls", "Visit Banasura Sagar earth dam with speedboating. Trek through tea estates to Soochipara waterfalls with freshwater dip.", "Vythiri Village Resort Wayanad", "Breakfast, Lunch & Dinner"),
                (4, "Tea Factory Walk & Bangalore Return", "Morning tour of traditional tea processing factory. Check out and drive back to Bangalore.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation in rainforest resort cottage",
                "All meals included (breakfast, lunch, and dinner)",
                "Muthanga Wildlife Sanctuary jeep safari and permits",
                "Private dedicated AC vehicle from Bangalore to Bangalore",
                "Edakkal Caves and Banasura Dam entry tickets"
            ],
            "exclusions": [
                "Speedboat fees at Banasura dam",
                "Camera fees at monuments and sanctuary",
                "Personal tips and driver gratuities",
                "Travel insurance"
            ]
        },
        {
            "name": "Kerala Backwater Houseboat & Marari Beach Tour",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Kerala",
            "starting_city": "Mumbai",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("32000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/kerala-houseboat-marari-beach",
            "is_active": True,
            "hotel_info": "Traditional air-conditioned private luxury houseboat in Alleppey (1N) and 4-star beach resort on Marari Beach (3N).",
            "meals_info": "Full board on houseboat with Karimeen pollichathu; daily breakfast and coastal dinners at beach resort.",
            "transportation_info": "Private dedicated AC sedan from Kochi airport covering backwaters and beaches.",
            "sightseeing_info": "Alleppey backwaters, Vembanad Lake, Marari Beach, and Fort Kochi heritage district.",
            "activities_info": "Overnight private houseboat cruise, beachcombing on quiet Marari sands, village canoe ride, and Kathakali show.",
            "themes": ["beach", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Flight to Kochi & Alleppey Houseboat Cruise", "Flight from Mumbai to Kochi. Private transfer to Alleppey. Board private luxury houseboat. Cruise through narrow backwater canals.", "Private AC Deluxe Houseboat", "Lunch & Dinner"),
                (2, "Houseboat Sunrise & Transfer to Marari Beach", "Morning cruise past paddy fields. Disembark and transfer to serene beachfront resort on Marari Beach. Afternoon relaxation.", "Marari Beach Resort CGH Earth", "Breakfast & Dinner"),
                (3, "Marari Beach Day & Village Bicycle Tour", "Morning village bicycle tour through fishing hamlets. Afternoon swimming in the warm Arabian sea and sunset beach stroll.", "Marari Beach Resort CGH Earth", "Breakfast & Dinner"),
                (4, "Fort Kochi Heritage Excursion", "Day excursion to Fort Kochi to see Chinese Fishing Nets, St. Francis Church, and Jewish Synagogue in Mattancherry.", "Marari Beach Resort CGH Earth", "Breakfast & Dinner"),
                (5, "Morning Dip & Kochi Airport Departure", "Morning swim in the ocean. Check out and transfer to Kochi airport for flight back to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "1 night on private exclusive AC houseboat with captain and private chef",
                "3 nights in luxury garden cottage at Marari Beach resort",
                "All meals on houseboat; breakfast and dinner at beach resort",
                "Private dedicated AC car for all transfers and excursions",
                "Fort Kochi heritage tour entry passes"
            ],
            "exclusions": [
                "Airfare tickets Mumbai - Kochi - Mumbai",
                "Ayurvedic massage charges at beach resort",
                "Personal beverage orders and alcoholic drinks",
                "Travel insurance"
            ]
        },

        # Kashmir (3 new packages - Nature, Adventure, Luxury)
        {
            "name": "Kashmir Valley of Flowers & Gulmarg Gondola",
            "operator_name": "BlueSky Journeys",
            "destination_name": "Kashmir",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("46000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://bluesky-demo.example.com/packages/kashmir-gulmarg-gondola",
            "is_active": True,
            "hotel_info": "4-star alpine hotel in Gulmarg (2N) and cedarwood luxury houseboat on Dal Lake (3N).",
            "meals_info": "Daily buffet breakfast and authentic Kashmiri wazwan dinners with hot kahwa tea.",
            "transportation_info": "Private dedicated AC Innova vehicle for all Srinagar, Gulmarg, and Pahalgam travel.",
            "sightseeing_info": "Dal Lake, Gulmarg meadow of flowers, Apharwat Peak, Mughal Gardens (Shalimar & Nishat), and Betaab Valley.",
            "activities_info": "Gulmarg Gondola cable car ride to Phase 2 (14,000 ft), shikara ride on Dal Lake, and pony trek in Pahalgam.",
            "themes": ["nature", "mountain"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Mumbai to Srinagar & Dal Lake Shikara", "Flight arrival from Mumbai. Check into traditional carved cedarwood houseboat. Sunset shikara cruise through floating vegetable gardens.", "Mascot Luxury Dal Lake Houseboat", "Dinner"),
                (2, "Mughal Gardens & Shankaracharya Temple", "Visit Nishat Bagh, Shalimar Bagh, and hilltop Shankaracharya Temple offering panoramic views over Srinagar city.", "Mascot Luxury Dal Lake Houseboat", "Breakfast & Dinner"),
                (3, "Drive to Gulmarg & Gondola Cable Car", "Scenic drive to alpine resort town of Gulmarg. Ascend via Gulmarg Gondola to Phase 1 and Phase 2 (Apharwat Peak) snowline.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (4, "Gulmarg Meadow Walk & Golf Course", "Morning walk through pine forests and historical St. Mary's church. Afternoon leisurely stroll around high-altitude golf course.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (5, "Pahalgam Valley of Shepherds Day-Trip", "Full day excursion to picturesque Pahalgam along the Lidder river. Visit scenic Betaab Valley and Aru Valley.", "Mascot Luxury Dal Lake Houseboat", "Breakfast & Dinner"),
                (6, "Floating Flower Market & Mumbai Return", "Early dawn shikara ride to the floating flower market. Check out and transfer to Srinagar airport for flight home.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights accommodation (3N luxury houseboat, 2N Gulmarg alpine resort)",
                "Daily breakfast and traditional Kashmiri dinners",
                "Phase 1 & Phase 2 Gulmarg Gondola tickets",
                "Dedicated private AC vehicle for all transfers and sightseeing",
                "Two private shikara rides on Dal Lake"
            ],
            "exclusions": [
                "Airfare Mumbai - Srinagar - Mumbai",
                "Pony rides and local union cab fees in Pahalgam/Gulmarg",
                "Personal tips to shikara boatmen and drivers",
                "Travel insurance"
            ]
        },
        {
            "name": "Srinagar Houseboat & Pahalgam Adventure Trek",
            "operator_name": "Horizon Trails",
            "destination_name": "Kashmir",
            "starting_city": "Delhi",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("31000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/srinagar-pahalgam-adventure",
            "is_active": True,
            "hotel_info": "Deluxe houseboat on Nigeen Lake (2N) and riverside alpine cottages in Pahalgam (3N).",
            "meals_info": "Hearty breakfast and dinner spreads daily with local trout and mutton specialties.",
            "transportation_info": "Private AC vehicle for all airport transfers and mountain valleys.",
            "sightseeing_info": "Nigeen Lake, Aru Valley, Baisaran valley (Mini Switzerland), Chandanwari, and Lidder river.",
            "activities_info": "Day trek from Aru to Lidderwat, river rafting on Lidder river, and horse riding in Baisaran meadows.",
            "themes": ["adventure", "nature"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Delhi to Srinagar & Nigeen Lake Houseboat", "Flight from Delhi to Srinagar. Transfer to serene Nigeen Lake. Sunset shikara cruise in peaceful lotus waters.", "Nigeen Lake Heritage Houseboat", "Dinner"),
                (2, "Srinagar to Pahalgam Valley Drive", "Scenic drive through saffron fields of Pampore along the rushing Lidder river to Pahalgam. Check-in riverside lodge.", "Pahalgam Riverside Mountain Lodge", "Breakfast & Dinner"),
                (3, "Baisaran Meadow Trek & Horseback Trail", "Trek through dense pine forests to the stunning high-altitude alpine meadow of Baisaran (Mini Switzerland).", "Pahalgam Riverside Mountain Lodge", "Breakfast & Dinner"),
                (4, "Aru Valley & River Rafting Excursion", "Explore unspoiled Aru village. Afternoon white-water rafting on the thrilling rapids of Lidder river.", "Pahalgam Riverside Mountain Lodge", "Breakfast & Dinner"),
                (5, "Chandanwari Snow Bridge & Srinagar Return", "Visit Chandanwari gorge. Drive back to Srinagar. Evening shopping for carved walnut wood and saffron in Lal Chowk.", "Nigeen Lake Heritage Houseboat", "Breakfast & Dinner"),
                (6, "Srinagar Airport Drop to Delhi", "Transfer to Srinagar airport for return flight back to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights accommodation in deluxe houseboat and riverside lodge",
                "Daily breakfast and dinner throughout",
                "Private dedicated AC vehicle for the entire itinerary",
                "Lidder river rafting experience pass",
                "Shikara boat ride on Nigeen Lake"
            ],
            "exclusions": [
                "Flights Delhi - Srinagar - Delhi",
                "Pony rental charges in Baisaran",
                "Lunch meals along the highway",
                "Travel and adventure insurance"
            ]
        },
        {
            "name": "Grand Kashmir Luxury Winter Wonderland",
            "operator_name": "JourneyMint",
            "destination_name": "Kashmir",
            "starting_city": "Pune",
            "duration_days": 7,
            "duration_nights": 6,
            "price_per_person": Decimal("76000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/kashmir-luxury-winter-wonderland",
            "is_active": True,
            "hotel_info": "5-star luxury heated ski resort in Gulmarg (3N) and ultra-luxury royal suite houseboat (3N).",
            "meals_info": "All meals: champagne breakfasts, wazwan royal feasts, hot chocolate tastings, and fine dining.",
            "transportation_info": "Private luxury 4x4 Fortuner / Prado with snow chains and dedicated mountain chauffeur.",
            "sightseeing_info": "Gulmarg ski slopes, Apharwat Peak, Dal Lake private channels, and snowy Dachigam sanctuary.",
            "activities_info": "Private ski instructor sessions on powdery snow, heated shikara cruise with warm blankets, and private Wazwan feast.",
            "themes": ["luxury", "romantic", "mountain"],
            "travel_types": ["Couple"],
            "availability_months": [11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune to Srinagar & Royal Houseboat Welcome", "Flight to Srinagar. VIP reception with hot saffron kahwa. Check into heated luxury houseboat suite on Dal Lake.", "Sukhoon Luxury Houseboat", "Dinner"),
                (2, "Winter Dal Lake & Mughal Snow Architecture", "Heated private shikara ride. Visit snow-dusted Shalimar and Nishat Mughal gardens.", "Sukhoon Luxury Houseboat", "Breakfast & Dinner"),
                (3, "Scenic Drive to Snowy Gulmarg Paradise", "Luxury 4x4 drive through snow-covered pine forests to Gulmarg. Check into 5-star ski resort with indoor heated pool.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (4, "Gondola Phase 2 & Private Ski Lesson", "Ascend through clouds on Gondola Phase 2 to 14,000 ft. Private 2-hour skiing session with personal ski instructor.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (5, "Snowmobile Safari & Mountain Spa", "Snowmobile ride across the snowy golf course. Afternoon couples hot stone massage at L'Occitane spa.", "The Khyber Himalayan Resort & Spa", "Breakfast & Dinner"),
                (6, "Srinagar Return & Royal 36-Course Wazwan", "Scenic descent to Srinagar. Evening bespoke royal 36-course Wazwan banquet served on copper trami plates.", "Sukhoon Luxury Houseboat", "Breakfast & Dinner"),
                (7, "Srinagar Airport VIP Departure", "Private luxury 4x4 transfer to Srinagar airport for return flight to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "6 nights in 5-star luxury heated accommodations",
                "All gourmet breakfasts and multi-course Wazwan banquets",
                "Private luxury 4x4 vehicle with snow chains for all 7 days",
                "Both phases of Gulmarg Gondola with fast-track entry",
                "Couples signature wellness spa treatment"
            ],
            "exclusions": [
                "Airfare tickets Pune - Srinagar - Pune",
                "Ski equipment rental fees",
                "Private cellar alcoholic selections",
                "Personal tips and butler gratuities"
            ]
        },

        # Rishikesh (2 new packages - Adventure, Spiritual)
        {
            "name": "Rishikesh White Water Rafting & Cliff Jump Weekend",
            "operator_name": "ExploreSphere Tours",
            "destination_name": "Rishikesh",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("8200.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://exploresphere-demo.example.com/packages/rishikesh-rafting-cliff-jump",
            "is_active": True,
            "hotel_info": "Riverside alpine tent camp in Shivpuri with sandy beach volleyball court and swimming pool.",
            "meals_info": "All meals included: buffet breakfast, lunch, and riverside barbecue dinner with bonfire.",
            "transportation_info": "Roundtrip AC bus/cab from Delhi to Rishikesh and rafting transfer jeeps.",
            "sightseeing_info": "Shivpuri rapids, Marine Drive, Lakshman Jhula, and Triveni Ghat.",
            "activities_info": "26km Grade III/IV white-water river rafting from Marine Drive, cliff jumping from 25 feet, and body surfing.",
            "themes": ["adventure"],
            "travel_types": ["Group", "Solo"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4, 5, 6],
            "itinerary": [
                (1, "Delhi to Rishikesh & Camp Check-in", "Morning departure from Delhi (5 hrs). Check into riverside camp in Shivpuri. Afternoon beach volleyball and evening musical bonfire.", "Camp AquaForest Riverside Camp", "Lunch & Dinner"),
                (2, "26km White Water Rafting & Cliff Jumping", "Thrilling 26km river rafting expedition tackling 'Three Blind Mice', 'Roller Coaster', and 'Golf Course' rapids with cliff jumping.", "Camp AquaForest Riverside Camp", "Breakfast, Lunch & Dinner"),
                (3, "Triveni Ghat Aarti & Delhi Return", "Morning nature walk to Neer Garh waterfall. Visit sacred Triveni Ghat before returning to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "2 nights in premium riverside Swiss camp with attached washroom",
                "All meals included (2 breakfasts, 2 lunches, 2 dinners)",
                "26km river rafting with certified river guide, lifejackets, and helmets",
                "Roundtrip AC transport from Delhi to Delhi",
                "Campfire activities and cliff jumping gear"
            ],
            "exclusions": [
                "Bungee jumping charges at Mohan Chatti (optional)",
                "Personal snacks and cold drinks",
                "Personal tips to rafting guides",
                "Travel insurance"
            ]
        },
        {
            "name": "Sacred Ganga Yoga & Spiritual Detox Camp",
            "operator_name": "RoamRise Tours",
            "destination_name": "Rishikesh",
            "starting_city": "Pune",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("21000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://roamrise-demo.example.com/packages/rishikesh-spiritual-yoga-camp",
            "is_active": True,
            "hotel_info": "Tranquil wellness ashram resort in Tapovan overlooking the emerald green Ganges river.",
            "meals_info": "Pure vegetarian satvik meals, Ayurvedic detox teas, and fresh cold-pressed fruit juices daily.",
            "transportation_info": "Dehradun airport pickup in private AC cab; walking and cab tours in Rishikesh.",
            "sightseeing_info": "Parmarth Niketan, Beatles Ashram (Chaurasi Kutia), Vashistha Cave, and Ram Jhula.",
            "activities_info": "Daily sunrise Hatha yoga, guided pranayama and meditation, evening Parmarth Ganga Aarti, and Vashistha cave meditation.",
            "themes": ["spiritual", "nature"],
            "travel_types": ["Solo", "Couple"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4, 5],
            "itinerary": [
                (1, "Pune to Dehradun & Rishikesh Ashram Welcome", "Flight to Dehradun. Chauffeur transfer to Tapovan ashram resort. Evening welcoming herb tea and introductory meditation.", "Aloha on the Ganges Spiritual Resort", "Dinner"),
                (2, "Sunrise Yoga & Parmarth Ganga Aarti", "Dawn Hatha yoga on open yoga deck overlooking Ganges. Afternoon visit to Beatles Ashram. Evening prayer chanting at Parmarth Niketan.", "Aloha on the Ganges Spiritual Resort", "Breakfast & Dinner"),
                (3, "Vashistha Cave Deep Meditation", "Drive along the mountain river to sacred Vashistha meditation cave. Silent meditation by the pristine riverbank.", "Aloha on the Ganges Spiritual Resort", "Breakfast & Dinner"),
                (4, "Ayurvedic Detox & Sound Healing", "Morning pranayama breathwork masterclass. Afternoon Tibetan sound bowl healing and Ayurvedic massage session.", "Aloha on the Ganges Spiritual Resort", "Breakfast & Dinner"),
                (5, "Dawn Chants & Dehradun Departure", "Final dawn meditation ceremony. Satvik breakfast and transfer to Dehradun airport for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights accommodation in spiritual river-view room",
                "Daily satvik vegetarian breakfast and dinner",
                "Daily morning yoga and evening meditation sessions",
                "Private AC vehicle for all transfers and excursions",
                "Sound healing and Ayurvedic massage session"
            ],
            "exclusions": [
                "Airfare Pune - Dehradun - Pune",
                "Entry fee at Beatles Ashram",
                "Personal tips and ashram donations",
                "Travel insurance"
            ]
        },

        # Andaman (2 new packages - Heritage, Romantic Beach)
        {
            "name": "Port Blair & Ross Island Historical Odyssey",
            "operator_name": "WanderNest Travels",
            "destination_name": "Andaman",
            "starting_city": "Delhi",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("32000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/andaman-port-blair-ross-island",
            "is_active": True,
            "hotel_info": "4-star oceanfront hotel in Port Blair with swimming pool and panoramic harbor views.",
            "meals_info": "Buffet breakfast daily and coastal multi-cuisine dinners.",
            "transportation_info": "Private dedicated AC car for all tours and high-speed ferry boat to islands.",
            "sightseeing_info": "Cellular Jail National Memorial, Ross Island (Netaji Subhash Chandra Bose Island), North Bay, and Corbyn's Cove Beach.",
            "activities_info": "Cellular Jail Sound and Light Show, deer spotting among British colonial ruins on Ross Island, and sea walk at North Bay.",
            "themes": ["heritage", "beach"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Delhi to Port Blair & Cellular Jail Light Show", "Flight from Delhi to Port Blair. Check into oceanfront hotel. Evening visit to Cellular Jail National Memorial and Sound & Light show.", "Sinclairs Bayview Port Blair", "Dinner"),
                (2, "Ross Island Colonial Ruins & North Bay Coral", "Ferry boat to Ross Island exploring ruined British barracks, church, and bakery. Boat to North Bay for coral viewing.", "Sinclairs Bayview Port Blair", "Breakfast & Dinner"),
                (3, "Chidiya Tapu Sunset & Marine Museum", "Morning visit to Samudrika Naval Marine Museum and Anthropological Museum. Sunset drive to Chidiya Tapu bird island.", "Sinclairs Bayview Port Blair", "Breakfast & Dinner"),
                (4, "Corbyn's Cove Beach & Shopping", "Relaxing morning at Corbyn's Cove coconut-palm beach. Afternoon shopping for pearl jewelry and shell crafts at Sagarika emporium.", "Sinclairs Bayview Port Blair", "Breakfast & Dinner"),
                (5, "Port Blair Airport Departure to Delhi", "Check out after breakfast. Transfer to Port Blair airport for return flight to Delhi.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in ocean-facing deluxe room in Port Blair",
                "Daily breakfast and dinner",
                "Private dedicated AC vehicle for all transfers and city tours",
                "Ferry tickets to Ross Island and North Bay Island",
                "Cellular Jail entry and Sound & Light show tickets"
            ],
            "exclusions": [
                "Airfare Delhi - Port Blair - Delhi",
                "Sea walk and scuba diving charges at North Bay",
                "Lunch meals and personal refreshments",
                "Travel insurance"
            ]
        },
        {
            "name": "Andaman Tropical Romance & Snorkeling Haven",
            "operator_name": "JourneyMint",
            "destination_name": "Andaman",
            "starting_city": "Mumbai",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("56000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://journeymint-demo.example.com/packages/andaman-tropical-romance",
            "is_active": True,
            "hotel_info": "5-star luxury beachfront villa on Havelock Island with private plunge pool and direct beach access.",
            "meals_info": "Daily champagne breakfast, beachside candlelight dinner, and seafood banquets.",
            "transportation_info": "Private Makruzz / Nautika luxury cruise transfers between Port Blair and Havelock.",
            "sightseeing_info": "Radhanagar Beach (Asia's best beach), Elephant Beach, Kalapathar Beach, and Vijaynagar Beach.",
            "activities_info": "Private couples snorkeling safari, sunset candlelit dinner on white sand, and night kayak bioluminescence tour.",
            "themes": ["beach", "romantic", "nature"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Port Blair & Luxury Cruise to Havelock", "Flight from Mumbai to Port Blair. Executive class catamaran cruise to Havelock Island. Settle into private pool beach villa.", "Taj Exotica Resort & Spa Havelock", "Dinner"),
                (2, "Radhanagar Beach Sunset & Tropical Relaxation", "Day at leisure on the powder-white sands of Radhanagar Beach. Spectacular crimson sunset over the Bay of Bengal.", "Taj Exotica Resort & Spa Havelock", "Breakfast & Dinner"),
                (3, "Elephant Beach Coral Reef Snorkeling", "Private speed boat to Elephant Beach. Guided couples snorkeling session over vibrant coral reefs with clownfish.", "Taj Exotica Resort & Spa Havelock", "Breakfast & Dinner"),
                (4, "Kalapathar Turquoise Coast & Private Dinner", "Scenic drive to Kalapathar Beach with black volcanic rocks and turquoise water. Evening private 4-course candlelit beach dinner.", "Taj Exotica Resort & Spa Havelock", "Breakfast & Dinner"),
                (5, "Catamaran Back to Port Blair", "Morning luxury cruise back to Port Blair. Afternoon spa treatment and sunset walk along Marina Park.", "Welcomhotel by ITC Hotels Port Blair", "Breakfast & Dinner"),
                (6, "Port Blair Airport Drop to Mumbai", "Breakfast at hotel. Private transfer to Port Blair airport for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in 5-star beachfront pool villa in Havelock + 1 night Port Blair",
                "Daily breakfast and candlelit specialty dinners",
                "Luxury catamaran cruise tickets (Makruzz Royal/Premium class)",
                "Private dedicated AC car on disposal on both islands",
                "Guided snorkeling session with underwater photos"
            ],
            "exclusions": [
                "Airfare tickets Mumbai - Port Blair - Mumbai",
                "Scuba diving certification add-ons",
                "Cellar wine and premium spirits",
                "Personal tips and driver gratuities"
            ]
        },

        # Jaisalmer (1 new package - Adventure, Culture)
        {
            "name": "Thar Desert Camel Safari & Sam Dune Glamping",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Jaisalmer",
            "starting_city": "Pune",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("16000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/thar-desert-glamping",
            "is_active": True,
            "hotel_info": "Desert luxury Swiss tents in Sam Sand Dunes (2N) and yellow sandstone haveli inside Jaisalmer Fort (1N).",
            "meals_info": "All meals in desert camp: buffet breakfast, traditional Rajasthani thali, and live campfire buffet.",
            "transportation_info": "Jodhpur / Jaisalmer train or cab connection and private AC vehicle for all tours.",
            "sightseeing_info": "Jaisalmer Golden Fort, Patwon Ki Haveli, Gadisar Lake, Kuldhara ghost village, and Sam Sand Dunes.",
            "activities_info": "Sunset camel safari across rolling dunes, 4x4 dune bashing, Kalbelia folk dance by the fire, and stargazing.",
            "themes": ["adventure", "culture"],
            "travel_types": ["Group", "Solo"],
            "availability_months": [10, 11, 12, 1, 2, 3],
            "itinerary": [
                (1, "Pune to Jaisalmer & Golden Fort Walk", "Arrival in Jaisalmer. Check into sandstone heritage haveli. Afternoon exploration of living Jaisalmer Fort and Jain temples.", "Hotel Pleasant Haveli Jaisalmer", "Dinner"),
                (2, "Patwon Ki Haveli & Sam Dunes Camp", "Tour exquisite carved stone balconies at Patwon Ki Haveli. Drive to Sam Sand Dunes. Sunset camel safari and evening Kalbelia folk dance.", "Royal Desert Camp Sam Dunes", "Breakfast & Dinner"),
                (3, "4x4 Dune Bashing & Kuldhara Ghost Village", "Morning thrilling 4x4 jeep dune bashing. Afternoon excursion to the eerie abandoned ghost village of Kuldhara.", "Royal Desert Camp Sam Dunes", "Breakfast & Dinner"),
                (4, "Gadisar Lake Sunrise & Departure", "Early sunrise walk at sacred Gadisar Lake. Check out and transfer for return transit to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights accommodation (1N heritage haveli, 2N luxury Swiss desert tent)",
                "Daily breakfast and dinner (including cultural camp buffets)",
                "Sunset camel safari on dunes and evening Kalbelia dance show",
                "Private dedicated AC car for all transfers and touring",
                "All monument entry passes and desert permits"
            ],
            "exclusions": [
                "Transit tickets Pune - Jaisalmer - Pune",
                "4x4 dune bashing jeep fee (optional add-on)",
                "Lunch meals and personal drinks",
                "Travel insurance"
            ]
        },

        # Gangtok (1 new package - Mountain, Nature)
        {
            "name": "Tsomgo Lake & Nathula Pass Mountain Explorer",
            "operator_name": "TrailMosaic Holidays",
            "destination_name": "Gangtok",
            "starting_city": "Mumbai",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("28000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://trailmosaic-demo.example.com/packages/gangtok-tsomgo-nathula",
            "is_active": True,
            "hotel_info": "4-star mountain view resort on ridge in Gangtok with panoramic vistas of Kanchenjunga.",
            "meals_info": "Daily buffet breakfast and dinners featuring Sikkimese and Tibetan specialties.",
            "transportation_info": "Dedicated AC Innova for Bagdogra airport transfers and high-altitude 4x4 permit vehicle.",
            "sightseeing_info": "Tsomgo Glacial Lake, Baba Mandir, Nathula Pass (Indo-China border), Rumtek Monastery, and MG Marg.",
            "activities_info": "High-altitude yak ride at frozen Tsomgo Lake, visiting international border at Nathula Pass, and cable car ride.",
            "themes": ["mountain", "nature"],
            "travel_types": ["Couple", "Family"],
            "availability_months": [3, 4, 5, 6, 9, 10, 11, 12],
            "itinerary": [
                (1, "Mumbai to Bagdogra & Gangtok Ascent", "Flight to Bagdogra from Mumbai. Scenic 4.5 hr drive alongside Teesta river to Gangtok. Evening walk on pedestrian MG Marg.", "The Elgin Nor-Khill Gangtok", "Dinner"),
                (2, "Tsomgo Lake & Baba Mandir High Pass Tour", "Full day excursion to frozen alpine Tsomgo Lake (12,400 ft) and sacred Baba Mandir near the Indo-China border.", "The Elgin Nor-Khill Gangtok", "Breakfast & Dinner"),
                (3, "Rumtek Monastery & Enchey Gompa", "Visit the grand Dharma Chakra Centre at Rumtek Monastery, Namgyal Institute of Tibetology, and flower exhibition centre.", "The Elgin Nor-Khill Gangtok", "Breakfast & Dinner"),
                (4, "Banjhakri Falls & Tashi Viewpoint", "Morning panoramic sunrise view of Kanchenjunga from Tashi Viewpoint. Afternoon visit to Banjhakri waterfalls and ropeway ride.", "The Elgin Nor-Khill Gangtok", "Breakfast & Dinner"),
                (5, "Descent to Bagdogra & Flight Return", "Morning drive down to Bagdogra airport for afternoon flight back to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in deluxe mountain-view room in Gangtok",
                "Daily breakfast and dinner",
                "Dedicated private vehicle for all transfers and sightseeing",
                "Tsomgo Lake and Baba Mandir restricted area permits",
                "All toll charges, parking, and driver allowances"
            ],
            "exclusions": [
                "Airfare Mumbai - Bagdogra - Mumbai",
                "Nathula Pass special permit surcharge (subject to military clearance)",
                "Yak ride charges at lake",
                "Personal tips and driver gratuities"
            ]
        },

        # Meghalaya (1 new package - Adventure, Nature)
        {
            "name": "Cherrapunji Waterfalls & Caving Adventure",
            "operator_name": "Horizon Trails",
            "destination_name": "Meghalaya",
            "starting_city": "Pune",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("27500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/meghalaya-waterfalls-caving",
            "is_active": True,
            "hotel_info": "Cozy pine valley eco-cottages in Shillong and cliffside resort in Cherrapunji overlooking Bangladesh plains.",
            "meals_info": "Daily hearty breakfast and dinner spreads with authentic Khasi organic preparations.",
            "transportation_info": "Private dedicated AC Innova Guwahati - Shillong - Cherrapunji - Guwahati.",
            "sightseeing_info": "Nohkalikai Falls, Mawsmai Cave, Arwah Cave, Wei Sawdong three-tier falls, and Dawki river.",
            "activities_info": "Speleology caving with helmets and headlamps in limestone caves, trekking to plunging waterfalls, and cliff jumping.",
            "themes": ["adventure", "nature"],
            "travel_types": ["Solo", "Group"],
            "availability_months": [9, 10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Pune to Guwahati & Umiam Lake Drive", "Flight from Pune to Guwahati. Scenic drive into Meghalaya hills with stop at Umiam Lake. Check-in Shillong.", "Polo Towers Hotel Shillong", "Dinner"),
                (2, "Shillong to Cherrapunji Waterfalls", "Drive to Cherrapunji (Sohra). Marvel at Nohkalikai Falls (India's tallest plunge waterfall) and seven sister falls.", "Polo Orchid Resort Cherrapunji", "Breakfast & Dinner"),
                (3, "Limestone Caving & Wei Sawdong Hike", "Explore prehistoric fossils inside Arwah Cave and Mawsmai Cave with headlamps. Afternoon trek down to turquoise Wei Sawdong falls.", "Polo Orchid Resort Cherrapunji", "Breakfast & Dinner"),
                (4, "Dawki Crystal River & Mawlynnong", "Visit the world-famous crystal-clear Umngot River in Dawki for transparent boating. Visit Mawlynnong (Asia's cleanest village).", "Polo Orchid Resort Cherrapunji", "Breakfast & Dinner"),
                (5, "Laitlum Canyons & Shillong Night", "Morning hike around the dramatic precipice of Laitlum Grand Canyon. Evening stroll at Police Bazar in Shillong.", "Polo Towers Hotel Shillong", "Breakfast & Dinner"),
                (6, "Guwahati Airport Drop for Flight", "Drive down to Guwahati airport with stop at Kamakhya temple. Flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights accommodation (2N Shillong, 3N Cherrapunji)",
                "Daily breakfast and dinner throughout",
                "Private dedicated AC Innova vehicle for all 6 days",
                "Cave exploration gear and local Khasi guide",
                "All entry permits and parking charges"
            ],
            "exclusions": [
                "Airfare Pune - Guwahati - Pune",
                "Boating fees at Dawki river",
                "Lunch meals along the highway",
                "Travel and adventure insurance"
            ]
        },

        # Dubai (2 new active packages - Luxury, Culture, Romantic)
        {
            "name": "Dubai Glitz, Burj Khalifa & Desert Safari",
            "operator_name": "TripCraft Holidays",
            "destination_name": "Dubai",
            "starting_city": "Mumbai",
            "duration_days": 5,
            "duration_nights": 4,
            "price_per_person": Decimal("62000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://tripcraft-demo.example.com/packages/dubai-glitz-burj-safari",
            "is_active": True,
            "hotel_info": "4-star luxury hotel in Downtown Dubai with rooftop swimming pool and view of city skyline.",
            "meals_info": "Daily international buffet breakfast, desert safari barbecue buffet, and Marina Dhow cruise dinner.",
            "transportation_info": "Private AC airport transfers and 4x4 Land Cruiser for desert dune safari.",
            "sightseeing_info": "Burj Khalifa 124th floor observatory, Dubai Mall, Dubai Marina, Museum of the Future, and Miracle Garden.",
            "activities_info": "Observation deck viewing from Burj Khalifa, 4x4 red dune bashing, camel riding, and belly dance show.",
            "themes": ["luxury", "culture"],
            "travel_types": ["Family", "Group"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Mumbai to Dubai & Marina Dhow Cruise", "Flight from Mumbai to Dubai. Private airport transfer. Evening luxury glass-enclosed Dhow cruise with dinner along Dubai Marina.", "Rove Downtown Dubai", "Dinner"),
                (2, "Burj Khalifa Observatory & Dubai Mall", "Ascend to the 124th floor observation deck of Burj Khalifa. Watch the Dubai Fountain show and explore the Dubai Mall.", "Rove Downtown Dubai", "Breakfast & Dinner"),
                (3, "Museum of the Future & 4x4 Desert Safari", "Morning visit to the architectural marvel Museum of the Future. Afternoon 4x4 red dune safari with sandboarding and barbecue dinner.", "Rove Downtown Dubai", "Breakfast & Dinner"),
                (4, "Miracle Garden & Old Dubai Souks", "Visit Dubai Miracle Garden (150 million blooming flowers). Afternoon abra boat ride across Dubai Creek to Gold & Spice Souks.", "Rove Downtown Dubai", "Breakfast & Dinner"),
                (5, "Duty Free Shopping & Return Flight", "Leisure morning for shopping. Transfer to Dubai International Airport for return flight to Mumbai.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "4 nights in deluxe 4-star room in Downtown Dubai",
                "Daily buffet breakfast and 2 specialty dinners",
                "Burj Khalifa 124th floor non-prime entry ticket",
                "4x4 Desert Safari with barbecue buffet dinner and shows",
                "Dubai Marina Dhow Cruise dinner tickets"
            ],
            "exclusions": [
                "International flights Mumbai - Dubai - Mumbai",
                "UAE tourist visa and medical insurance",
                "Tourism Dirham fee paid directly at hotel check-in",
                "Personal shopping and souvenirs"
            ]
        },
        {
            "name": "Dubai Marina & Palm Jumeirah Luxury Break",
            "operator_name": "TravelVista India",
            "destination_name": "Dubai",
            "starting_city": "Delhi",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("74000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://travelvista-demo.example.com/packages/dubai-marina-palm-luxury",
            "is_active": True,
            "hotel_info": "5-star luxury beachfront resort on Palm Jumeirah with private beach and infinity pools.",
            "meals_info": "Full American champagne breakfast daily and fine dining vouchers at celebrity chef restaurants.",
            "transportation_info": "Private luxury Mercedes/BMW airport transfers and private chauffeur on disposal.",
            "sightseeing_info": "The View at The Palm, Atlantis Aquaventure, Dubai Marina Yacht Club, and Ain Dubai.",
            "activities_info": "Private yacht charter cruise around Palm Jumeirah, Aquaventure waterpark thrill slides, and rooftop lounge evenings.",
            "themes": ["luxury", "romantic"],
            "travel_types": ["Couple"],
            "availability_months": [10, 11, 12, 1, 2, 3, 4],
            "itinerary": [
                (1, "Delhi Flight Arrival & Palm Jumeirah Check-in", "Flight arrival from Delhi. Luxury chauffeur transfer to Palm Jumeirah 5-star beachfront resort. Evening sunset cocktails on private beach.", "Atlantis The Palm Dubai", "Dinner"),
                (2, "Private Yacht Cruise & The View at The Palm", "Private 2-hour luxury yacht charter around Palm Jumeirah and Burj Al Arab. Sunset views from The View at The Palm observation deck.", "Atlantis The Palm Dubai", "Breakfast & Dinner"),
                (3, "Aquaventure Waterpark & Fine Dining", "VIP fast-track access to Aquaventure Waterpark and Lost Chambers Aquarium. Romantic dinner at Gordon Ramsay's Bread Street Kitchen.", "Atlantis The Palm Dubai", "Breakfast & Dinner"),
                (4, "Luxury Spa & Delhi Airport Return", "Morning couple's massage at ShuiQi Spa. Leisurely champagne breakfast before private luxury transfer to airport for flight home.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "3 nights in ocean-view luxury room at Atlantis The Palm",
                "Daily breakfast and multi-course gourmet dinners",
                "Private 2-hour luxury yacht charter cruise with refreshments",
                "Unlimited VIP access to Aquaventure Waterpark and Aquarium",
                "Private luxury vehicle airport transfers"
            ],
            "exclusions": [
                "Flights Delhi - Dubai - Delhi",
                "UAE tourist visa charges",
                "Tourism Dirham fee per night",
                "Personal tips and butler gratuities"
            ]
        },

        # Bali (1 new package - Culture, Nature)
        {
            "name": "Bali Culture, Temples & Ubud Monkey Forest",
            "operator_name": "WanderNest Travels",
            "destination_name": "Bali",
            "starting_city": "Pune",
            "duration_days": 6,
            "duration_nights": 5,
            "price_per_person": Decimal("49000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://wandernest-demo.example.com/packages/bali-culture-ubud",
            "is_active": True,
            "hotel_info": "4-star Balinese resort nestled amidst Ubud tropical rainforest with ravine infinity pool.",
            "meals_info": "Daily buffet breakfast and authentic Balinese dinners (Nasi Goreng, Satay, and seafood).",
            "transportation_info": "Private dedicated AC car with English-speaking Balinese driver for all days.",
            "sightseeing_info": "Sacred Monkey Forest Sanctuary, Tegallalang Rice Terraces, Tirta Empul water temple, and Tanah Lot sea temple.",
            "activities_info": "Purification bath at Tirta Empul, giant jungle swing at rice terraces, and sunset Kecak fire dance at Uluwatu.",
            "themes": ["culture", "nature"],
            "travel_types": ["Family", "Group"],
            "availability_months": [4, 5, 6, 7, 8, 9, 10],
            "itinerary": [
                (1, "Pune to Denpasar & Ubud Rainforest Welcome", "Flight to Bali via Kuala Lumpur. Warm flower garland welcome at Denpasar airport. Transfer to Ubud rainforest resort.", "Alaya Resort Ubud", "Dinner"),
                (2, "Monkey Forest & Tegallalang Rice Terraces", "Morning walk through sacred Ubud Monkey Forest sanctuary. Afternoon visit to emerald Tegallalang rice terraces with giant swing.", "Alaya Resort Ubud", "Breakfast & Dinner"),
                (3, "Tirta Empul Holy Water & Kintamani Volcano", "Participate in holy spring water cleansing ritual at Tirta Empul. Panoramic lunch view of Mount Batur active volcano.", "Alaya Resort Ubud", "Breakfast & Dinner"),
                (4, "Uluwatu Clifftop Temple & Kecak Fire Dance", "Drive down to southern cliffs of Uluwatu. Watch sunset Kecak fire dance performed on cliff edge over the Indian Ocean.", "Alaya Resort Ubud", "Breakfast & Dinner"),
                (5, "Tanah Lot Sunset Sea Temple", "Morning artisan shopping at Ubud Art Market. Late afternoon excursion to the famous offshore rock temple of Tanah Lot.", "Alaya Resort Ubud", "Breakfast & Dinner"),
                (6, "Denpasar Airport Departure to Pune", "Morning tropical fruit breakfast by the pool. Private transfer to Denpasar airport for flight back to Pune.", "Onward Transit", "Breakfast"),
            ],
            "inclusions": [
                "5 nights in deluxe Balinese garden suite in Ubud",
                "Daily breakfast and dinner throughout",
                "Private dedicated AC vehicle with Balinese driver-guide",
                "All temple entry tickets, sarong rentals, and Kecak dance passes",
                "Airport pick-up and drop-off in Denpasar"
            ],
            "exclusions": [
                "International flights Pune - Denpasar - Pune",
                "Indonesia Visa on Arrival fee ($35 USD) and tourist tax",
                "Jungle swing ticket surcharge",
                "Personal tips and driver gratuities"
            ]
        },

        # =====================================================================
        # 15. INACTIVE DEMO PACKAGES (For testing active-package constraint)
        # =====================================================================
        {
            "name": "Monsoon Off-Season Coastal Trek (Discontinued)",
            "operator_name": "Horizon Trails",
            "destination_name": "Goa",
            "starting_city": "Mumbai",
            "duration_days": 4,
            "duration_nights": 3,
            "price_per_person": Decimal("9000.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://horizontrails-demo.example.com/packages/monsoon-coastal-discontinued",
            "is_active": False,  # INACTIVE TEST PACKAGE
            "hotel_info": "Budget coastal lodge (currently closed for seasonal repairs).",
            "meals_info": "Daily breakfast.",
            "transportation_info": "Shared bus.",
            "sightseeing_info": "Coastal cliffs.",
            "activities_info": "Off-season hiking.",
            "themes": ["beach", "adventure"],
            "travel_types": ["Solo"],
            "availability_months": [7, 8],
            "itinerary": [
                (1, "Day 1", "Discontinued package itinerary day 1.", "Lodge", "None"),
                (2, "Day 2", "Discontinued package itinerary day 2.", "Lodge", "None"),
                (3, "Day 3", "Discontinued package itinerary day 3.", "Lodge", "None"),
                (4, "Day 4", "Discontinued package itinerary day 4.", "None", "None"),
            ],
            "inclusions": ["Accommodation"],
            "exclusions": ["Everything else"]
        },
        {
            "name": "Old Delhi Heritage Walk - Season Closed (Discontinued)",
            "operator_name": "GlobeNest Travels",
            "destination_name": "Agra",
            "starting_city": "Delhi",
            "duration_days": 3,
            "duration_nights": 2,
            "price_per_person": Decimal("7500.00"),
            "featured_image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
            "source_url": "https://globenest-demo.example.com/packages/old-delhi-discontinued",
            "is_active": False,  # INACTIVE TEST PACKAGE
            "hotel_info": "Heritage inn (seasonal closure).",
            "meals_info": "Daily breakfast.",
            "transportation_info": "Local rickshaw.",
            "sightseeing_info": "Heritage alleyways.",
            "activities_info": "Walking tour.",
            "themes": ["heritage", "culture"],
            "travel_types": ["Group"],
            "availability_months": [5, 6],
            "itinerary": [
                (1, "Day 1", "Discontinued package itinerary day 1.", "Inn", "None"),
                (2, "Day 2", "Discontinued package itinerary day 2.", "Inn", "None"),
                (3, "Day 3", "Discontinued package itinerary day 3.", "None", "None"),
            ],
            "inclusions": ["Accommodation"],
            "exclusions": ["Everything else"]
        },
    ]
