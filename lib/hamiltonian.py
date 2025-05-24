import numpy as np

from .basis import *


class Hamiltonian:
    # basis: one-body basis structure
    # g: pairing-interaction strength
    def __init__(self, basis: Basis, g: float = 0.1):
        self.basis = basis
        self.NMO = self.basis.NMO
        self.g = g

    # calculate <Df|H|Di>
    def get_matrix_element(self, Df: Det, Di: Det) -> float:
        D = get_excite_det(Df, Di, self.NMO)  # different part of Df and Di
        diff = D.occupation_number  # number of different orbitals of Df and Di
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
