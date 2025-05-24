from typing import List


class Orbital:
    def __init__(self, i: int, p: int, s: int, delta: float = 1):
        # i: index (0, 1, 2, ...)
        # p: principle quantum number (1, 2, 3, 4, ...)
        # s: spin projection (1, -1)
        # delta: spacing of single-particle levels
        # e: energy
        self.i = i
        self.p = p
        self.s = s
        self.e = delta * (p - 1)

    def info(self) -> str:
        return f"Orb (index={self.i}, p={self.p}, spin={self.s}, energy={self.e:.2f})"


# build one-body basis
def build_one_body_basis(p_max: int, delta: float = 1) -> List[Orbital]:
    # p_max: maximum principle quantum number
    sp_basis_list = []
    index = 0
    # p: [1, 2, 3, ..., p_max]
    for p in range(1, p_max + 1):
        # s: [1, -1]
        for s in [1, -1]:
            orb = Orbital(index, p, s, delta)
            sp_basis_list.append(orb)
            index += 1
    return sp_basis_list


# check one-body symmetry
def check_one_body_symmetry(orb_a: Orbital, orb_b: Orbital) -> bool:
    symmetry_condition = True
    if orb_a.s != orb_b.s:
        symmetry_condition = False
    return symmetry_condition


# check two-body symmetry
def check_two_body_symmetry(orb_a: Orbital, orb_b: Orbital, orb_c: Orbital, orb_d: Orbital) -> bool:
    symmetry_condition = True
    if (orb_a.s + orb_b.s) != (orb_c.s + orb_d.s):
        symmetry_condition = False
    return symmetry_condition


def one_body_symmetry_key(orb_a: Orbital) -> int:
    key = orb_a.s
    return key


def two_body_symmetry_key(orb_a: Orbital, orb_b: Orbital) -> int:
    key = orb_a.s + orb_b.s
    return key


# usage: python -m lib.orbit
if __name__ == "__main__":
    p_max, delta = 4, 1
    sp_basis = build_one_body_basis(p_max, delta)
    for orb in sp_basis:
        print(orb.info())
