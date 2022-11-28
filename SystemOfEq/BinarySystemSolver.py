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
        determinant = N.subtract(N.square(N.add(a, d)), N.multiply(4, N.subtract(N.multiply(a, d), N.multiply(b, c))))
        right = N.sqrt((0j if determinant < 0 else 0) + determinant)
        right = N.divide(right, 2)

        eigen_value0 = N.subtract(left, right)
        eigen_value1 = N.add(left, right)

        res.complex = determinant < 0

        if (res.complex and N.imag(eigen_value0) < N.imag(eigen_value1)) or not res.complex and eigen_value0 < eigen_value1:
            eigen_values = (eigen_value0, eigen_value1)
        else:
            eigen_values = (eigen_value1, eigen_value0)

        if not res.complex:
            res.eigen_values = eigen_values
        else:
            res.complex = True
            res.complex_eigen_values = eigen_values

        eigen_vector0 = (N.multiply(-1, b), N.subtract(a, eigen_values[0]))
        eigen_vector1 = (N.multiply(-1, b), N.subtract(a, eigen_values[1]))

        if not res.complex:
            res.eigen_vectors = (eigen_vector0, eigen_vector1)
        else:
            res.complex_eigen_vectors = (eigen_vector0, eigen_vector1)

        return res
