from src.EA import EA
from benchmarks.functions import *
import statistics as st
import pprint
import sys

benchmark = [sphere, ackley, rosenbrock, rastrigin, griewank, schwefel_2_21,
             schwefel_2_22, schwefel_1_2, extended_f_10, bohachevsky, schaffer]


class Logger():
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('data_analitics.out', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()


def run_basic_DE(bounds, probsize, popsize, func, iters, reps):
    results = []

    for i in range(reps):
        DE = EA(func, [bounds for _ in range(probsize)], popsize)
        DE.run(iters)
        results.append(DE.best().fitness)

    return results


params = {'bounds': (-100, 100), 'probsize': 10, 'popsize': 10, 'iters': 50, 'reps': 10}
results_basic_DE = {}
for func in benchmark:
    results_basic_DE[func.__name__] = run_basic_DE(params['bounds'], params['probsize'], params['popsize'], func,
                                                   params['iters'], params['reps'])


# Data analitics
def get_data_analitics_DE():
    data_analitics_DE = {}
    for fun in results_basic_DE:
        analitics = {}
        values = results_basic_DE.get(fun)
        values.sort()
        mean = st.mean(values)
        analitics['mean'] = mean
        median = st.median(values)
        analitics['median'] = median
        min = values[0]
        analitics['min'] = min
        max = values[-1]
        analitics['max'] = max
        desv_est = st.stdev(values)
        analitics['desv_est'] = desv_est
        data_analitics_DE[fun] = analitics
    return data_analitics_DE


def print_data_analitics_DE():
    data_analitics_DE = get_data_analitics_DE()
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(data_analitics_DE)


print_data_analitics_DE()
