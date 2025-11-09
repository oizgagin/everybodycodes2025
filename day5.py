from math import floor, ceil
import fractions
import sys

def get_spine(nums):
    spine = [ [None, nums[0], None] ]
    for i in range(1, len(nums)):
        num = nums[i]
        for seg in spine:
            if num < seg[1] and seg[0] is None:
                seg[0] = num
                break
            elif num > seg[1] and seg[2] is None:
                seg[2] = num
                break
        else:
            spine.append([None, num, None])
    return spine

def get_quality(spine):
    return int(''.join(map(lambda seg: str(seg[1]), spine)))

def solve1(id_, nums):
    print(get_quality(get_spine(nums)))

def solve2(it):
    max_, min_ = float('-inf'), float('inf')
    for _, nums in it:
        max_ = max(max_, get_quality(get_spine(nums)))
        min_ = min(min_, get_quality(get_spine(nums)))
    print(max_ - min_)

def solve3(it):

    def key(id_, sword):
        spine = get_spine(sword)

        nums = tuple(map(lambda seg: int(''.join(map(str, filter(None, seg)))), spine))
        return (
            get_quality(spine),
            nums,
            id_,
        )

    v = list(sorted(it, key=lambda t: key(t[0], t[1]), reverse=True))

    res = 0
    for i, (id_, _) in enumerate(v, 1):
        res += id_ * i
    print(res)

def parse(it):
    for line in it.readlines():
        id_, nums = line.strip().split(':')
        yield int(id_), list(map(int, nums.split(',')))

swords = list(parse(sys.stdin))
#solve1(id_, nums)
#solve2(it)
solve3(swords)
