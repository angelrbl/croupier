from enum import Enum
from croupier.models import Deck, Hand, Card

class GameState(Enum):
    PLAYER_TURN = 0
    DEALER_TURN = 1
    GAME_ENDED = 2

class Result(Enum):
    WIN = 'win'
    LOSS = 'loss'
    DRAW = 'draw'

class Game:
    def __init__(self, dealer_stand_threshold: int = 17) -> None:
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.game_state = GameState.GAME_ENDED

        self.dealer_stand_threshold = dealer_stand_threshold

    @property
    def dealer_upcard(self) -> Card | None:
        if len(self.dealer_hand) > 0:
            return self.dealer_hand.cards[0]
        return None

    @property
    def player_score(self) -> int:
        return self.player_hand.value

    @property
    def result(self) -> Result | None:
        if self.game_state != GameState.GAME_ENDED:
            return

        if self.player_hand.is_bust:
            return Result.LOSS
        
        if self.dealer_hand.is_bust:
            return Result.WIN

        if self.player_hand.value < self.dealer_hand.value:
            return Result.LOSS
        elif self.player_hand.value > self.dealer_hand.value:
            return Result.WIN
        else:
            return Result.DRAW

    def start(self) -> None:
        self.deck.shuffle()

        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())

        if self.player_hand.is_blackjack or self.dealer_hand.is_blackjack:
            self.game_state = GameState.GAME_ENDED
        else:
            self.game_state = GameState.PLAYER_TURN

    def hit(self) -> None:
        match (self.game_state):
            case GameState.GAME_ENDED:
                return
            case GameState.PLAYER_TURN:
                self.player_hand.add_card(card=self.deck.draw())

                if self.player_hand.is_bust:
                    self.game_state = GameState.GAME_ENDED
            case GameState.DEALER_TURN:
                self.dealer_hand.add_card(card=self.deck.draw())

                if self.dealer_hand.is_bust:
                    self.game_state = GameState.GAME_ENDED

    def stand(self) -> None:
        self.game_state = GameState.DEALER_TURN

        while self.dealer_hand.value < self.dealer_stand_threshold:
            self.hit()

        self.game_state = GameState.GAME_ENDED