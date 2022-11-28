from typing import Tuple

import numpy

from SystemOfEq.TrigEq import TrigEq


class SystemResult:
    def __init__(self):
        self.complex: bool = None

        self.eigen_values: Tuple[float, float] = None
        self.eigen_vectors: Tuple[Tuple[float, float], Tuple[float, float]] = None

        self.complex_eigen_values: Tuple[numpy.complex, numpy.complex] = None
        self.complex_eigen_vectors: Tuple[Tuple[numpy.complex, numpy.complex], Tuple[numpy.complex, numpy.complex]] = None
