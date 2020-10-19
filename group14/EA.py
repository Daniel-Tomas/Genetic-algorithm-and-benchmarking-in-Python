from group14.ImplementedClasses import *
from group14.Population import Population


class EA(object):
    """docstring for EA
    """

    def __init__(self, minfun, bounds, p_size):
        self.minfun = minfun
        self.bounds = bounds
        self.population = Population(minfun, bounds, p_size)

    def run(self, iterations):
        print(f'Antes:\n {self.population}\n')

        selector = UniformSelectionOperator()
        mutator = Rand1MutationOperator()
        mixer = ExponentialCrossoverOperator()
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
            for target in self.population.collection:
                # List with genomes who will be the donors
                donors = selector.apply(target, self.population)
                # Genome modified (mutant)
                mutant = mutator.apply(self.minfun, donors, self.bounds)
                # Genome modified by replacing a few random positions
                candidate = mixer.apply(self.minfun, target, mutant)
                # TODO: Mirar si esta bien hecho el paso por parametros
                # target is replaced by candidate from the population if candidate has less fitness than target
                replacer.apply(self.population, target, candidate)

        print(f'Despues:\n {self.population}\n')


if __name__ == '__main__':
    def f(sol):
        return sum(sol)


    mybounds = [(0, 10), (10, 20), (20, 30), (30, 40)]

    myEA = EA(f, mybounds, 20)

    myEA.run(1000)
