import pandas as pd
from croupier.strats import BasicStrategy
from croupier.strats import Action
from croupier.models import Hand, Card, Rank, Suit
from croupier.simulation import run_simulation

def test_basic_strategy_logic():
    strategy = BasicStrategy()
    assert strategy.name == "Basic"

    hand = Hand(cards=[Card(rank=Rank.SEVEN, suit=Suit.HEARTS), Card(rank=Rank.TWO, suit=Suit.SPADES)])
    assert strategy(player_hand=hand) == Action.HIT

    hand.add_card(Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS))
    assert strategy(player_hand=hand) == Action.STAND

def test_run_simulation_returns_valid_dataframe():
    strategy = BasicStrategy()
    df = run_simulation(iterations=50, strategy=strategy, dealer_stand_threshold=17)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 50

def test_simulation_data_consistency():
    strategy = BasicStrategy()
    df = run_simulation(iterations=20, strategy=strategy, dealer_stand_threshold=17)
    
    assert (df["player_final_score"] >= df["player_initial_score"]).all()