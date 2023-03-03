from bank_queues.bank_queue import BankQueue
from consts import PRIORITY_QUEUE_TYPE, REGULAR_QUEUE_TYPE
from bank_queues.priority_queue import PriorityQueue
from bank_queues.regular_queue import RegularQueue


class QueueFactory:
    @staticmethod
    def create_queue(queue_type: str) -> BankQueue:
        if queue_type == REGULAR_QUEUE_TYPE:
            return RegularQueue()
        elif queue_type == PRIORITY_QUEUE_TYPE:
            return PriorityQueue()
        else:
            raise NotImplementedError("Queue type does not exist")
