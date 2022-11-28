from typing import Tuple

from SystemOfEq.TrigEq import TrigEq


class ComplexResult:
    def __init__(self):
        self.complex_e_power: float = None
        self.complex_vectors: Tuple[Tuple[TrigEq, TrigEq], Tuple[TrigEq, TrigEq]] = None