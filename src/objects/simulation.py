from src.objects.forest import Forest
from src.seedwork.drawer import draw_forest
from src.seedwork.display import display_simulation


class Simulation:
    forest: Forest
    init_arsons: int
    p: float

    def __init__(self, size: tuple[int, int], init_arsons: int, p: float):
        self.forest = Forest(size)
        self.init_arsons = init_arsons
        self.p = p

    def simulate(self, visualize=False):
        generation = 1
        self.forest.setup_fire(self.init_arsons)
        images = [draw_forest([[forest.state.value for forest in row] for row in self.forest.field], 25)]
        print(f'Generation {generation}:', self.forest.field)
        while self.forest.count_on_fire() > 0:
            generation += 1
            self.forest.next_generation(p=self.p)
            images.append(draw_forest([[forest.state.value for forest in row] for row in self.forest.field], 25))
            print(f'Generation {generation}:', self.forest.field)
        if visualize:
            display_simulation(images=images, fps=1)
