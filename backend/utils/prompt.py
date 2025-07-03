from backend.utils.schema import AssetDetails


class Prompt:
    def find_depreciation(asset_details: AssetDetails):
        return f"""
            Imagine you are a Fixed Asset Manager with expertise in asset management and depreciation calculation.
            You are provided with the following details of an asset:
            - Asset Name: {asset_details.name}
            - Purchase Cost: {asset_details.purchase_cost}
            - Purchase Date: {asset_details.purchase_date}
            - Category: {asset_details.category}
            - Production Units: {asset_details.category} (Ignore this if not relevant)

            Based on this information, provide the following details:
            1. The estimated useful life (in years) of the asset. Consider industry standards, asset category, and any relevant factors.
            2. The salvage value of the asset, which is the expected residual value after the asset's useful life ends. Please provide it as an integer.
            3. The best depreciation method to use for the asset. Select the method based on the asset's category, purpose, and other relevant considerations. Don't just pick the most commonly used method; provide the method that would be most appropriate for the asset in question.
            (NOTE:
            - Depreciation method should be from these options: Straight-Line, Double-Declining-Balance, Sum-of-Years-Digits, Units-of-Production.
            - If the best method for this is Units-of-Production, you can consider any number of units per year. I will adjust that later. 
            - Make sure to consider the methods for calculating depreciation before giving the answer.
            )

            Instructions:
            1. Answer all three questions concisely, following the format below:
                - estimated_life||salvage_value||method_name
            2. Do not include extra text or explanations beyond this structured format.
        """

    def find_depreciation_with_context(asset_details: AssetDetails, asset_list: list):
        # Get actual prompt.
        prompt = Prompt.find_depreciation(asset_details)

        # Convert assets list to str.
        strForm = ""
        for asset in asset_list:
            strForm += f"""(
                Asset Name: {asset.name},
                Purchase Cost: {asset.purchase_cost},
                Purchase Date: {asset.purchase_date},
                Category: {asset.category},
                Depreciation Method: {asset.depreciation_method},
                Useful Life: {asset.salvage_value},
                Total Units of Production: {asset.total_units_of_production}
            )"""

        # Prepare context.
        context = f"""
            Here are some previously analyzed assets: {strForm}
            Note:
            While these results provide some context, do not rely solely on them.
            Apply your professional judgment and industry knowledge to refine your answer for the new asset based on industry standards and specific asset characteristics:
        """

        return prompt + "\n" + context
