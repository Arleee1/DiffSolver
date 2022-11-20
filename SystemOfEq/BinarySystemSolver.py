from typing import Tuple
import numpy as N


from SystemOfEq.SystemResult import SystemResult


class BinarySystemSolver:

    def solve_system(self, coeffs: Tuple[Tuple[float, float], Tuple[float, float]]) -> SystemResult:

        # TODO - add support for complex solutions using Euler's formula
        a = coeffs[0][0]
        b = coeffs[0][1]
        c = coeffs[1][0]
        d = coeffs[1][1]
        res = SystemResult()

        left = N.add(a, d)
        left = N.divide(left, 2)
        right = N.sqrt(0j + N.subtract(N.square(N.add(a, d)), N.multiply(4, N.subtract(N.multiply(a, d), N.multiply(b, c)))))
        right = N.divide(right, 2)

        res.eigen_values = (N.subtract(left, right), N.add(left, right))

        eigen_vector0 = (N.multiply(-1, b), N.subtract(a, res.eigen_values[0]))
        eigen_vector1 = (N.multiply(-1, b), N.subtract(a, res.eigen_values[1]))

        res.eigen_vectors = (eigen_vector0, eigen_vector1)
        return res
