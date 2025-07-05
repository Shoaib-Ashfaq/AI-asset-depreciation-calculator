import uuid
from sqlalchemy import func
from backend.database.db import Database
from backend.database.migrations.assets import Assets
from backend.utils.schema import AssetDetails, DepreciationDetails


class Asset:
    def get(asset_id: uuid.UUID):
        # Get db.
        db = Database.get()

        # Get asset.
        asset = db.query(Assets).filter(Assets.id == asset_id).first()

        # Return.
        if asset:
            return asset, ""
        else:
            return None, "Invalid Asset ID"

    def save(asset_details: AssetDetails):
        # Get db.
        db = Database.get()

        # Generate asset Id.
        asset_id = uuid.uuid4()

        # Create an object to save.
        asset_data = Assets(
            id=asset_id,
            name=asset_details.name,
            purchase_date=asset_details.purchase_date,
            purchase_cost=asset_details.purchase_cost,
            category=asset_details.category,
            total_units_of_production=asset_details.total_units_of_production,
        )

        # Save.
        db.add(asset_data)
        db.commit()
        db.refresh(asset_data)
        return asset_id

    def update(depreciationDetails: DepreciationDetails):
        # Get db.
        db = Database.get()

        # Get asset.
        asset = db.query(Assets).filter(Assets.id == depreciationDetails.id).first()

        # Update values.
        for key, value in depreciationDetails.model_dump().items():
            if hasattr(asset, key):
                setattr(asset, key, value)

        db.commit()
        db.refresh(asset)

        return depreciationDetails.id

    def get_asset_list(category: str = None, limit: int = 10):
        # Get db.
        db = Database.get()

        # Base query.
        query = db.query(Assets.id, Assets.name, Assets.category)

        # Get list.
        if category:
            query = query.filter(func.lower(Assets.category) == func.lower(category))

        assets = query.order_by(Assets.created.desc()).limit(limit).all()

        # Convert to list of dicts.
        asset_list = [
            {"id": asset.id, "name": asset.name, "category": asset.category}
            for asset in assets
        ]

        # Return.
        return asset_list
