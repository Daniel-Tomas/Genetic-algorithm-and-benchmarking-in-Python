from abc import ABC, abstractmethod


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, target, population):
        """
        Args:
            target (Genome): Genome class object selected.
            population (Population): Object which contains a list of genomes.
        """
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, target, population):
        """
         Args:
            target (Genome): Genome class object selected.
            population (Population): Object which contains a list of genomes.
        """
        ...


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, target, mutant):
        """
        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            target (Genome): Genome class object selected.
            mutant (Genome): The genome which we are going to combine with 'target'.
        """
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, population, candidate_population):
        """
        Args:
            current_population (Population): Object which contains a list of genomes.
            candidate_population (list): List which contains a list of genomes.
        """
        ...
