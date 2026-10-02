from datetime import datetime
from app.extensions import db


class Operator(db.Model):
    __tablename__ = 'operators'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    website_url = db.Column(db.String(255), nullable=True)
    contact_email = db.Column(db.String(150), nullable=True)
    contact_phone = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Numeric(2, 1), default=0.0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships - Operator cannot be deleted if active packages exist (RESTRICT on packages.operator_id)
    packages = db.relationship('Package', back_populates='operator', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'website_url': self.website_url,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'rating': float(self.rating) if self.rating is not None else 0.0,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def __repr__(self):
        return f"<Operator {self.id}: {self.name}>"
