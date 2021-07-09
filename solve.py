import copy
import random

from tile_state import TileState


def init_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(False)

    return board


def board_is_covered(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j]:
                return False

    return True


def a_one_tile_gap_exists(board):
    for i in range(len(board)):
        if board[i][0] == False and board[i][1] == True:
            return (i, 0)
        for j in range(1, 6):
            if board[i][j - 1] == True and board[i][j + 1] == True and board[i][j] == False:
                return (i, j)

    t_board = transpose_board(board)
    for i in range(len(t_board)):
        if t_board[i][0] == False and t_board[i][1] == True:
            return (0, i)
    for j in range(1, 6):
        if t_board[i][j - 1] == True and t_board[i][j + 1] == True and t_board[i][j] == False:
            return (j, i)

    return None


class Move:
    def __init__(self, tile_state: TileState, direction: str):
        self.tile_state = tile_state
        self.direction = direction


def transpose_board(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]


def cant_solve_from_here(board, position):
    for i in range(len(board)):
        if all(board[i]) and position.x < i:
            # Trapped to the left
            return True

    rez = transpose_board(board)
    for i in range(len(board)):
        if all(rez[i]) and position.y > i:
            # Trapped to the left
            return True

    return False


def print_board(board):
    for i in range(len(board)):
        line = ""
        for j in range(len(board[i])):
            if board[j][i]:
                line += "x"
            else:
                line += " "
        print(line)


def solve(moves, board):
    moves_str = ", ".join([str(m.direction) for m in moves])

    if len(moves) > 61:
        print(f"Move Length: {len(moves)} {moves_str}")
        print_board(board)
        print("" )

    if board_is_covered(board):
        if moves[-1].tile_state.state == TileState.RED:
            return True
        else:
            # Close, Filled the board, wrong color at the end step
            return False

    if cant_solve_from_here(board, moves[-1].tile_state):
        return False

    one_tile_check = a_one_tile_gap_exists(board)
    if (
        one_tile_check
        and abs(one_tile_check[0] - moves[-1].tile_state.x) > 1
        and abs(one_tile_check[1] - moves[-1].tile_state.y) > 1
    ):
        #print_board(board)
        #print(f"Move Length: {len(moves)} {moves_str}")
        #print(one_tile_check)
        #print(f"{moves[-1].tile_state.x},  {moves[-1].tile_state.y}")
        #print("")
        return False

    all_moves = moves[-1].tile_state.all_possible_moves()

    if len(all_moves) == 0:
        return False

    random.shuffle(all_moves)
    for i in all_moves:
        new_state = moves[-1].tile_state.clone().move(i)
        new_moves = moves.copy()
        new_moves.append(Move(new_state, i))
        new_board = copy.deepcopy(board)
        if new_board[new_state.x][new_state.y]:
            # Already Visited that Tile
            pass
        else:
            new_board[new_state.x][new_state.y] = True
            solved = solve(new_moves, new_board)
            if solved:
                return True

    return False


board = init_board(8)
board[0][0] = True

initial_position = Move(TileState(0, 0, TileState.RED), None)

solve([initial_position], board)

print(f"({t.x}, {t.y}, {t.state}")
