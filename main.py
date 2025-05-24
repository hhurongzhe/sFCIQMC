import numpy as np
import matplotlib.pyplot as plt

from lib.util import *
from lib.orbit import *
from lib.basis import *
from lib.hamiltonian import *
from lib.fci import *
from lib.fciqmc import *


params = {}
params["warm_up_walkers"] = [1e5]
params["d_tau"] = 1e-4
params["A"] = 10
params["xi"] = 0.1
params["steps"] = 3000
params["initiator_threshold"] = 3
params["seed"] = 0


def main():
    p_max = 4
    delta, g = 1, 1
    basis = Basis(p_max, delta)
    hamiltonian = Hamiltonian(basis, g)
    fciqmc = FCIQMC(basis, hamiltonian, params)
    fciqmc.warm()
    print("sFCIQMC terminated successfully!")


if __name__ == "__main__":
    main()
