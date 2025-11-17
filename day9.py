from collections import defaultdict
from math import floor, ceil
import fractions
import sys

def is_child(p1, p2, c):
    for i, ch in enumerate(c):
        if ch != p1[i] and ch != p2[i]:
            return False
    return True

def degree(p, c):
    res = 0
    for ch1, ch2 in zip(p, c):
        if ch1 == ch2: res += 1
    return res

def solve1(notes):
    for i in range(len(notes)):
        for j in range(i+1, len(notes)):
            for k in range(j+1, len(notes)):
                if is_child(notes[i][1], notes[j][1], notes[k][1]):
                    print(degree(notes[i][1], notes[k][1]) * degree(notes[j][1], notes[k][1]))

def solve2(notes):
    res = 0

    seen = set()

    for i in range(len(notes)):
        for j in range(i+1, len(notes)):
            if i == j: continue
            for k in range(len(notes)):
                if j == k or i == k: continue
                if (i, j, k) not in seen and is_child(notes[i][1], notes[j][1], notes[k][1]):
                    res += degree(notes[i][1], notes[k][1]) * degree(notes[j][1], notes[k][1])
                    seen.add((i, j, k))
    print(res)

def solve3(notes):

    uf = list(range(0, len(notes)+1))
    sz = [1] * (len(notes)+1)

    def union(p1, p2):
        if find(p1) != find(p2):
            sz[find(p2)] += sz[find(p1)]
            uf[find(p1)] = find(p2)

    def find(p):
        if uf[p] != p:
            uf[p] = find(uf[p])
        return uf[p]

    res = 0

    for i in range(len(notes)):
        for j in range(i+1, len(notes)):
            if i == j: continue
            for k in range(len(notes)):
                if j == k or i == k: continue
                if is_child(notes[i][1], notes[j][1], notes[k][1]):
                    union(notes[i][0], notes[j][0])
                    union(notes[j][0], notes[k][0])

    c = defaultdict(int)
    for i in range(1, len(notes)+1):
        c[find(i)] += i

    m = max(sz)
    for i in range(1, len(notes)+1):
        if sz[find(i)] == m:
            print(c[find(i)])
            break

def parse(it):
    notes = []
    for line in it.readlines():
        scale, dna = line.strip().split(':')
        notes.append((int(scale), dna))
    return notes

notes = parse(sys.stdin)
solve1(notes)
solve2(notes)
solve3(notes)
