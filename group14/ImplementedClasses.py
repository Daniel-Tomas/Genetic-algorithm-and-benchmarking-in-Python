from group14 import AbstractClasses


class UniformSelectionOperator(AbstractClasses.SelectionOperator):
    def apply(self, target, population):
        pass


class Rand1MutationOperator(AbstractClasses.MutationOperator):
    def apply(self, target, population):
        pass


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    def apply(self, target, mutant):
        pass


class ElitistReplacementOperator(AbstractClasses.ReplacementOperator):
    def apply(self, population, target, candidate):
        pass
