from typing import List

from stats import RenderedStats, Stats


class SummaryStats(Stats):
    def render(self, customers_served: List[str]) -> RenderedStats:
        return {f"{self._agency}-{self._day}": len(customers_served)}
