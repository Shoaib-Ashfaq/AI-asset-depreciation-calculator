import uuid
from fastapi import HTTPException
from backend.utils.depreciation import Depreciation
from backend.database.models.asset import Asset


def call(asset_id: uuid.UUID):
    # Get asset.
    asset, err = Asset.get(asset_id)
    if not asset:
        raise HTTPException(status_code=500, detail=err)

    # Generate depreciation report.
    report = Depreciation.generate_report(asset)

    # Return.
    return {**asset.to_dict(), "report": report}
