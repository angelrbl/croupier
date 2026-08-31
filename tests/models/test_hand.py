from croupier import Card, Hand, Rank, Suit

def test_normal_hand():
    hand = Hand(cards=[Card(rank=Rank.TEN, suit=Suit.HEARTS)])
    hand.add_card(card=Card(rank=Rank.FIVE, suit=Suit.SPADES))

    assert hand.value == 15

def test_blackjack():
    hand = Hand()
    hand.add_card(card=Card(rank=Rank.ACE, suit=Suit.SPADES))
    hand.add_card(card=Card(rank=Rank.KING, suit=Suit.CLUBS))

    assert hand.is_blackjack is True

def test_ace_saves_hand():
    hand = Hand(cards=[Card(rank=Rank.FIVE, suit=Suit.DIAMONDS), Card(rank=Rank.KING, suit=Suit.CLUBS)])
    hand.add_card(card=Card(rank=Rank.ACE, suit=Suit.HEARTS))

    assert hand.value == 16

def test_multiple_aces():
    hand = Hand()
    hand.add_card(card=Card(rank=Rank.ACE, suit=Suit.DIAMONDS))
    hand.add_card(card=Card(rank=Rank.ACE, suit=Suit.SPADES))

    assert hand.value == 12

def test_burst():
    hand = Hand(cards=[
        Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
        Card(rank=Rank.KING, suit=Suit.CLUBS),
        Card(rank=Rank.JACK, suit=Suit.HEARTS),
    ])

    assert hand.value == 25
    assert hand.is_bust is True