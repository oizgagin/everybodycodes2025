from collections import defaultdict
from math import floor, ceil
import fractions
import sys

def solve1(nums):
    res = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i-1]) == 16:
            res += 1
    print(res)

def solve2(nums):
    res = 0
    seen = set()

    ok = lambda p1, p2, pp1, pp2: pp1 < p1 < pp2 and p2 != pp1 and p2 != pp2 and not pp1 < p2 < pp2

    for i in range(1, len(nums)):
        p1, p2 = nums[i-1], nums[i]

        if p1 > p2:
            p1, p2 = p2, p1

        for pp1, pp2 in seen:
            if ok(p1, p2, pp1, pp2) or ok(p2, p1, pp1, pp2): res += 1
        seen.add((p1, p2))
    print(res)

def solve3(nums):
    res = 0
    seen = defaultdict(int)

    def ok(p1, p2, pp1, pp2):
        assert pp1 < pp2
        return pp1 < p1 < pp2 and (p2 > pp2 or p2 < pp1)

    for i in range(1, len(nums)):
        p1, p2 = nums[i-1], nums[i]

        if p1 > p2:
            p1, p2 = p2, p1

        seen[(p1, p2)] += 1

    N = 256

    max_ = float('-inf')
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            res = 0

            for pp1, pp2 in seen:
                if ok(i, j, pp1, pp2) or ok(j, i, pp1, pp2): res += seen[(pp1, pp2)]

            if (i, j) in seen: res += seen[(i, j)]

            max_ = max(res, max_)

    print(max_)

def parse(it):
    return list(map(int, it.readline().split(',')))

nums = parse(sys.stdin)
solve1(nums)
solve2(nums)
solve3(nums)
