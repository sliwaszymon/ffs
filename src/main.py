from src.objects.simulation import Simulation

if __name__ == '__main__':
    simulation = Simulation(size=(25, 25), init_arsons=3, p=0.3)
    simulation.simulate(visualize=True)
