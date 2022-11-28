from math import gcd
from typing import Tuple
import numpy as N

from SystemOfEq.ComplexResult import ComplexResult
from SystemOfEq.SystemResult import SystemResult
from SystemOfEq.TrigEq import TrigEq


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

    def euler_simplify(self, res: SystemResult) -> ComplexResult:
        if not res.complex:
            raise ValueError("Euler simplify must be called on a complex result!")

        complex_res = ComplexResult()

        inner_coeff: float = abs(N.imag(res.complex_eigen_values[0]))
        exponent: float = N.real(res.complex_eigen_values[0])
        c: float = N.real(res.complex_eigen_vectors[0][0])
        d: float = abs(N.imag(res.complex_eigen_vectors[0][0]))
        e: float = N.real(res.complex_eigen_vectors[0][1])
        f: float = -abs(N.imag(res.complex_eigen_vectors[0][1]))

        vector0: Tuple[TrigEq, TrigEq] = (TrigEq(sin_coeff_inner=inner_coeff, cos_coeff_inner=inner_coeff), TrigEq(sin_coeff_inner=inner_coeff, cos_coeff_inner=inner_coeff))
        vector1: Tuple[TrigEq, TrigEq] = (TrigEq(sin_coeff_inner=inner_coeff, cos_coeff_inner=inner_coeff), TrigEq(sin_coeff_inner=inner_coeff, cos_coeff_inner=inner_coeff))

        vector0[0].cos_coeff_outer = c
        vector0[0].sin_coeff_outer = -d
        vector0[1].cos_coeff_outer = e
        vector0[1].sin_coeff_outer = -f

        vector1[0].sin_coeff_outer = c
        vector1[0].cos_coeff_outer = d
        vector1[1].sin_coeff_outer = e
        vector1[1].cos_coeff_outer = f

        complex_res.complex_e_power = exponent

        if d > 0:
            complex_res.complex_vectors = (vector0, vector1)
        else:
            complex_res.complex_vectors = (vector1, vector0)

        return complex_res
