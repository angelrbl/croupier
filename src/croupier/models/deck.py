from dataclasses import dataclass, field
import random

from .card import Card, Rank, Suit

@dataclass
class Deck:
    cards: list[Card] = field(init=False)

    def __post_init__(self) -> None:
        self.cards = self._default_deck()

    def _default_deck(self) -> list[Card]:
        return [Card(rank=rank, suit=suit) for suit in Suit for rank in Rank]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

    def clone(self) -> Deck:
        new_deck = Deck()
        new_deck.cards = list(self.cards)
        return new_deck

    def __str__(self) -> str:
        return str([str(card) for card in self.cards])