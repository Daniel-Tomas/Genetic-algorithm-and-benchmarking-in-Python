from src.EA import EA
import sys
from benchmarks.functions import *
import pyade.sade as sade
import pprint
from scipy.stats import kruskal
from scipy.stats import friedmanchisquare
import pandas as pd
import scikit_posthocs as sp


class Logger():
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('benchmarking.out', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()

benchmark = [sphere, ackley, rosenbrock, rastrigin, griewank, schwefel_2_21,
             schwefel_2_22, schwefel_1_2, extended_f_10, bohachevsky, schaffer]


def run_SADE(bounds, probsize, popsize, func, iters, reps):
    params = sade.get_default_params(dim=probsize)

    params['bounds'] = np.array([[bounds[0], bounds[1]]] * probsize)
    params['max_evals'] = popsize * iters
    params['population_size'] = popsize
    params['func'] = func

    results = []

    for i in range(reps):
        _, fitness = sade.apply(**params)
        results.append(fitness)

    return results


def run_basic_DE(bounds, probsize, popsize, func, iters, reps):
    results = []

    for i in range(reps):
        DE = EA(func, [bounds for _ in range(probsize)], popsize)
        DE.run(iters)
        results.append(DE.best().fitness)

    return results


params = {'bounds': (-100, 100), 'probsize': 10, 'popsize': 50, 'iters': 250, 'reps': 50}

print('\n----------------------------------------RESULTS BASIC DE-------------------------------------------')
results_basic_DE = {}

for func in benchmark:
    results_basic_DE[func.__name__] = run_basic_DE(params['bounds'], params['probsize'], params['popsize'], func,
                                                   params['iters'], params['reps'])

pp = pprint.PrettyPrinter(indent=3)
pp.pprint(results_basic_DE)

print('\n----------------------------------------RESULTS SADE-------------------------------------------')
results_SADE = {}

for func in benchmark:
    results_SADE[func.__name__] = run_SADE(params['bounds'], params['probsize'], params['popsize'], func,
                                           params['iters'], params['reps'])

pp.pprint(results_SADE)

print('\n-----------------------------------------KRUSKAL TEST------------------------------------')
for func in benchmark:
    f = func.__name__
    res = kruskal(results_basic_DE[f], results_SADE[f])
    print("Results for the " + f + " function: " + str(res.pvalue))

print('\n-----------------------------------------MEAN FITNESS PER FUNCTION-----------------------------------')
algNames = ["DE", "SADE"]
results_avg = {}

for n in algNames:
    results_avg[n] = []

for func in benchmark:
    f = func.__name__
    results_avg["DE"].append(np.mean(results_basic_DE[f]))
    results_avg["SADE"].append(np.mean(results_SADE[f]))

pp.pprint(results_avg)
# print('\n-----------------------------------------FRIEDMAN TEST-----------------------------------')
# friedmanchisquare(results_avg["DE"], results_avg["SADE"])

print('\n-----------------------------------------MANN-WHITNEY TEST WITH HOLM-----------------------------------')
data = pd.DataFrame({"algs": ["DE"] * len(results_avg["DE"]) +
                             ["SADE"] * len(results_avg["SADE"]),
                     "vals": results_avg["DE"] +
                             results_avg["SADE"]})

sp.posthoc_wilcoxon(data, val_col='vals', group_col='algs', p_adjust='holm')
