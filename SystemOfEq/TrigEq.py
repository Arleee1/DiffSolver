class TrigEq:
    def __init__(self, sin_coeff_inner=None, sin_coeff_outer=None, cos_coeff_inner=None, cos_coeff_outer=None):
        self.sin_coeff_inner: float = sin_coeff_inner
        self.sin_coeff_outer: float = sin_coeff_outer
        self.cos_coeff_inner: float = cos_coeff_inner
        self.cos_coeff_outer: float = cos_coeff_outer

    def __str__(self):
        res = ""
        if self.sin_coeff_outer != 0:
            res += f"""{self.sin_coeff_outer if self.sin_coeff_outer != 1 else ""}sin({self.sin_coeff_inner}t)"""
        if self.cos_coeff_outer != 0:
            res += f""" {"+" if self.cos_coeff_outer >= 0 else "-"} """ if res != "" else ""
            res += f"""{abs(self.cos_coeff_outer) if abs(self.cos_coeff_outer) != 1 else ""}cos({self.cos_coeff_inner}t)"""
        return res

