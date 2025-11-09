from math import floor, ceil
import fractions
import sys

def solve1(nums):
    r = fractions.Fraction(1)
    for i in range(1, len(nums)):
        r *= fractions.Fraction(nums[i], nums[i-1])
    print(floor(2025 / r))

def solve2(nums):
    """
    x / r >= 10000000000000
    x >= 10000000000000 * r
    x = ceil
    """
    r = fractions.Fraction(1)
    for i in range(1, len(nums)):
        r *= fractions.Fraction(nums[i], nums[i-1])
    print(ceil(10000000000000 * r))

def solve3(nums):
    rs = []
    for arr in nums:
        r = fractions.Fraction(1)
        for i in range(1, len(arr)):
            r *= fractions.Fraction(arr[i], arr[i-1])
        rs.append(r)

    r = rs[0]
    for i in range(1, len(rs)):
        r *= rs[i]
    print(floor(100 / r))

def parse(it):
    res = [[]]

    for l in it.readlines():
        if '|' not in l:
            res[-1].append(int(l))
        else:
            a, b = tuple(map(int, l.split('|')))
            res[-1].append(a)
            res.append([b])
    return res

nums = parse(sys.stdin)
#solve1(nums)
#solve2(nums)
solve3(nums)
