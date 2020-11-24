from abc import ABC, abstractmethod


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, target):
        """
        Args:
            target (Genome): Genome object selected to work it.
        """
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, target):
        """
         Args:
            target (Genome): Genome object selected to work it.
        """
        ...


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, target, mutant):
        """
        Args:
            target (Genome): Genome class object selected to work it.
            mutant (Genome): The genome which we are going to combine with 'target'.
        """
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, current_population, candidate_population):
        """
        Args:
            current_population (Population): Object which contains a list of genomes.
            candidate_population (list): List which contains a the candidates genomes.
        """
        ...
