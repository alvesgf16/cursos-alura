from bank_queue import BankQueue
from consts import STANDARD_MAX_LENGTH
from tests.consts import MOCK_CODE


class MockQueueWithLimitCode(BankQueue):
    def __init__(self) -> None:
        super().__init__()
        self._code = STANDARD_MAX_LENGTH

    def _generate_current_password(self) -> None:
        self._current_password = f"{MOCK_CODE}{self._code}"
