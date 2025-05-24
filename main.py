# -*- coding: utf-8 -*-
"""
main.py: 主程序入口，设置参数，运行计算，处理结果。
"""

import numpy as np
import matplotlib.pyplot as plt

# 导入依赖模块 (修改为从 lib 包导入)
from lib import constants
from lib.util import timing_decorator
from lib.orbit import build_orbit_basis, Orbital
from lib.basis import build_fci_basis, SlaterDeterminant
from lib.hamiltonian import build_hamiltonian_from_file, Hamiltonian
from lib.fciqmc import FCIQMC_Runner

# ... (程序的其余部分保持不变) ...


@timing_decorator
def run_calculation():
    """
    设置并运行完整的计算流程。
    """
    print("=" * 40)
    print("   开始 Ab Initio 计算 (FCIQMC)   ")
    print("=" * 40)

    # --- 1. 设置参数 ---
    print("\n[1. 设置参数]")
    num_orbitals = 4
    num_electrons = 2
    initial_walkers = 10
    target_walkers = 1000
    time_step = 0.001
    simulation_steps = 1000
    hamiltonian_file = "integrals.dat"
    orbital_energies = [0.0, 0.2, 0.8, 1.0]

    print(f"  轨道数: {num_orbitals}, 电子数: {num_electrons}")
    print(f"  初始 Walker 数: {initial_walkers}, 目标 Walker 数: {target_walkers}")
    print(f"  时间步长: {time_step}, 模拟步数: {simulation_steps}")
    print(f"  Pi = {constants.PI}")  # 使用 constants

    # --- 2. 构建基组 ---
    print("\n[2. 构建基组]")
    single_particle_basis = build_orbit_basis(num_orbitals, orbital_energies)
    many_body_basis = build_fci_basis(single_particle_basis, num_electrons)

    # --- 3. 构建哈密顿量 ---
    print("\n[3. 构建哈密顿量]")
    print("  警告: 使用 Mock Hamiltonian 进行演示！")
    M = num_orbitals
    h1 = np.diag(orbital_energies)
    h2 = np.zeros((M, M, M, M))
    H = Hamiltonian(h1, h2)

    def mock_get_matrix_element(det_bra, det_ket):
        holes, particles = det_bra.find_excitations(det_ket)
        if not holes and not particles:
            return sum(orb.energy for orb in det_bra.orbitals)
        else:
            return 0.0

    H.get_matrix_element = mock_get_matrix_element

    # --- 4. 运行 FCIQMC ---
    print("\n[4. 运行 FCIQMC]")
    fciqmc_calc = FCIQMC_Runner(H, many_body_basis, initial_walkers, time_step, target_walkers)
    print("  警告: 使用 Mock Spawning 进行演示！")

    def mock_spawn(det_i, N_i):
        pass

    fciqmc_calc._spawn = mock_spawn
    energies, walker_counts = fciqmc_calc.simulate(simulation_steps)

    # --- 5. 处理并展示结果 ---
    print("\n[5. 展示结果]")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ax1.plot(range(simulation_steps), energies)
    ax1.set_ylabel("Shift (Energy Estimate / a.u.)")
    ax1.set_title("FCIQMC Simulation Results (Mock)")
    ax1.grid(True)
    ax2.plot(range(simulation_steps), walker_counts)
    ax2.axhline(target_walkers, color="r", linestyle="--", label=f"Target ({target_walkers})")
    ax2.set_xlabel("Time Step")
    ax2.set_ylabel("Total Walkers")
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.savefig("fciqmc_results.png")
    print("  结果已保存到 fciqmc_results.png")
    plt.show()

    print("\n计算完成。")


if __name__ == "__main__":
    run_calculation()
