class TileState:

    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    YELLOW = "YELLOW"
    RED = "RED"
    HORIZONTAL_YELLOW_UP = "Bi-Color Horizontal Yellow Up"
    HORIZONTAL_YELLOW_DOWN = "Bi-Color Horizontal Yellow Down"
    VERTICAL_YELLOW_LEFT = "Bi-Color Vertical Yellow Left"
    VERTICAL_YELLOW_RIGHT = "Bi-Color Vertical Yellow Right"

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def move(self, direction):
        if direction == TileState.UP:
            self.y -= 1
        elif direction == TileState.DOWN:
            self.y += 1
        elif direction == TileState.LEFT:
            self.x -= 1
        elif direction == TileState.RIGHT:
            self.x += 1

        if self.state == TileState.YELLOW:
            if direction == TileState.LEFT:
                self.state = TileState.VERTICAL_YELLOW_LEFT
            elif direction == TileState.RIGHT:
                self.state = TileState.VERTICAL_YELLOW_RIGHT
            elif direction == TileState.UP:
                self.state = TileState.HORIZONTAL_YELLOW_UP
            elif direction == TileState.DOWN:
                self.state = TileState.HORIZONTAL_YELLOW_DOWN
        elif self.state == TileState.RED:
            if direction == TileState.LEFT:
                self.state = TileState.VERTICAL_YELLOW_RIGHT
            elif direction == TileState.RIGHT:
                self.state = TileState.VERTICAL_YELLOW_LEFT
            elif direction == TileState.UP:
                self.state = TileState.HORIZONTAL_YELLOW_DOWN
            elif direction == TileState.DOWN:
                self.state = TileState.HORIZONTAL_YELLOW_UP
        elif self.state == TileState.VERTICAL_YELLOW_LEFT:
            if direction == TileState.LEFT:
                self.state = TileState.RED
            elif direction == TileState.RIGHT:
                self.state = TileState.YELLOW
        elif self.state == TileState.VERTICAL_YELLOW_RIGHT:
            if direction == TileState.LEFT:
                self.state = TileState.YELLOW
            elif direction == TileState.RIGHT:
                self.state = TileState.RED
        elif self.state == TileState.HORIZONTAL_YELLOW_UP:
            if direction == TileState.UP:
                self.state = TileState.RED
            elif direction == TileState.DOWN:
                self.state = TileState.YELLOW
        elif self.state == TileState.HORIZONTAL_YELLOW_DOWN:
            if direction == TileState.UP:
                self.state = TileState.YELLOW
            elif direction == TileState.DOWN:
                self.state = TileState.RED

        return self

    def clone(self):
        return TileState(self.x, self.y, self.state)

    def can_move(self, direction):
        # Can block move in direction given that it's at x, y position in state

        if (self.x == 0 and direction == TileState.LEFT) or (
            self.x == 7 and direction == TileState.RIGHT
        ):
            # Out Of Bounds
            return False

        if (self.y == 0 and direction == TileState.UP) or (
            self.y == 7 and direction == TileState.DOWN
        ):
            # Out Of Bounds
            return False

        n = self.clone().move(direction)
        if n.state == TileState.RED:
            if n.x == 7 and n.y == 0:
                pass
            else:
                return False

        return True

    def all_possible_moves(self):
        all_states = []

        for d in [TileState.UP, TileState.DOWN, TileState.RIGHT, TileState.LEFT]:
            if self.can_move(d):
                all_states.append(d)
        return all_states
