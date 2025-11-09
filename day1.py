import sys

def solve1(names, moves):
    pos = 0
    for move in moves:
        pos = min(max(pos + move[0] * move[1], 0), len(names)-1)
    print(names[pos])

def solve2(names, moves):
    pos = 0
    for move in moves:
        pos = (pos + move[0] * move[1]) % len(names)
    print(names[pos])

def solve3(names, moves):
    for move in moves:
        pos = (move[0] * move[1]) % len(names)
        names[0], names[pos] = names[pos], names[0]
    print(names[0])

def parse(it):
    names = it.readline().strip().split(',')
    _ = it.readline()
    moves = list(map(lambda m: (-1 if m[0] == 'L' else +1, int(m[1:])), it.readline().split(',')))
    return names, moves

names, moves = parse(sys.stdin)
solve1(names, moves)
solve2(names, moves)
solve3(names, moves)
