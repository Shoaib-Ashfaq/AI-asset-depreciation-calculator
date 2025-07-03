import uuid
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, REAL, String, Date, INTEGER, TIMESTAMP
from backend.database.db import Base


class Assets(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = Column(TIMESTAMP(timezone=True), default=func.now())
    name = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)
    purchase_cost = Column(REAL, nullable=False)
    category = Column(String, nullable=False)
    depreciation_method = Column(String, nullable=True)
    useful_life = Column(REAL, nullable=True)
    salvage_value = Column(REAL, nullable=True)
    total_units_of_production = Column(INTEGER, nullable=True)
    annual_units_of_production = Column(REAL, nullable=True)

    def to_dict(self):
        # Converts the SQLAlchemy object to a dictionary.
        return {
            "id": self.id,
            "created": self.created,
            "name": self.name,
            "purchase_date": self.purchase_date,
            "purchase_cost": self.purchase_cost,
            "category": self.category,
            "depreciation_method": self.depreciation_method,
            "useful_life": self.useful_life,
            "salvage_value": self.salvage_value,
            "total_units_of_production": self.total_units_of_production,
            "annual_units_of_production": self.annual_units_of_production,
        }
