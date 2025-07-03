from datetime import datetime


class Date:
    @staticmethod
    def get_year(date: str) -> int:
        return datetime.strptime(date, "%Y-%m-%d").year
