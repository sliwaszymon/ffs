from src.objects.tree import Tree
import random


class Forest:
    size: tuple[int, int]
    field: list[list[Tree]]

    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.field = [[Tree() for x in range(size[0])] for y in range(size[1])]

    def setup_fire(self, n: int = 1) -> None:
        fired: list[tuple[int, int]] = []
        for _ in range(n):
            while True:
                x, y = random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1)
                if (x, y) not in fired:
                    break
            fired.append((x, y))
            self.field[y][x].set_on_fire()

    def next_generation(self, p: float) -> None:
        new_generation = [[Tree() for x in range(self.size[0])] for y in range(self.size[1])]
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.field[y][x].state.value == 1:
                    burning_neighbors = self._burning_neighbors((x, y))
                    for _ in range(burning_neighbors):
                        if random.uniform(0.0, 1.0) < p:
                            new_generation[y][x].set_on_fire()
                            break
                else:
                    new_generation[y][x].extinguish()
        self.field = new_generation

    def _burning_neighbors(self, point: tuple[int, int]) -> int:
        rows, cols = self.size[1], self.size[0]
        neighbor_indices = [
            (point[1] - 1, point[0] - 1), (point[1] - 1, point[0]), (point[1] - 1, point[0] + 1),
            (point[1], point[0] - 1), (-1, -1), (point[1], point[0] + 1),
            (point[1] + 1, point[0] - 1), (point[1] + 1, point[0]), (point[1] + 1, point[0] + 1)
        ]
        total_sum = 0
        for r, c in neighbor_indices:
            if 0 <= r < rows and 0 <= c < cols:
                if self.field[r][c].state.value == 2:
                    total_sum += 1

        return total_sum

    def count_on_fire(self):
        count = 0
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.field[y][x].state.value == 2:
                    count += 1
        return count
