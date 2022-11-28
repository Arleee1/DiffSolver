from typing import Tuple

from SystemOfEq.TrigEq import TrigEq


class ComplexResult:
    def __init__(self):
        self.complex_e_power: float = None
        self.complex_vectors: Tuple[Tuple[TrigEq, TrigEq], Tuple[TrigEq, TrigEq]] = None

    def __str__(self):
        res: str = f"e^({self.complex_e_power}t)("
        for i, v in enumerate(self.complex_vectors, start=1):
            res += f"""C{i}[{str(v[0])}, {str(v[1])}] + """

        res = res[:-3] + ")"
        return res
