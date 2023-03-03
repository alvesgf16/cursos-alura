from abc import ABC, abstractmethod
from typing import List

from consts import (
    STANDARD_MAX_LENGTH,
    STANDARD_QUEUE_RESET_CODE,
)


class BankQueue(ABC):
    def __init__(self) -> None:
        self._code = 0
        self.__queue: List[str] = []
        self._customers_served: List[str] = []
        self._current_password = ""

    def update_queue(self) -> None:
        self.__reset_queue()
        self._generate_current_password()
        self.__add_customer_to_queue()

    def __reset_queue(self) -> None:
        if self._code >= STANDARD_MAX_LENGTH:
            self._code = STANDARD_QUEUE_RESET_CODE
        else:
            self._code += 1

    @abstractmethod
    def _generate_current_password(self) -> None:
        ...

    def __add_customer_to_queue(self) -> None:
        self.__queue.append(self._current_password)

    def call_customer(self, a_teller: int) -> str:
        current_customer = self.__queue.pop(0)
        self._customers_served.append(current_customer)
        return (
            f"Current customer: {current_customer}, go to teller: {a_teller}"
        )
