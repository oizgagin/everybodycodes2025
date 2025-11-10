from math import floor, ceil
import fractions
import sys

def solve1(l):
    U = {'A': 0, 'B': 0, 'C': 0}

    res = 0
    for ch in l:
        if ch == 'A':
            U[ch] += 1
        else:
            res += U[ch.upper()]
    print(res)

def solve2(l):
    U = {'A': 0, 'B': 0, 'C': 0}

    res = 0
    for ch in l:
        if ch in 'ABC':
            U[ch] += 1
        else:
            res += U[ch.upper()]
    print(res)

def solve3(l):
    D, N = 1000, 1000
    # i: max(i-D, 0) ; min(N, i+D)
    l = l * N

    U = {'A': 0, 'B': 0, 'C': 0}
    for i in range(0, D):
        if l[i] in 'ABC':
            U[l[i]] += 1

    res = 0
    for i in range(len(l)):
        if i + D < len(l) and l[i+D] in 'ABC':
            U[l[i+D]] += 1

        if l[i] in 'abc':
            res += U[l[i].upper()]

        if i - D >= 0 and l[i-D] in 'ABC':
            U[l[i-D]] -= 1

    print(res)

def parse(it):
    return it.readline().strip()

l = parse(sys.stdin)
solve1(l)
solve2(l)
solve3(l)
