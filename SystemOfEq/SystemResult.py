from typing import Tuple

import numpy


class SystemResult:
    def __init__(self):
        self.eigen_values: Tuple[numpy.complex, numpy.complex] = None
        self.eigen_vectors: Tuple[Tuple[numpy.complex, numpy.complex], Tuple[numpy.complex, numpy.complex]] = None
