from backend.database.models.asset import Asset
from backend.utils.schema import DepreciationDetails


def call(details: DepreciationDetails):
    # Update.
    return Asset.update(details)
