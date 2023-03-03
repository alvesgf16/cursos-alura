from typing import List

from stats import RenderedStats, Stats


class DetailedStats(Stats):
    def render(self, customers_served: List[str]) -> RenderedStats:
        return {
            "day": self._day,
            "agency": self._agency,
            "customers_served": customers_served,
            "number_of_customers_served": len(customers_served),
        }
