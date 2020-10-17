from group14.ImplementedClasses import *
from group14.Population import Population


class EA(object):
    """docstring for EA
    """

    def __init__(self, minfun, bounds, p_size):
        self.minfun = minfun
        self.population = Population(minfun, bounds, p_size)

    def run(self, iterations):
        for _ in range(0, iterations):
            for target in self.population:
                # List with genomes
                donors = UniformSelectionOperator.apply(target, self.population)
                # Genome
                mutant = Rand1MutationOperator.apply(self.minfun, donors)
                # Genome
                candidate = ExponentialCrossoverOperator.apply(self.minfun, target, mutant)
                # TODO: Mirar si esta bien hecho el paso por parametros
                ElitistReplacementOperator.apply(self.population, target, candidate)


if __name__ == '__main__':
    def f(sol):
        return sum(sol)


    mybounds = [(0, 1)] * 10

    myEA = EA(f, mybounds, 50)

    myEA.run(1000)
