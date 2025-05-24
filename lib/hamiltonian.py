import numpy as np


from .basis import *


class Hamiltonian:
    def __init__(self, basis: Basis):
        self.basis = basis
        self.NMO = self.basis.one_body_basis_number

    # calculate <Df|H|Di>
    def get_matrix_element(self, Df: Det, Di: Det) -> float:
        D = get_excite_det(Df, Di, self.NMO)
        diff = D.occupation_number
        if diff == 0:
            # diagonal part
            # <D|H|D>, with Df=Di=D
            return 0
        elif diff == 2:
            # single-excitation part
            return 0
        elif diff == 4:
            # double-excitation part
            return 0
        else:
            # cannot happen
            return 0


if __name__ == "__main__":
    print("TODO")
