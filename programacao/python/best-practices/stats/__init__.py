from abc import ABC, abstractmethod
from typing import Dict, List, Union


RenderedStats = Dict[str, Union[str, int, List[str]]]


class Stats(ABC):
    def __init__(self, a_day: str, an_agency: int) -> None:
        self._day = a_day
        self._agency = an_agency

    @abstractmethod
    def render(self, customers_served: List[str]) -> RenderedStats:
        ...
