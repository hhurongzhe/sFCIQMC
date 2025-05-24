# -*- coding: utf-8 -*-
"""
constants.py: 定义通用数学和物理常数。
"""

import math

# --- 数学常数 ---
PI = math.pi
TWO_PI = 2.0 * PI

# --- 物理常数 (以原子单位制 a.u. 为例) ---
HBAR = 1.0  # 约化普朗克常数 (a.u.)
ELECTRON_MASS = 1.0  # 电子质量 (a.u.)
ELEMENTARY_CHARGE = 1.0  # 基本电荷 (a.u.)
BOHR_RADIUS = 1.0  # 玻尔半径 (a.u.)
HARTREE_ENERGY = 1.0  # 哈特里能量 (a.u.)

# --- 其他可能需要的常数 ---
# ...

if __name__ == "__main__":
    print("通用常数模块:")
    print(f"  π = {PI}")
    print(f"  ħ = {HBAR} a.u.")
