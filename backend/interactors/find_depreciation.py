from backend.service.openai import LLM
from backend.utils.prompt import Prompt
from backend.utils.schema import AssetDetails
from backend.utils.depreciation import Depreciation
from backend.database.models.asset import Asset


def call(asset_details: AssetDetails):
    # Get asset list.
    asset_list = Asset.get_asset_list(category=asset_details.category)

    # Get prompt.
    prompt = ""
    if len(asset_list) > 0:
        prompt = Prompt.find_depreciation_with_context(asset_details, asset_list)
    else:
        prompt = Prompt.find_depreciation(asset_details)

    # Find.
    resp = LLM.ask(prompt)

    # Retrieve data.
    life, value, method = resp.split("||")

    # Get exact method name.
    method = Depreciation.find_method(method)

    # Save asset.
    id = Asset.save(asset_details)

    # Return.
    return {
        "asset_id": id,
        "useful_life": life,
        "depreciation_method": method,
        "salvage_value": int(value),
        "total_units_of_production": asset_details.total_units_of_production,
    }
