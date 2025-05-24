import itertools
from typing import List, Tuple, Iterable
from collections import defaultdict

from .orbit import *


class Basis:
    def __init__(self, p_max: int, delta: float = 1):
        self.p_max = p_max
        self.delta = delta
        # build one-body basis
        self.one_body_basis = build_one_body_basis(p_max, delta)
        self.one_body_basis_map = self.build_one_body_basis_sorted()
        self.one_body_basis_number = len(self.one_body_basis)
        self.one_body_channel_number = len(self.one_body_basis_map)
        # build two-body basis
        self.two_body_basis = self.build_two_body_basis()
        self.two_body_basis_map = self.build_two_body_basis_sorted()
        self.two_body_basis_number = len(self.two_body_basis)
        self.two_body_channel_number = len(self.two_body_basis_map)

    # get index-th one-body state |index>
    def get_one_body_state(self, index: int) -> Orbital:
        return self.one_body_basis[index]

    # sort one-body states into map
    def build_one_body_basis_sorted(self) -> defaultdict[int, List[Orbital]]:
        one_body_basis_map = defaultdict(list)
        for orb in self.one_body_basis:
            key = one_body_symmetry_key(orb)
            value = orb
            one_body_basis_map[key].append(value)
        return one_body_basis_map

    # get one-body states in the same channel of |index>
    def get_one_body_channel(self, index: int) -> List[Orbital]:
        orb = self.get_one_body_state(index)
        key = one_body_symmetry_key(orb)
        return self.one_body_basis_map[key]

    # build two-body basis
    def build_two_body_basis(self) -> List[Tuple[Orbital, Orbital]]:
        return list(itertools.combinations(self.one_body_basis, 2))

    # sort two-body states into map
    def build_two_body_basis_sorted(self) -> defaultdict[int, List[Tuple[Orbital, Orbital]]]:
        two_body_basis_map = defaultdict(list)
        for orb_a, orb_b in self.two_body_basis:
            key = two_body_symmetry_key(orb_a, orb_b)
            value = (orb_a, orb_b)
            two_body_basis_map[key].append(value)
        return two_body_basis_map

    # get two-body states in the same channel of |index_a, index_b>
    def get_two_body_channel(self, index_a: int, index_b: int) -> List[Tuple[Orbital, Orbital]]:
        orb_a = self.get_one_body_state(index_a)
        orb_b = self.get_one_body_state(index_b)
        key = two_body_symmetry_key(orb_a, orb_b)
        return self.two_body_basis_map[key]


class Det:
    def __init__(self, occupied_indices: Iterable[int], nmo: int):
        # occupied_indices: [0, 1, 5] for example
        # nmo: total length of Det
        self.nmo: int = nmo
        self.bits: int = 0
        occupation_number = 0
        for index in occupied_indices:
            if not (0 <= index < nmo):
                raise ValueError(f"index: {index} out of range: [0, {nmo-1}]!")
            self.bits |= 1 << index
            occupation_number += 1
        self.occupation_number = occupation_number

    @classmethod
    def from_int(cls, bits: int, nmo: int) -> "Det":
        instance = cls([], nmo)
        instance.bits = bits
        instance.occupation_number = bits.bit_count()  # need Python 3.10+
        return instance

    def is_occupied(self, index: int) -> bool:
        if not (0 <= index < self.nmo):
            raise IndexError(f"index: {index} out of range: [0, {self.nmo-1}]。")
        return bool((self.bits >> index) & 1)

    def get_occupied_indices(self) -> Tuple[int, ...]:
        indices = []
        bits = self.bits
        index = 0
        while bits > 0:
            if bits & 1:
                indices.append(index)
            bits >>= 1
            index += 1
        return tuple(indices)

    def count_occupation(self) -> int:
        return self.bits.bit_count()

    def __and__(self, other: "Det") -> int:
        return self.bits & other.bits

    def __or__(self, other: "Det") -> int:
        return self.bits | other.bits

    def __xor__(self, other: "Det") -> int:
        return self.bits ^ other.bits

    def __hash__(self) -> int:
        return hash((self.bits, self.nmo))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Det):
            return NotImplemented
        return self.bits == other.bits and self.nmo == other.nmo

    def __repr__(self) -> str:
        standard_bin = bin(self.bits)[2:]
        padded_bin = standard_bin.zfill(self.nmo)
        left_to_right_bin = padded_bin[::-1]
        return f"Det({left_to_right_bin})"

    def __str__(self) -> str:
        return f"Det(NMO={self.nmo}, occupation number={self.count_occupation()}, Indices={self.get_occupied_indices()})"


# usage: python -m lib.basis
if __name__ == "__main__":
    # tesing basis...
    p_max, delta = 4, 1
    test_basis = Basis(p_max, delta)
    print(f"number of one-body channels: {test_basis.one_body_channel_number}")
    for one_body_channel_key in test_basis.one_body_basis_map:
        print(f"one-body channel key: {one_body_channel_key}")
        states_this_channel = test_basis.one_body_basis_map[one_body_channel_key]
        for state in states_this_channel:
            print(state.info())
    print(f"number of two-body basis: {test_basis.two_body_basis_number}")
    for two_body_channel_key in test_basis.two_body_basis_map:
        print(f"two-body channel key: {two_body_channel_key}")
        states_this_channel = test_basis.two_body_basis_map[two_body_channel_key]
        for state_a, state_b in states_this_channel:
            print(state_a.info(), state_b.info())

    # testing Det...
    NMO = 8

    det1 = Det([0, 2, 5], NMO)
    print(det1)
    print(repr(det1))
    print(f"  轨道 2 是否占据? {det1.is_occupied(2)}")
    print(f"  轨道 3 是否占据? {det1.is_occupied(3)}")
    print(f"  总粒子数: {det1.count_occupation()}")

    det2 = Det([1, 2, 6], NMO)
    print(f"\ndet2: {det2}")

    # 计算激发 (通过 XOR)
    excitation_mask = det1 ^ det2
    excitation_det = Det.from_int(excitation_mask, NMO)
    print(f"\n激发 (XOR): {excitation_det}")
    print(f"  激发的轨道: {excitation_det.get_occupied_indices()}")

    # 用作字典键
    my_map = {det1: 10.5, det2: -3.2}
    print(f"\n字典: {my_map}")
    print(f"  det1 的值: {my_map.get(det1)}")
