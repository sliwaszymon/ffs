from enum import Enum


class TreeState(Enum):
    BURNED = 0
    ALIVE = 1
    FIRE = 2


class Tree:
    state: TreeState

    def __init__(self) -> None:
        self.state = TreeState.ALIVE

    def set_on_fire(self) -> None:
        self.state = TreeState.FIRE

    def extinguish(self) -> None:
        self.state = TreeState.BURNED

    def __str__(self) -> str:
        return self.state.name

    def __repr__(self) -> str:
        return str(self)
