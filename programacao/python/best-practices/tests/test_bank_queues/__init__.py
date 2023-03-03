from typing import Tuple
import unittest

from bank_queue import BankQueue
from bank_queue.factory import QueueFactory


class TestBankQueues(unittest.TestCase):
    def _given_queue_with_three_customers(
        self, a_queue_type: str
    ) -> BankQueue:
        result = QueueFactory.create_queue(a_queue_type)
        return self._add_three_customers_to_queue(result)

    def _add_three_customers_to_queue(
        self, result: BankQueue
    ) -> BankQueue:
        result.update_queue()
        result.update_queue()
        result.update_queue()
        return result

    def _when_two_customers_are_called(
        self, a_queue: BankQueue
    ) -> Tuple[str, str]:
        first_call = a_queue.call_customer(5)
        second_call = a_queue.call_customer(3)
        return first_call, second_call

    def _then_the_correct_messages_are_displayed(
        self, actual: Tuple[str, str], *expected: str
    ) -> None:
        assert actual[0] == expected[0]
        assert actual[1] == expected[1]
