from tile_state import TileState


def test_answer():
    t = TileState(0, 0, TileState.RED)
    assert t.can_move(TileState.UP) == False
    assert t.can_move(TileState.LEFT) == False
    assert t.can_move(TileState.DOWN) == True
    assert t.can_move(TileState.RIGHT) == True

    assert TileState(3, 3, TileState.YELLOW).can_move(TileState.UP) == True
    assert TileState(3, 3, TileState.VERTICAL_YELLOW_LEFT).can_move(TileState.UP) == True
    assert TileState(3, 3, TileState.VERTICAL_YELLOW_RIGHT).can_move(TileState.UP) == True
    assert TileState(3, 3, TileState.HORIZONTAL_YELLOW_DOWN).can_move(TileState.UP) == True
    assert TileState(3, 3, TileState.HORIZONTAL_YELLOW_UP).can_move(TileState.UP) == False


def test_move():
    t = (
        TileState(0, 0, TileState.RED)
        .move(TileState.DOWN)
        .move(TileState.DOWN)
        .move(TileState.DOWN)
        .move(TileState.RIGHT)
        .move(TileState.UP)
    )

    assert t.x == 1
    assert t.y == 2
    assert t.state == TileState.YELLOW


def test_final_move():
    assert TileState(5, 0, TileState.VERTICAL_YELLOW_RIGHT).can_move(TileState.RIGHT) == False
    assert TileState(6, 0, TileState.VERTICAL_YELLOW_RIGHT).can_move(TileState.RIGHT) == True


def test_all_states():
    t = TileState(0, 0, TileState.RED)
    all_moves = t.all_possible_moves()
    assert len(all_moves) == 2
    assert TileState.DOWN in all_moves
    assert TileState.RIGHT in all_moves
