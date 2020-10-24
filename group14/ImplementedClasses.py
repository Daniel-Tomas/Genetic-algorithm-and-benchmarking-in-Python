from group14 import AbstractClasses
import random
import numpy as np

from group14.Genome import Genome


class UniformSelectionOperator(AbstractClasses.SelectionOperator):
    # TODO: Añadir comentarios a las funciones cambiadas, sobre todo a los constructores de dichas funciones.
    # TODO: comprobar correcto funcionamiento del algoritmo y comentar clase EA ya que ahora devuelve el mejor genoma

    """Basic class

    This class inherits from the abstract class 'SelectionOperator'.
    """

    def apply(self, target, population):
        """Select three random genomes of population different from each other and from the target.

        Args:
            target (Genome): Genome object selected to work it.
            population (Population): Object which contains a list of genomes.

        Returns:
            donors (array) : Contains three different genomes obtained randomly from 'population'.
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
    """

    def __init__(self, F=0.5):
        self.F = F

    def apply(self, donors, bounds):
        """Generate a new genome by combining 'donors'.

        Args:
            donors (array): Contains three different genomes.
            bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
                solution.

        Returns:
            Genome (Genome) : Returns the genome resulting from the combination of the three genomes passed as a
                parameter in the 'donors' array.
        """
        mutant_array = []
        i = 0
        for i in range(len(bounds)):
            min_ = bounds[i][0]
            max_ = bounds[i][1]
            subtract_res = donors[1].array[i] - donors[2].array[i]
            multiplication_res = self.F * subtract_res
            addition_res = donors[0].array[i] + multiplication_res
            if (addition_res < min_):
                addition_res = min_
            elif (addition_res > max_):
                addition_res = max_
            mutant_array = np.append(mutant_array, addition_res)
        return Genome(array=mutant_array, fitness=0)


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    """Basic class

    This class inherits from the abstract class 'CrossoverOperator'.

    Attributes:
            minfun (function): Function used to calculate the fitness of a genome.
            CR (float): This parameter will be used as a condition to continue doing the crossover operation.
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
            Genome (Genome) : It is the genome resulting from the combination between 'target' and 'mutant'.
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

    def apply(self, population, target, candidate):
        """Include in 'population' the genome with the best fitness between 'target' and 'candidate'

        Args:
            population (Population): Object which contains a list of genomes.
            target (Genome): Genome object selected to work it.
            candidate (Genome): Candidate to have better fitness than our 'target' genome.
        """
        if candidate.fitness < target.fitness:
            population.replace(target, candidate)
