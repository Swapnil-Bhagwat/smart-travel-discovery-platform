from datetime import datetime
from app.extensions import db

# Junction Table: Package <-> Theme
package_themes = db.Table(
    'package_themes',
    db.Column('package_id', db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), primary_key=True),
    db.Column('theme_id', db.Integer, db.ForeignKey('themes.id', ondelete='CASCADE'), primary_key=True),
    db.Index('idx_package_themes_theme_id', 'theme_id')
)


class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    # Foreign keys with ON DELETE RESTRICT
    operator_id = db.Column(db.Integer, db.ForeignKey('operators.id', ondelete='RESTRICT'), nullable=False, index=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id', ondelete='RESTRICT'), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    starting_city = db.Column(db.String(100), nullable=False, index=True)
    duration_days = db.Column(db.SmallInteger, nullable=False, index=True)
    duration_nights = db.Column(db.SmallInteger, nullable=False)
    price_per_person = db.Column(db.Numeric(10, 2), nullable=False, index=True)
    featured_image_url = db.Column(db.String(500), nullable=True)
    source_url = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Detailed fields for display & comparison (NOT search filters)
    hotel_info = db.Column(db.Text, nullable=True)
    meals_info = db.Column(db.Text, nullable=True)
    transportation_info = db.Column(db.Text, nullable=True)
    sightseeing_info = db.Column(db.Text, nullable=True)
    activities_info = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Data integrity constraints
    __table_args__ = (
        db.CheckConstraint('duration_days > 0', name='ck_packages_duration_days_positive'),
        db.CheckConstraint('duration_nights >= 0', name='ck_packages_duration_nights_non_negative'),
        db.CheckConstraint('price_per_person >= 0', name='ck_packages_price_non_negative'),
    )

    # Relationships
    operator = db.relationship('Operator', back_populates='packages')
    destination = db.relationship('Destination', back_populates='packages')
    themes = db.relationship('Theme', secondary=package_themes, back_populates='packages')
    travel_types = db.relationship('PackageTravelType', back_populates='package', cascade='all, delete-orphan')
    availability_months = db.relationship('PackageAvailabilityMonth', back_populates='package', cascade='all, delete-orphan')
    itineraries = db.relationship('PackageItinerary', back_populates='package', cascade='all, delete-orphan', order_by='PackageItinerary.day_number')
    inclusions = db.relationship('PackageInclusion', back_populates='package', cascade='all, delete-orphan')
    exclusions = db.relationship('PackageExclusion', back_populates='package', cascade='all, delete-orphan')

    def to_summary_dict(
        self,
        requested_travellers=1,
        match_score=None,
        budget_status='within_budget',
        budget_difference=0.0,
        match_reasons=None,
        mismatches=None
    ):
        total_cost = round(float(self.price_per_person) * requested_travellers, 2)
        summary = {
            'id': self.id,
            'name': self.name,
            'operator': {
                'id': self.operator.id,
                'name': self.operator.name,
                'rating': float(self.operator.rating) if self.operator and self.operator.rating is not None else 0.0,
            } if self.operator else None,
            'destination': {
                'id': self.destination.id,
                'name': self.destination.name,
                'country': self.destination.country,
                'region': self.destination.region,
            } if self.destination else None,
            'starting_city': self.starting_city,
            'duration_days': self.duration_days,
            'duration_nights': self.duration_nights,
            'price_per_person': float(self.price_per_person),
            'requested_travellers': requested_travellers,
            'estimated_total_cost': total_cost,
            'themes': [
                {'id': t.id, 'name': t.name, 'slug': t.slug}
                for t in self.themes
            ],
            'travel_types': [tt.travel_type for tt in self.travel_types],
            'available_months': sorted([m.month for m in self.availability_months]),
            'featured_image_url': self.featured_image_url,
            'source_url': self.source_url,
            'match_score': match_score if match_score is not None else 100,
            'budget_status': budget_status,
            'budget_difference': float(budget_difference),
            'provider': 'demo',
            'source_type': 'demo',
        }
        if match_reasons is not None:
            summary['match_reasons'] = match_reasons
        if mismatches is not None:
            summary['mismatches'] = mismatches
        return summary

    def to_detail_dict(self, requested_travellers=1, match_score=None, budget_status='within_budget', budget_difference=0.0):
        summary = self.to_summary_dict(
            requested_travellers=requested_travellers,
            match_score=match_score,
            budget_status=budget_status,
            budget_difference=budget_difference
        )
        summary.update({
            'is_active': self.is_active,
            'hotel_info': self.hotel_info,
            'meals_info': self.meals_info,
            'transportation_info': self.transportation_info,
            'sightseeing_info': self.sightseeing_info,
            'activities_info': self.activities_info,
            'itinerary': [
                {
                    'id': it.id,
                    'day_number': it.day_number,
                    'title': it.title,
                    'description': it.description,
                    'accommodation': it.accommodation,
                    'meals_provided': it.meals_provided,
                }
                for it in self.itineraries
            ],
            'inclusions': [inc.description for inc in self.inclusions],
            'exclusions': [exc.description for exc in self.exclusions],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        })
        return summary

    def __repr__(self):
        return f"<Package {self.id}: {self.name}>"


class PackageTravelType(db.Model):
    __tablename__ = 'package_travel_types'

    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), primary_key=True)
    travel_type = db.Column(db.Enum('Solo', 'Couple', 'Family', 'Group', name='travel_type_enum'), primary_key=True, index=True)

    package = db.relationship('Package', back_populates='travel_types')

    def __repr__(self):
        return f"<PackageTravelType {self.package_id}: {self.travel_type}>"


class PackageAvailabilityMonth(db.Model):
    __tablename__ = 'package_availability_months'

    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), primary_key=True)
    month = db.Column(db.SmallInteger, primary_key=True, index=True)

    # Data integrity constraint: Month must be between 1 and 12
    __table_args__ = (
        db.CheckConstraint('month >= 1 AND month <= 12', name='ck_availability_month_range'),
    )

    package = db.relationship('Package', back_populates='availability_months')

    def __repr__(self):
        return f"<PackageAvailabilityMonth {self.package_id}: month={self.month}>"


class PackageItinerary(db.Model):
    __tablename__ = 'package_itineraries'

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), nullable=False, index=True)
    day_number = db.Column(db.SmallInteger, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    accommodation = db.Column(db.String(255), nullable=True)
    meals_provided = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('package_id', 'day_number', name='uq_package_itinerary_day'),
    )

    package = db.relationship('Package', back_populates='itineraries')

    def __repr__(self):
        return f"<PackageItinerary {self.package_id}: Day {self.day_number} - {self.title}>"


class PackageInclusion(db.Model):
    __tablename__ = 'package_inclusions'

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), nullable=False, index=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    package = db.relationship('Package', back_populates='inclusions')

    def __repr__(self):
        return f"<PackageInclusion {self.id}: pkg={self.package_id}>"


class PackageExclusion(db.Model):
    __tablename__ = 'package_exclusions'

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), nullable=False, index=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    package = db.relationship('Package', back_populates='exclusions')

    def __repr__(self):
        return f"<PackageExclusion {self.id}: pkg={self.package_id}>"
