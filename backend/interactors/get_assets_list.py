from backend.database.models.asset import Asset

def call():
    # Get asset list.
    asset_list = Asset.get_asset_list()

    # Return.
    return asset_list
