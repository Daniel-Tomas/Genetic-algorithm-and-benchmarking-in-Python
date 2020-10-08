from group14.Genome import Genome


class Population:
    def __init__(self, collection):
        self.collection = collection

    def __repr__(self):
        """
        It casts ...
        Returns:
             str: The population in string format
        """
        res = '[ '
        for elem in self.collection:
            res += f'[ {elem.array}, {elem.fitness} ], '
        return res

    def ascendent_sort(self):
        self.collection.sort(key=lambda x: x.fitness)

    def descendent_sort(self):
        self.collection.sort(key=lambda x: x.fitness, reverse=True)

    def add(self, genome):
        """
        Args:
            genome:
        """
        self.collection.append(genome)

    def remove(self, genome):
        """Excepcion en caso de que no esté el elemento a elminar

        Args:
            genome:
        """
        # for elem in self.collection:
        #     if elem == genome:
        self.collection.remove(genome)

    def replace(self, genome):
        """Excepcion en caso de que no esté el elemento a elminar

        Args:
            genome:
        """
        # for elem in self.collection:
        #     if elem == genome:
        self.remove(genome)
        self.add(genome)


genome1 = Genome([1, 33, 4], 3)
genome2 = Genome([1, 33, 5], 4)
genome3 = Genome([2, 33, 4], 1)

genome4 = Genome([2, 33, 4], -1)

prueba = Population([genome1, genome2, genome3])
prueba.ascendent_sort()

prueba.add(genome4)
print(prueba)

prueba.remove(genome2)
print(prueba)
