from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    sums = 0
    for i in triplet:
        sums += i
    return sums


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    volume = 1
    for j in box_dimensions:
        volume *= j
    return volume

  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
