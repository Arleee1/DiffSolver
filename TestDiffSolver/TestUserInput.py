import unittest

from SystemOfEq.BinarySystemSolver import BinarySystemSolver


class TestUserInput(unittest.TestCase):

    def testGetRes(self):
        solver = BinarySystemSolver()

        coeffs = ((3, 7), (-7, 3))
        res = solver.solve_system(coeffs)

        if res.complex:
            res_euler = solver.euler_simplify(res)
            print(res_euler)
        else:
            print(res)
