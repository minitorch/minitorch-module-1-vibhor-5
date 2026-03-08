"""Collection of the core mathematical operators used throughout the code base."""

import math
from functools import reduce
# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    """Multiptly two numbers"""
    return x * y


def id(x: float) -> float:
    """Return input"""
    return x


def add(x: float, y: float) -> float:
    """Add two numbers"""
    return x + y


def neg(x: float) -> float:
    """Return Negative of input"""
    return -x


def lt(x: float, y: float) -> float:
    """Less than"""
    return float(x < y)


def eq(x: float, y: float) -> float:
    """Equality comparison"""
    return float(x == y)


def max(x: float, y: float) -> float:
    """Max of two numbers"""
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    """Two numbers close to each other"""
    return float(abs(x - y) < 1e-2)


def sigmoid(x: float) -> float:
    """Sigmoid activation function"""
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))


def relu(x: float) -> float:
    """ReLU activation function"""
    return x if x > 0 else 0.0


def log(x: float) -> float:
    """Natural logarithm of number"""
    return math.log(x)


def exp(x: float) -> float:
    """Exponential of number"""
    return math.exp(x)


def inv(x: float) -> float:
    """Reciprocal of x"""
    return 1 / x


def log_back(x: float, d: float) -> float:
    r"""$log(x)*d$"""
    return (1 / x) * d


def inv_back(x: float, d: float) -> float:
    r"""$d/x$"""
    return -1 / (x * x) * d


def relu_back(x: float, d: float) -> float:
    """D if x>0 else 0"""
    return d if x > 0 else 0.0


## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

# TODO: Implement for Task 0.3.
def negList(ls: list[float]) -> list[float]:
    """Negate a list of numbers"""
    return [neg(x) for x in ls]

def addLists(ls1: list[float], ls2: list[float]) -> list[float]:
    """Add two lists of numbers together"""
    return [add(x, y) for x, y in zip(ls1, ls2)]

def sum(ls: list[float]) -> float:
    """Sum a list of numbers"""
    if len(ls) == 0:
        return 0.0
    return reduce(lambda x,y:x+y, ls) 

def prod(ls:list[float])-> float:
    """Products of all numbers in a list"""
    if len(ls) == 0:
        return 0.0
    return reduce(lambda x,y:x*y,ls)

