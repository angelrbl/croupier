from enum import Enum
from abc import ABC, abstractmethod

from croupier.models import Hand, Card

class Action(Enum):
    HIT = 0
    STAND = 1

class Strategy(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def decide(self, player_hand: Hand, dealer_upcard: Card | None = None) -> Action:
        ...

    def __call__(self, player_hand: Hand, dealer_upcard: Card | None = None) -> Action:
        return self.decide(player_hand=player_hand, dealer_upcard=dealer_upcard)