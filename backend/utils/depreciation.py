from typing import List, TypedDict
from backend.utils.schema import Asset
from backend.utils.date import Date

# Constants for depreciation methods
STRAIGHT_LINE = "Straight Line"
DOUBLE_DECLINING_BALANCE = "Double Declining Balance"
UNITS_OF_PRODUCTION = "Units of Production"
SUM_OF_YEARS_DIGIT = "Sum of Years Digits"


class DepreciationReport(TypedDict):
    year: int
    annual_depreciation: float
    accumulated_depreciation: float
    book_value: float


class Depreciation:
    @staticmethod
    def find_method(input: str) -> str:
        # Return the exact method name that matches
        # with the incoming string.
        input = input.lower()
        return (
            DOUBLE_DECLINING_BALANCE
            if "declining" in input
            else (
                UNITS_OF_PRODUCTION
                if "units" in input
                else SUM_OF_YEARS_DIGIT if "sum" in input else STRAIGHT_LINE
            )
        )

    @staticmethod
    def generate_report(asset: Asset) -> List[DepreciationReport]:
        # Get purchase year from purchase date.
        purchase_year = Date.get_year(str(asset.purchase_date))

        method = asset.depreciation_method
        if method == DOUBLE_DECLINING_BALANCE:
            return Depreciation.generate_double_declining_balance_report(
                asset, purchase_year
            )
        elif method == SUM_OF_YEARS_DIGIT:
            return Depreciation.generate_sum_of_years_digits_report(
                asset, purchase_year
            )
        elif method == UNITS_OF_PRODUCTION:
            return Depreciation.generate_units_of_production_report(
                asset, purchase_year
            )
        else:
            return Depreciation.generate_straight_line_report(asset, purchase_year)

    @staticmethod
    def _create_report_entry(
        year: int,
        annual_depreciation: float,
        accumulated_depreciation: float,
        book_value: float,
    ) -> DepreciationReport:
        return DepreciationReport(
            year=year,
            annual_depreciation=annual_depreciation,
            accumulated_depreciation=accumulated_depreciation,
            book_value=book_value,
        )

    @staticmethod
    def generate_straight_line_report(
        asset: Asset, purchase_year: int
    ) -> List[DepreciationReport]:
        useful_life = asset.useful_life
        purchase_cost = asset.purchase_cost
        salvage_value = asset.salvage_value

        # Calculate the annual depreciation.
        annual_depreciation = (purchase_cost - salvage_value) / useful_life

        # Initialize accumulated depreciation.
        accumulated_depreciation = 0

        # Generate.
        depreciation_reports = []
        for year in range(0, int(useful_life)):
            report_year = purchase_year + year
            accumulated_depreciation += annual_depreciation
            remaining_value = purchase_cost - accumulated_depreciation

            # Append.
            depreciation_reports.append(
                Depreciation._create_report_entry(
                    report_year,
                    annual_depreciation,
                    accumulated_depreciation,
                    remaining_value,
                )
            )

        return depreciation_reports

    @staticmethod
    def generate_double_declining_balance_report(
        asset: Asset, purchase_year: int
    ) -> List[DepreciationReport]:
        useful_life = asset.useful_life
        purchase_cost = asset.purchase_cost
        salvage_value = asset.salvage_value

        # Calculate the depreciation rate.
        depreciation_rate = 2 / useful_life

        # Initialize variables.
        accumulated_depreciation = 0
        book_value = purchase_cost

        # Generate.
        depreciation_reports = []
        for year in range(0, int(useful_life)):
            report_year = purchase_year + year

            # Calculate the depreciation for the current year.
            annual_depreciation = book_value * depreciation_rate

            # Ensure that depreciation does not cause the book value to fall below the salvage value.
            if book_value - annual_depreciation < salvage_value:
                annual_depreciation = book_value - salvage_value
                accumulated_depreciation += annual_depreciation
                book_value = salvage_value
            else:
                accumulated_depreciation += annual_depreciation
                book_value -= annual_depreciation

            remaining_value = book_value

            # Append.
            depreciation_reports.append(
                Depreciation._create_report_entry(
                    report_year,
                    annual_depreciation,
                    accumulated_depreciation,
                    remaining_value,
                )
            )

        # Return.
        return depreciation_reports

    @staticmethod
    def generate_sum_of_years_digits_report(
        asset: Asset, purchase_year: int
    ) -> List[DepreciationReport]:
        useful_life = asset.useful_life
        purchase_cost = asset.purchase_cost
        salvage_value = asset.salvage_value

        # Calculate the sum of the years' digits.
        sum_of_digits = sum(range(1, int(useful_life) + 1))

        # Initialize accumulated depreciation.
        accumulated_depreciation = 0

        # Generate.
        depreciation_reports = []
        for year in range(0, int(useful_life)):
            report_year = purchase_year + year

            # Calculate the fraction for the current year.
            remaining_years = useful_life - (year - 1)
            depreciation_fraction = remaining_years / sum_of_digits

            # Calculate the annual depreciation for this year.
            annual_depreciation = depreciation_fraction * (
                purchase_cost - salvage_value
            )

            # Update the accumulated depreciation.
            accumulated_depreciation += annual_depreciation

            # Ensure that accumulated depreciation does not exceed (purchase cost - salvage value).
            if accumulated_depreciation > purchase_cost - salvage_value:
                accumulated_depreciation = purchase_cost - salvage_value
                annual_depreciation = accumulated_depreciation - (
                    accumulated_depreciation - annual_depreciation
                )

            remaining_value = purchase_cost - accumulated_depreciation

            # Append.
            depreciation_reports.append(
                Depreciation._create_report_entry(
                    report_year,
                    annual_depreciation,
                    accumulated_depreciation,
                    remaining_value,
                )
            )

        # Return.
        return depreciation_reports

    @staticmethod
    def generate_units_of_production_report(
        asset: Asset,
        purchase_year: int,
    ) -> List[DepreciationReport]:
        useful_life = asset.useful_life
        purchase_cost = asset.purchase_cost
        salvage_value = asset.salvage_value

        # Calculate the depreciation per unit.
        depreciation_per_unit = (
            purchase_cost - salvage_value
        ) / asset.total_units_of_production

        # Initialize accumulated depreciation.
        accumulated_depreciation = 0

        # Generate.
        depreciation_reports = []
        for year in range(0, int(useful_life)):
            report_year = purchase_year + year

            annual_depreciation = (
                asset.annual_units_of_production * depreciation_per_unit
            )

            # Update the accumulated depreciation.
            accumulated_depreciation += annual_depreciation

            # Ensure that accumulated depreciation does not exceed the purchase cost minus the salvage value.
            if accumulated_depreciation > purchase_cost - salvage_value:
                accumulated_depreciation = purchase_cost - salvage_value
                annual_depreciation = accumulated_depreciation - (
                    accumulated_depreciation - annual_depreciation
                )

            remaining_value = purchase_cost - accumulated_depreciation

            # Append.
            depreciation_reports.append(
                Depreciation._create_report_entry(
                    report_year,
                    annual_depreciation,
                    accumulated_depreciation,
                    remaining_value,
                )
            )

        # Return.
        return depreciation_reports
