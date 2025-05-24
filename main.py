import numpy as np
import matplotlib.pyplot as plt

from lib.profiler import *
from lib.utility import *
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
    header_message()
    profiler = Profiler()

    p_max = 4
    delta, g = 1, 1

    section_message("basis setting up")
    t1 = time.time()
    basis = Basis(p_max, delta)
    t2 = time.time()
    profiler.add_timing("set up basis", t2 - t1)

    t1 = time.time()
    section_message("hamiltonian setting up")
    hamiltonian = Hamiltonian(basis, g)
    t2 = time.time()
    profiler.add_timing("set up hamiltonian", t2 - t1)

    section_message("fciqmc algorithm")
    t1 = time.time()
    fciqmc = FCIQMC(basis, hamiltonian, params)
    for nw in params["warm_up_walkers"]:
        fciqmc.warm(nw)
        fciqmc.start()
    t2 = time.time()
    profiler.add_timing("fciqmc algorithm", t2 - t1)

    section_message("Timings")
    profiler.print_timings()
    footer_message()


if __name__ == "__main__":
    main()
