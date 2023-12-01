from src.objects.simulation import Simulation

if __name__ == '__main__':
    simulation = Simulation(size=(3, 3), init_arsons=3, p=0.2)
    simulation.simulate()
