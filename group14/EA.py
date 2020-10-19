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

        for _ in range(0, iterations):
            for target in self.population.collection:
                # List with genomes
                donors = selector.apply(target, self.population)
                # Genome
                mutant = mutator.apply(self.minfun, donors, self.bounds)
                # Genome
                candidate = mixer.apply(self.minfun, target, mutant)
                # TODO: Mirar si esta bien hecho el paso por parametros
                replacer.apply(self.population, target, candidate)

        print(f'Despues:\n {self.population}\n')


if __name__ == '__main__':
    def f(sol):
        return sum(sol)


    mybounds = [(0, 3)] * 2

    myEA = EA(f, mybounds, 50)

    myEA.run(1000)
