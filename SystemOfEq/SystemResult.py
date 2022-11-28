from typing import Tuple

import numpy


class SystemResult:
    def __init__(self):
        self.complex: bool = None

        self.eigen_values: Tuple[float, float] = None
        self.eigen_vectors: Tuple[Tuple[float, float], Tuple[float, float]] = None

        self.complex_eigen_values: Tuple[numpy.complex, numpy.complex] = None
        self.complex_eigen_vectors: Tuple[Tuple[numpy.complex, numpy.complex], Tuple[numpy.complex, numpy.complex]] = None

    def __str__(self):
        if self.complex:
            raise ValueError("Cannot get string from complex, convert to Euler first")

        get_sol = lambda vec, val, i: f"C{i}[{vec[0]}, {vec[0]}]e^({val}t)"

        res = f"{get_sol(self.eigen_vectors[0], self.eigen_values[0], 1)} + {get_sol(self.eigen_vectors[1], self.eigen_values[1], 2)}"
        return res
