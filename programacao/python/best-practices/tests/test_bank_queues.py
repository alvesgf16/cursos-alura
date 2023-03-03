import pytest
from typing import Tuple

from bank_queue import BankQueue
from bank_queue.priority import PriorityQueue
from bank_queue.factory import QueueFactory
from stats.detailed_stats import DetailedStats
from stats.summary_stats import SummaryStats
from tests.mocks.mock_queue_with_limit_code import MockQueueWithLimitCode
from tests.consts import TEST_AGENCY, TEST_DAY


def test_creating_a_queue_of_invalid_type_raises_an_exception() -> None:
    with pytest.raises(NotImplementedError, match="Queue type does not exist"):
        QueueFactory.create_queue("invalid_type")


def test_regular_queue() -> None:
    regular_queue = given_queue_with_three_customers("regular")
    actual_messages = when_two_customers_are_called(regular_queue)
    then_the_correct_messages_are_displayed(
        actual_messages,
        "Current customer: NM1, go to teller: 5",
        "Current customer: NM2, go to teller: 3",
    )


def test_priority_queue() -> None:
    priority_queue = given_queue_with_three_customers("priority")
    actual_messages = when_two_customers_are_called(priority_queue)
    then_the_correct_messages_are_displayed(
        actual_messages,
        "Current customer: PR1, go to teller: 5",
        "Current customer: PR2, go to teller: 3",
    )


def test_queue_with_limit_code() -> None:
    queue_with_limit_code = given_queue_with_limit_code()
    actual_messages = when_two_customers_are_called(queue_with_limit_code)
    then_the_correct_messages_are_displayed(
        actual_messages,
        "Current customer: MK0, go to teller: 5",
        "Current customer: MK1, go to teller: 3",
    )


def test_priority_queue_statistics() -> None:
    priority_queue = given_queue_with_three_customers("priority")
    when_two_customers_are_called(priority_queue)
    statistics = when_statistics_are_run(priority_queue)
    then_the_correct_messages_are_displayed(
        statistics,
        "{'198-10/01/1993': 2}",
        "{'day': '10/01/1993', 'agency': 198,"
        + " 'customers_served': ['PR1', 'PR2'],"
        + " 'number_of_customers_served': 2}",
    )


def given_queue_with_three_customers(a_queue_type: str) -> BankQueue:
    result = QueueFactory.create_queue(a_queue_type)
    result.update_queue()
    result.update_queue()
    result.update_queue()
    return result


def given_queue_with_limit_code() -> BankQueue:
    result = MockQueueWithLimitCode()
    result.update_queue()
    result.update_queue()
    return result


def when_statistics_are_run(a_queue: BankQueue) -> Tuple[str, str]:
    assert isinstance(a_queue, PriorityQueue)
    summary_stats = a_queue.render_stats(SummaryStats(TEST_DAY, TEST_AGENCY))
    detailed_stats = a_queue.render_stats(DetailedStats(TEST_DAY, TEST_AGENCY))
    return str(summary_stats), str(detailed_stats)


def when_two_customers_are_called(a_queue: BankQueue) -> Tuple[str, str]:
    first_call = a_queue.call_customer(5)
    second_call = a_queue.call_customer(3)
    return first_call, second_call


def then_the_correct_messages_are_displayed(
    actual: Tuple[str, str], *expected: str
) -> None:
    assert actual[0] == expected[0]
    assert actual[1] == expected[1]
