import uuid
from pydantic import BaseModel


class AssetDetails(BaseModel):
    name: str
    purchase_cost: float
    purchase_date: str
    category: str
    total_units_of_production: int


class DepreciationDetails(BaseModel):
    id: uuid.UUID
    useful_life: float
    salvage_value: float
    depreciation_method: str
    annual_units_of_production: float


class Asset:
    id: uuid.UUID
    name: str
    purchase_cost: float
    purchase_date: str
    category: str
    useful_life: float
    salvage_value: float
    depreciation_method: str
    total_units_of_production: int
    annual_units_of_production: int
