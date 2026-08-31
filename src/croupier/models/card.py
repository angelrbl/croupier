from dataclasses import dataclass
from enum import Enum

class Rank(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'

    @property
    def score(self) -> int:
        if self.value in ['J', 'Q', 'K']:
            return 10
        if self.value == 'A':
            return 11
        return int(self.value)

class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"

@dataclass
class Card:
    rank: Rank
    suit: Suit

    @property
    def value(self) -> int:
        return self.rank.score

    def __str__(self) -> str:
        return f'{self.rank.value}{self.suit.value}'

if __name__ == "__main__":
    print(Card(Rank.ACE, Suit.HEARTS))