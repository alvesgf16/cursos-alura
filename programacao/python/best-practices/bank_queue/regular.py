from bank_queue import BankQueue
from consts import REGULAR_CODE


class RegularQueue(BankQueue):
    def __init__(self) -> None:
        super().__init__()

    def _generate_current_password(self) -> None:
        self._current_password = f"{REGULAR_CODE}{self._code}"
