from abc import ABC, abstractmethod


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        ...


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, collection1, collection2):
        ...
