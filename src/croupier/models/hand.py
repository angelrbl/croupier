from dataclasses import dataclass, field
from croupier.models.card import Card, Rank

@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)
    _max: int = 21

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def __len__(self) -> int:
        return len(self.cards)
    
    @property
    def value(self) -> int:
        current_score = 0

        ace_count = 0
        for card in self.cards:
            if card.rank == Rank.ACE:
                ace_count += 1

            current_score += card.value

        while current_score > self._max and ace_count > 0:
            current_score -= 10
            ace_count -= 1

        return current_score

    @property
    def is_bust(self) -> bool:
        return self.value > self._max

    @property
    def is_blackjack(self) -> bool:
        return self.value == self._max and len(self.cards) == 2

    def __str__(self) -> str:
        return str([str(card) for card in self.cards])