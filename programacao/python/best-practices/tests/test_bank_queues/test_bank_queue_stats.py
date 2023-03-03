from typing import Tuple

from bank_queue import BankQueue
from bank_queue.priority import PriorityQueue
from stats.detailed_stats import DetailedStats
from stats.summary_stats import SummaryStats
from tests.consts import TEST_AGENCY, TEST_DAY
from tests.test_bank_queues import TestBankQueues


class TestBankQueueStats(TestBankQueues):
    def test_priority_queue_statistics(self) -> None:
        priority_queue = self._given_queue_with_three_customers("priority")
        self._when_two_customers_are_called(priority_queue)
        statistics = self.__when_statistics_are_run(priority_queue)
        self._then_the_correct_messages_are_displayed(
            statistics,
            "{'198-10/01/1993': 2}",
            "{'day': '10/01/1993', 'agency': 198,"
            + " 'customers_served': ['PR1', 'PR2'],"
            + " 'number_of_customers_served': 2}",
        )

    def __when_statistics_are_run(self, a_queue: BankQueue) -> Tuple[str, str]:
        assert isinstance(a_queue, PriorityQueue)
        summary_stats = a_queue.render_stats(
            SummaryStats(TEST_DAY, TEST_AGENCY)
        )
        detailed_stats = a_queue.render_stats(
            DetailedStats(TEST_DAY, TEST_AGENCY)
        )
        return str(summary_stats), str(detailed_stats)
