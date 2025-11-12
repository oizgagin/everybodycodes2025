from math import floor, ceil
import fractions
import sys

def is_valid(name, rules):
    for i in range(1, len(name)):
        if (name[i-1], name[i]) not in rules:
            return False
    return True

def solve1(names, rules):
    for name in names:
        for i in range(1, len(name)):
            if (name[i-1], name[i]) not in rules:
                break
        else:
            print(name)
            return

def solve2(names, rules):
    res = 0
    for j, name in enumerate(names, 1):
        for i in range(1, len(name)):
            if (name[i-1], name[i]) not in rules:
                break
        else:
            res += j
    print(res)

def solve3(names, rules):
    prefixes = list(filter(lambda name: is_valid(name, rules), names))

    uniqs = set()

    def recurse(prefix):
        if len(prefix) == 12:
            return

        if 7 <= len(prefix) <= 11:
            uniqs.add(prefix)

        for rule in rules:
            if rule[0] == prefix[-1]:
                recurse(prefix + rule[1])

    for prefix in prefixes: recurse(prefix)
    print(len(uniqs))

def parse(it):
    names = list(it.readline().strip().split(','))
    _ = it.readline()

    rules = set()
    for line in it.readlines():
        from_, _, to = tuple(line.strip().split(' '))

        for ch in to.split(','):
            rules.add((from_, ch))

    return names, rules

names, rules = parse(sys.stdin)
solve1(names, rules)
solve2(names, rules)
solve3(names, rules)
