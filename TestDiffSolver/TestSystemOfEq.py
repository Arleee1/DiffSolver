import unittest

from SystemOfEq.BinarySystemSolver import BinarySystemSolver


class TestSystemOfEq(unittest.TestCase):
    def testSystem1(self):
        solver = BinarySystemSolver()

        coeffs = ((-9, 4), (4, -9))
        res = solver.solve_system(coeffs)

        self.assertTrue(-5 in res.eigen_values)
        self.assertTrue(-13 in res.eigen_values)

        self.assertAlmostEqual(-1, res.eigen_vectors[0][0]/res.eigen_vectors[0][1], places=5)
        self.assertAlmostEqual(1, res.eigen_vectors[1][0] / res.eigen_vectors[1][1], places=5)

    def testGetRes(self):
        solver = BinarySystemSolver()

        coeffs = ((7, 16), (-4, 7))
        res = solver.solve_system(coeffs)

        for i in range(2):
            print(f"vector{i}: ({res.eigen_vectors[i][0]}, {res.eigen_vectors[i][1]}), eigen value{i}: {res.eigen_values[i]}")
