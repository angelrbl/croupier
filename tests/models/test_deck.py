import pytest
from croupier import Deck, Card

def test_full_deck_size():
    deck = Deck()
    assert len(deck) == 52

def test_draw_card():
    deck = Deck()
    card = deck.draw()

    assert isinstance(card, Card)
    assert len(deck) == 51

def test_shuffle():
    deck = Deck()
    deck_clone = deck.clone()

    deck.shuffle()
    print(deck_clone.cards)
    print(deck.cards)
    assert deck.cards != deck_clone.cards

def test_empty_deck():
    deck = Deck()

    for i in range(52):
        deck.draw()

    assert len(deck) == 0

def test_empty_draw_error():
    deck = Deck()
    
    for i in range(52):
        deck.draw()

    with pytest.raises(IndexError):
        deck.draw()