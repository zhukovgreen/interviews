"""
# Array products
#
# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the elements of nums except nums[i].

def array_products(a):
  # please add your implementation here

  return [24, 12, 8, 6]

print('Array products')
print('Should be')
print('[24, 12, 8, 6]')
print(array_products([1, 2, 3, 4]))
"""
from functools import reduce
from operator import mul
from typing import List


def solution(s: List[int]) -> List[int]:
    output = []
    for idx in range(len(s)):
        sub_list = s[:idx] + s[idx + 1 :]
        res = 1
        for item in sub_list:
            res *= item
        output.append(res)

    return output


def solution_alt(s: List[int]) -> List[int]:
    total = reduce(mul, s, 1)
    return [int(total / i) for i in s]


def test_solution():
    assert solution([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_alt([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_alt([0, 2, 3, 4]) == [24, 0, 0, 0]
    assert solution_alt([0, 0, 3, 4]) == [0, 0, 0, 0]
