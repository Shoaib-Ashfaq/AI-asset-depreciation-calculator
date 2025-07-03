from fastapi import APIRouter
from backend.utils.schema import AssetDetails, DepreciationDetails
from backend.interactors import get_asset as get_asset_interactor
from backend.interactors import upd_asset as upd_asset_interactor
from backend.interactors import find_depreciation as find_depreciation_interactor
import uuid

# Create a router.
router = APIRouter(tags=["depreciation"], prefix="/api")


# Routes.
@router.post("/find-depreciation/")
async def find_depreciation(payload: AssetDetails):
    return find_depreciation_interactor.call(payload)


@router.post("/upd-asset/")
async def upd_asset(payload: DepreciationDetails):
    return upd_asset_interactor.call(payload)


@router.get("/get-asset/")
async def get_asset(asset_id: uuid.UUID):
    return get_asset_interactor.call(asset_id)
