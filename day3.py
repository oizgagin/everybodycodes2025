import collections
import sys

def solve1(nums):
    print(sum(set(nums)))

def solve2(nums):
    s = list(set(nums))
    s.sort()
    print(sum(s[:20]))

def solve3(nums):
    c = collections.Counter(nums)
    print(max(c.values()))

def parse(it):
    return list(map(int, it.readline().split(',')))

nums = parse(sys.stdin)
solve1(nums)
solve2(nums)
solve3(nums)
