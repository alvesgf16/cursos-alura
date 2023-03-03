from bank_queue import BankQueue
from consts import PRIORITY_QUEUE_TYPE, REGULAR_QUEUE_TYPE
from bank_queue.priority import PriorityQueue
from bank_queue.regular import RegularQueue


class QueueFactory:
    @staticmethod
    def create_queue(a_queue_type: str) -> BankQueue:
        if a_queue_type == REGULAR_QUEUE_TYPE:
            return RegularQueue()
        elif a_queue_type == PRIORITY_QUEUE_TYPE:
            return PriorityQueue()
        else:
            raise NotImplementedError("Queue type does not exist")
