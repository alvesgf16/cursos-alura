from bank_queues.bank_queue import BankQueue
from consts import PRIORITY_CODE
from stats import RenderedStats, Stats


class PriorityQueue(BankQueue):
    def __init__(self) -> None:
        super().__init__()

    def _generate_current_password(self) -> None:
        self._current_password = f"{PRIORITY_CODE}{self._code}"

    def render_stats(self, stats: Stats) -> RenderedStats:
        return stats.render(self._customers_served)
