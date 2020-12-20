from src.ImplementedClasses import *
from src.Population import Population
import random
import numpy as np
from benchmarks import functions as fun

#todo imprimir dos decimales
#todo hacer memoria
#todo pasar a ingles las variables
class EA(object):
    """This class is the entry point to the execution of the algorithm.

    Attributes:
        minfun (function): Function used to calculate the fitness of a genome.
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
            solution.
        population (Population): Object which contains a list of genomes.
        best_genome (Genome): Optimal solution calculated by the algorithm.


    Args:
        minfun_ (function): The function to be set.
        bounds_ (list): List of values to be set.
        p_size (int): Maximum size of our population.
    """

    def __init__(self, minfun_, bounds_, p_size):
        self.minfun = minfun_
        self.bounds = bounds_
        self.population = Population(minfun_, bounds_, p_size)
        self.best_genome = None

    def run(self, iterations):
        """Runs the Differential Evolution algorithm.

        Args:
            iterations (int): Number of iterations to be made by the algorithm.
        """
        print(f'Before:\n {self.population}\n')
        self.best()
        print(f'Best Genome before: {self.best_genome.array}, fitness={self.best_genome.fitness} ')

        mutator = Rand1MutationOperator(self.population, self.bounds, 0.2)
        mixer = ExponentialCrossoverOperator(self.minfun)
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
            candidate_population = Population(None, None, 0)
            for target in self.population.collection:
                # List with genomes who will be the donors
                mutant = mutator.apply(target)
                # Genome modified by replacing a few random positions
                candidate_genome = mixer.apply(target, mutant)

                candidate_population.add(candidate_genome)

            # Targets are replaced by candidates from the population if candidate has less fitness than target
            self.population = replacer.apply(self.population, candidate_population)

        print(f'After:\n {self.population}\n')
        self.best()
        print(f'Best Genome after: {self.best_genome.array}, fitness={self.best_genome.fitness} ')

    def best(self):
        """Returns the best genome

        Returns:
            best_genome (Genome): Optimal solution calculated by the algorithm.
        """
        self.population.descendent_sort()
        self.best_genome = self.population.collection[0]
        return self.best_genome


if __name__ == '__main__':
    def f(array):
        res = 0;
        if (sum(array) > horas_estudio):
            return -np.inf;
        for i in range(len(array)):
            nota = (array[i] * punto_hora[i])
            if (random.random() <= posibilidad_revision[i]):
                nota += nota_revision[i];
            if (nota > 10):
                nota = 10
            res += nota * creditos[i]
        return res / sum(creditos);


    notas_minimas = [3, 4, 5, 2, 1]
    punto_hora = [1, 2, 1, 2, 3]
    creditos = [3, 6, 1, 4, 2]
    posibilidad_revision = [0.4, 0.3, 0.2, 0.5, 0.6]
    nota_revision = [0.5, 0.1, 0.3, 0.4, 0.2]
    horas_estudio = 15
    mybounds = [(notas_minimas[i] / punto_hora[i], 10 / punto_hora[i]) for i in range(len(creditos))]

    myEA = EA(f, mybounds, 20)

    myEA.run(1000)

    myEA.best()
