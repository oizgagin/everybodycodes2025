import sys

add = lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1])
mul = lambda t1, t2: (t1[0] * t2[0] - t1[1] * t2[1], t1[0] * t2[1] + t1[1] * t2[0])
div = lambda t1, t2: (int(t1[0] / t2[0]), int(t1[1] / t2[1]))

def solve1(A):
    R = (0, 0)
    for _ in range(3):
        R = mul(R, R)
        R = div(R, (10, 10))
        R = add(R, A)
    print(R)


def solve2(A):
    def cycle(p):
        r = (0, 0)
        for _ in range(100):
            r = mul(r, r)
            r = div(r, (100000, 100000))
            r = add(r, p)
            if not (-1000000 <= r[0] <= 1000000 and -1000000 <= r[1] <= 1000000):
                return False
        return True

    c = 0
    for dx in range(0, 1001):
        for dy in range(0, 1001):
            if cycle(add(A, (dx, dy))): c += 1
    print(c)


def solve3(a):
    print(a)


def parse(it):
    return tuple(map(int, it.readline().strip()[3:-1].split(',')))


A = parse(sys.stdin)
solve1(A)
solve2(A)
solve3(A)
