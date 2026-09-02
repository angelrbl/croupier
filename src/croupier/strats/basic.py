from croupier.strats.base import Action, Strategy
from croupier.models import Hand, Card

class BasicStrategy(Strategy):
    @property
    def name(self) -> str:
        return "Basic"

    def decide(self, player_hand: Hand, dealer_upcard: Card | None = None) -> Action:
        if player_hand.value < 17:
            return Action.HIT

        return Action.STAND