from croupier import Card, Suit, Rank

def test_card_value():
    card = Card(rank=Rank.SEVEN, suit=Suit.HEARTS)
    assert card.value == 7

def test_face_value():
    card = Card(rank=Rank.JACK, suit=Suit.HEARTS)
    assert card.value == 10

def test_ace_value():
    card = Card(rank=Rank.ACE, suit=Suit.HEARTS)
    assert card.value == 11

def test_ace_value():
    card = Card(rank=Rank.ACE, suit=Suit.HEARTS)
    assert str(card) == 'A♥'