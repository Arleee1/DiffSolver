class TrigEq:
    def __init__(self, sin_coeff_inner=None, sin_coeff_outer=None, cos_coeff_inner=None, cos_coeff_outer=None):
        self.sin_coeff_inner: float = sin_coeff_inner
        self.sin_coeff_outer: float = sin_coeff_outer
        self.cos_coeff_inner: float = cos_coeff_inner
        self.cos_coeff_outer: float = cos_coeff_outer

    def __str__(self):
        return f"{self.sin_coeff_outer}sin({self.sin_coeff_inner}t) + {self.cos_coeff_outer}cos({self.cos_coeff_inner}t)"
