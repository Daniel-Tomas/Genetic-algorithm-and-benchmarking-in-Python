from group14 import AbstractClasses
import random
import numpy as np

from group14.Genome import Genome
from group14.Population import Population


class UniformSelectionOperator(AbstractClasses.SelectionOperator):
    # TODO: Añadir comentarios a las funciones cambiadas, sobre todo a los constructores de dichas funciones.
    # TODO: comprobar correcto funcionamiento del algoritmo y comentar clase EA ya que ahora devuelve el mejor genoma

    """Basic class

    This class inherits from the abstract class 'SelectionOperator'.
    """

    def apply(self, target, population):
        """Select three random genomes of current_population different from each other and from the target.

        Args:
            target (Genome): Genome object selected to work it.
            population (Population): Object which contains a list of genomes.

        Returns:
            donors (array) : Contains three different genomes obtained randomly from 'current_population'.
        """

        donors = [target]

        for _ in range(3):
            genome = random.choice(population.collection)
            while genome in donors:
                genome = random.choice(population.collection)
            donors.append(genome)

        donors.remove(target)
        return donors


class Rand1MutationOperator(AbstractClasses.MutationOperator):
    """Basic class

    This class inherits from the abstract class 'MutationOperator'.

    Attributes:
        F (float): Will be used as an element in the mutation operation.
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
                solution.

    Args:
        F_ (float): Float to be set.
        bounds_ (list): Bounds to be set.
    """

    def __init__(self, bounds_, F_=0.5):
        self.bounds = bounds_
        self.F = F_
        self.selector = UniformSelectionOperator()

    def apply(self, target, population):
        """Generate a new genome by combining 'donors'.

       Args:
            target (Genome): Genome object selected to work it.
            population (Population): Object which contains a list of genomes.

        Returns:
            Genome (Genome) : Returns the genome resulting from the combination of the three genomes passed as a
            parameter in the 'donors' array.
        """
        donors = self.selector.apply(target, population)
        mutant_array = []
        for i in range(len(self.bounds)):
            min_ = self.bounds[i][0]
            max_ = self.bounds[i][1]
            subtract_res = donors[1].array[i] - donors[2].array[i]
            multiplication_res = self.F * subtract_res
            addition_res = donors[0].array[i] + multiplication_res
            if addition_res < min_:
                addition_res = min_
            elif addition_res > max_:
                addition_res = max_
            mutant_array = np.append(mutant_array, addition_res)
        return Genome(array=mutant_array, fitness=0)


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    """Basic class

    This class inherits from the abstract class 'CrossoverOperator'.

    Attributes:
        minfun (function): Function used to calculate the fitness of a genome.
        CR (float): This parameter will be used as a condition to continue doing the crossover operation.

    Args:
        minfun (function): Function to be set.
        CR (float): float tu be set.
    """

    def __init__(self, minfun, CR=0.1):
        self.minfun = minfun
        self.CR = CR

    def apply(self, target, mutant):
        """Returns a new candidate by mixing 'target' and 'mutant'.

        Args:
            target (Genome): Genome object selected to work it.
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
        Each genome of 'current_population' is compared with the genome that is in the same position within
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
