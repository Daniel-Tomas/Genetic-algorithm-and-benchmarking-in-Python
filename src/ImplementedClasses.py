from src import AbstractClasses
import random
import numpy as np

from src.Genome import Genome
from src.Population import Population


class UniformSelectionOperator(AbstractClasses.SelectionOperator):
    """Basic class

    This class inherits from the abstract class 'SelectionOperator'.

    Attributes:
        population (Population): Object which contains a list of genomes.

    Args:
        population_ (Population): Population to be set.
    """

    def __init__(self, population_):
        self.population = population_

    def apply(self, target):
        """Select two random genomes from current_population different between the other one, the target and
        the best.

        Args:
            target (Genome): Genome object selected to work with.

        Returns:
            donors (array) : Contains the best genome and two different genomes obtained randomly from the population.
        """

        donors = [target]
        best = self.population.collection[0]
        donors.append(best)

        for _ in range(2):
            genome = random.choice(self.population.collection)
            while genome in donors:
                genome = random.choice(self.population.collection)
            donors.append(genome)
        donors.remove(target)
        return donors


class Rand1MutationOperator(AbstractClasses.MutationOperator):
    """Basic class

    This class inherits from the abstract class 'MutationOperator'.

    Attributes:
        population (Population): Object which contains a list of genomes.
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
                solution.
        F (float): Used as a variable in the mutation operation.
        selector (UniformSelectionOperator): Selects three random genomes.

    Args:
        population_ (Population): Population to be set.
        bounds_ (list): List to be set.
        F_ (float): Float to be set.
    """

    def __init__(self, population_, bounds_, F_=0.5):
        self.population = population_
        self.bounds = bounds_
        self.F = F_
        self.selector = UniformSelectionOperator(population_)

    def apply(self, target):
        """Generate a new genome by combining 'donors'.

       Args:
            target (Genome): Genome object selected to work with.

        Returns:
            Genome (Genome) : Returns the genome resulting from the combination of the three genomes passed as a
            parameter in the 'donors' array.
        """
        donors = self.selector.apply(target)
        mutant_array = donors[0].array + self.F * (donors[1].array - donors[2].array)
        for i in range(len(self.bounds)):
            min_ = self.bounds[i][0]
            max_ = self.bounds[i][1]
            if mutant_array[i] < min_:
                mutant_array[i] = min_
            elif mutant_array[i] > max_:
                mutant_array[i] = max_

        return Genome(array=mutant_array, fitness=None)


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    """Basic class

    This class inherits from the abstract class 'CrossoverOperator'.

    Attributes:
        minfun (function): Function used to calculate the fitness of a genome.
        CR (float): This parameter will be used as a condition to continue doing the crossover operation.

    Args:
        minfun (function): Function to be set.
        CR (float): float to be set.
    """

    def __init__(self, minfun, CR=0.1):
        self.minfun = minfun
        self.CR = CR

    def apply(self, target, mutant):
        """Returns a new candidate by mixing 'target' and 'mutant'.

        Args:
            target (Genome): Genome object selected to work with.
            mutant (Genome): The genome which we are going to combine with 'target'.

        Returns:
            Genome (Genome) : Is the genome resulting from the combination between 'target' and 'mutant'.
        """
        size = len(target.array)
        j = random.randint(0, size - 1)
        candidate = Genome(array=target.array)

        candidate.array[j] = mutant.array[j]
        j = (j + 1) % size
        i = 1
        while i < size and random.random() < self.CR:
            candidate.array[j] = mutant.array[j]
            j = (j + 1) % size
            i = i + 1

        return Genome(array=candidate.array, fitness=self.minfun(candidate.array))


class ElitistReplacementOperator(AbstractClasses.ReplacementOperator):
    """Basic class

    This class inherits from the abstract class 'ReplacementOperator'.
    """

    def apply(self, current_population, candidate_population):
        """
        Each genome of 'current_population' is compared with the genome which is in the same position than
        'candidate_population' and the one with the best fitness of these two genomes is added to
        'result_population'.

        Args:
            current_population (Population): Object which contains a list of genomes.
            candidate_population (list): List which contains a list of genomes.

        Returns:
            result_population (Population) : Resulting population with the best fitness in each position.
        """
        result_population = Population(None, None, 0)
        for target, candidate in zip(current_population.collection, candidate_population.collection):
            result_population.add(candidate if candidate.fitness < target.fitness else target)

        return result_population
