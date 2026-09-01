from enum import Enum
from typing import Protocol

from croupier.models import Hand, Card

class Action(Enum):
    HIT = 0
    STAND = 1

class Strategy(Protocol):
    def __init__(self, name) -> None:
        self.name = name

    def decide(self, player_hand: Hand, dealer_upcard: Card) -> Action:
        ...

    def __call__(self, player_hand: Card, dealer_upcard: Card):
        action = self.decide(player_hand=player_hand, dealer_upcard=dealer_upcard)
        return action