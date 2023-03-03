import pytest

from bank_queue import BankQueue
from bank_queue.factory import QueueFactory
from tests.mocks.mock_queue_with_limit_code import MockQueueWithLimitCode
from tests.test_bank_queues import TestBankQueues


class TestBankQueueCalls(TestBankQueues):
    def test_create_a_queue_of_invalid_type_raises_an_exception(
        self,
    ) -> None:
        with pytest.raises(
            NotImplementedError, match="Queue type does not exist"
        ):
            QueueFactory.create_queue("invalid_type")

    def test_regular_queue(self) -> None:
        self.__basic_queue_test(
            "regular",
            "Current customer: NM1, go to teller: 5",
            "Current customer: NM2, go to teller: 3",
        )

    def test_priority_queue(self) -> None:
        self.__basic_queue_test(
            "priority",
            "Current customer: PR1, go to teller: 5",
            "Current customer: PR2, go to teller: 3",
        )

    def test_queue_with_limit_code(self) -> None:
        queue_with_limit_code = self.__given_queue_with_limit_code()
        actual_messages = self._when_two_customers_are_called(
            queue_with_limit_code
        )
        self._then_the_correct_messages_are_displayed(
            actual_messages,
            "Current customer: MK0, go to teller: 5",
            "Current customer: MK1, go to teller: 3",
        )

    def __basic_queue_test(
        self, queue_type: str, *expected_messages: str
    ) -> None:
        regular_queue = self._given_queue_with_three_customers(queue_type)
        actual_messages = self._when_two_customers_are_called(regular_queue)
        self._then_the_correct_messages_are_displayed(
            actual_messages, expected_messages[0], expected_messages[1]
        )

    def __given_queue_with_limit_code(self) -> BankQueue:
        result = MockQueueWithLimitCode()
        return self._add_three_customers_to_queue(result)
