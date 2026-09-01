from croupier import GameState, Game, Result

def test_start():
    game = Game()

    game.start()

    assert game.game_state == GameState.PLAYER_TURN
    assert len(game.player_hand) == 2
    assert len(game.dealer_hand) == 2

def test_bust():
    game = Game()
    game.start()

    while game.player_hand.is_bust is False:
        game.hit()

    assert game.game_state == GameState.GAME_ENDED
    assert game.result == Result.LOSS

def test_stand():
    game = Game()
    game.start()

    game.stand()

    assert game.game_state == GameState.GAME_ENDED
    assert game.dealer_hand.value > game.dealer_stand_threshold