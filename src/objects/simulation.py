from src.objects.forest import Forest
from src.utils.drawer import draw_forest


class Simulation:
    forest: Forest
    init_arsons: int
    p: float

    def __init__(self, size: tuple[int, int], init_arsons: int, p: float):
        self.forest = Forest(size)
        self.init_arsons = init_arsons
        self.p = p

    def simulate(self):
        generation = 1
        self.forest.setup_fire(self.init_arsons)
        img = draw_forest([[forest.state.value for forest in row] for row in self.forest.field], 50)
        img.show()
        print(f'Generation {generation}:', self.forest.field)
        while self.forest.count_on_fire() > 0:
            generation += 1
            self.forest.next_generation(p=self.p)
            img = draw_forest([[forest.state.value for forest in row] for row in self.forest.field], 50)
            img.show()
            print(f'Generation {generation}:', self.forest.field)
