import unittest

from SystemOfEq.BinarySystemSolver import BinarySystemSolver
from SystemOfEq.ComplexResult import ComplexResult
from SystemOfEq.SystemResult import SystemResult


class TestSystemOfEq(unittest.TestCase):
    def testSystem1(self):
        solver = BinarySystemSolver()

        coeffs = ((-9, 4), (4, -9))
        res = solver.solve_system(coeffs)

        self.assertEqual(-13, res.eigen_values[0])
        self.assertEqual(-5, res.eigen_values[1])

        self.assertFalse(res.complex)

        self.assertAlmostEqual(-1, res.eigen_vectors[0][0]/res.eigen_vectors[0][1], places=5)
        self.assertAlmostEqual(1, res.eigen_vectors[1][0] / res.eigen_vectors[1][1], places=5)

    def testComplexRes(self):
        solver = BinarySystemSolver()
        coeffs = ((1, -1), (5, -3))

        res = solver.solve_system(coeffs)

        self.assertTrue(res.complex)

        self.assertEqual(-1-1j, res.complex_eigen_values[0])
        self.assertEqual(-1+1j, res.complex_eigen_values[1])

        self.assertEqual(2+1j, res.complex_eigen_vectors[0][1]/res.complex_eigen_vectors[0][0])
        self.assertEqual(2-1j, res.complex_eigen_vectors[1][1]/res.complex_eigen_vectors[1][0])

    def testEulerSimplify(self):
        solver = BinarySystemSolver()

        resIn = SystemResult()
        resIn.complex_eigen_values = (-1-1j, -1+1j)
        resIn.complex_eigen_vectors = ((1, 2+1j), (1, 2-1j))
        resIn.complex = True

        res: ComplexResult = solver.euler_simplify(resIn)

        self.assertEqual(-1, res.complex_e_power)

        ind0 = 0 if res.complex_eigen_vectors[0][0].cos_coeff_outer == 1 else 1
        vector0: ComplexResult = res.complex_eigen_vectors[ind0]
        vector1: ComplexResult = res.complex_eigen_vectors[1-ind0]

        self.assertEqual(2, vector0[1].cos_coeff_outer/vector0[0].cos_coeff_outer)
        self.assertEqual(0, vector0[0].sin_coeff_outer)
        self.assertEqual(2, vector0[1].cos_coeff_outer/vector0[1].sin_coeff_outer)
        self.assertEqual(1, vector0[0].cos_coeff_inner)
        self.assertEqual(1, vector0[0].sin_coeff_inner)
        self.assertEqual(1, vector0[1].cos_coeff_inner)
        self.assertEqual(1, vector0[1].sin_coeff_inner)

        self.assertEqual(2, vector1[1].sin_coeff_outer / vector1[0].sin_coeff_outer)
        self.assertEqual(0, vector1[0].cos_coeff_outer)
        self.assertEqual(-2, vector1[1].sin_coeff_outer / vector1[1].cos_coeff_outer)
        self.assertEqual(1, vector1[0].cos_coeff_inner)
        self.assertEqual(1, vector1[0].sin_coeff_inner)
        self.assertEqual(1, vector1[1].cos_coeff_inner)
        self.assertEqual(1, vector1[1].sin_coeff_inner)

    def testComplexThrows(self):
        solver = BinarySystemSolver()

        res = SystemResult()
        res.complex = False

        self.assertRaises(ValueError, lambda: solver.euler_simplify(res))
