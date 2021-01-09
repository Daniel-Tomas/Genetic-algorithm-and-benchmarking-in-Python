import numpy as np

# Wrapper to allow using these functions with several libraries providing data in different formats
def f_wrap(x, func):
    if isinstance(x, list):
        return func(x)
    if isinstance(x, np.ndarray):
        if x.ndim == 1:
            return func(x)
        else:
            return np.array([func(x[i]) for i in range(x.shape[0])])
    else:
        return func(x),

# F1: Sphere function
def _sphere(x):
    return np.sum(np.power(x, 2))

def sphere(x):
    return f_wrap(x, _sphere)

# F2: Ackley function
def _ackley(x):
    dim = len(x)
    sum1 = 0.0
    sum2 = 0.0

    for n in range(0, dim):
        z = np.abs(x[n])
        sum1 += pow(z, 2)
        sum2 += np.cos(2 * np.pi * z)

    return -20 * np.exp(-0.2 * np.sqrt(sum1 / dim)) - np.exp(sum2 / dim) + 20 + np.e

def ackley(x):
    return f_wrap(x, _ackley)

# F3: Rosenbronck function
def _rosenbrock(x):
    F = 0.0
    z = [abs(x[n] + 1) for n in range(len(x))]

    for n in range(0, len(x) - 1):
        F += 100 * (pow((pow(z[n], 2) - z[n + 1]), 2)) + pow((z[n] - 1), 2)

    return F

def rosenbrock(x):
    return f_wrap(x, _rosenbrock)

# F4: Rastrigin function
def _rastrigin(x):
    F = 0.0
    for n in range(0, len(x)):
        z = x[n]
        F += (pow(z, 2) - 10 * np.cos(2 * np.pi * z) + 10)

    return F

def rastrigin(x):
    return f_wrap(x, _rastrigin)

# F5: Griewank function
def _griewank(x):
    F1 = 0.0
    F2 = 0.0

    for n in range(0, len(x)):
        z = abs(x[n])
        F1 += (pow(z, 2) / 4000)
        F2 *= (np.cos(z / np.sqrt(n + 1)))

    return F1 - F2 + 1

def griewank(x):
    return f_wrap(x, _griewank)

# F6: Schwefel 2.21 problem
def _schwefel_2_21(x):
    F = abs(x[0])

    for n in range(1, len(x)):
        z = x[n]
        F = max(F, abs(z))

    return F

def schwefel_2_21(x):
    return f_wrap(x, _schwefel_2_21)

# F7: Schwefel 2.22 problem
def _schwefel_2_22(x):
    sum_ = 0.0
    prod = 1.0

    for n in range(0, len(x)):
        val = abs(x[n])    
        sum_ += val
        prod *= val

    return sum_ + prod

def schwefel_2_22(x):
    return f_wrap(x, _schwefel_2_22)

# F8: Schwefel 1.2 problem
def _schwefel_1_2(x):
    sum_ = 0.0
    val  = 0.0

    for n in range(0, len(x)):
        val  += x[n]
        sum_ += val * val

    return sum_

def schwefel_1_2(x):
    return f_wrap(x, _schwefel_1_2)

# F9: Extended f10 function
def f_10(x, y):
    p = (x*x + y*y)
    z = pow(p, 0.25)
    t = np.sin(50.0 * pow(p, 0.1))
    t = t*t + 1.0

    return z*t

def _extended_f_10(x):
    sum_ = f_10(x[len(x)-1], x[0])

    for n in range(0, len(x)-1):
        sum_ += f_10(x[n], x[n+1])

    return sum_

def extended_f_10(x):
    return f_wrap(x, _extended_f_10)

# F10: Bohachevsky function
def _bohachevsky(x):
    sum_ = 0.0
    currentGen = x[0]

    for n in range(1, len(x)):
        nextGen = x[n]
        sum_ += currentGen * currentGen + 2.0 * nextGen * nextGen
        sum_ += -0.3 * np.cos (3.0 * np.pi * currentGen) - 0.4 * np.cos (4.0 * np.pi * nextGen) + 0.7
        currentGen = nextGen

    return sum_

def bohachevsky(x):
    return f_wrap(x, _bohachevsky)

# F11: Schaffer function
def _schaffer(x):
    sum_ = 0.0
    currentGen = x[0]
    currentGen = currentGen * currentGen

    for n in range(1, len(x)):
        nextGen = x[n]
        nextGen = nextGen * nextGen
        aux = currentGen + nextGen
        currentGen = nextGen
        aux2  = np.sin(50.0 * pow(aux, 0.1))
        sum_ += pow(aux, 0.25) * (aux2 * aux2 + 1.0)

    return sum_

def schaffer(x):
    return f_wrap(x, _schaffer)
