import numpy as np
import random
from typing import Dict, List

from .profiler import *
from .basis import *
from .hamiltonian import *


class FCIQMC:
    def __init__(self, basis: Basis, hamil: Hamiltonian, params: dict):
        self.basis = basis
        self.hamiltonian = hamil
        self.params = params
        self.NMO = self.basis.NMO
        print("TODO: init")

    def warm(self, nw: int):
        print("TODO: warm")

    def start(self):
        print("TODO: start")

    def step(self):
        print("TODO: step")

    def annihilation(self):
        print("TODO: annihilation")


if __name__ == "__main__":
    print("TODO")
