import pandas as pd

from croupier.core import Game, GameState
from croupier.strats import Strategy, Action

def run_simulation(iterations: int, strategy: Strategy, dealer_stand_threshold: int = 17) -> pd.DataFrame:
    records = []

    for i in range(iterations):
        game = Game(dealer_stand_threshold=dealer_stand_threshold)
        game.start()

        player_initial_score = game.player_score
        dealer_upcard = game.dealer_upcard

        while game.game_state == GameState.PLAYER_TURN:
            action = strategy(player_hand=game.player_hand, dealer_upcard=dealer_upcard)

            match action:
                case Action.HIT:
                    game.hit()
                case Action.STAND:
                    game.stand()

        records.append(
            {
                "strategy_name": strategy.name,
                "player_initial_score": player_initial_score,
                "dealer_upcard_value": dealer_upcard.value,
                "player_final_score": game.player_score,
                "player_bust": game.player_hand.is_bust,
                "player_blackjack": game.player_hand.is_blackjack,
                "result": game.result.value
            }
        )

    return pd.DataFrame(records)