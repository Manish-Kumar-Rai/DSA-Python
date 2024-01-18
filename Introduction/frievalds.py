# --------------- frivalds algorithm-----------------------------

"""
Frivold's algorithm is a probabilistic method for verifying matrix multiplication. Given matrices A, B, and C, the algorithm uses a random vector to check if AB = C with high probability. It is particularly useful in situations where a fast, probabilistic check for correctness is acceptable, even though there is a small chance of error.
"""

from sys import stdin
from random import randint

def readint():
    return int(stdin.readline())

def readarray(typ):
    return list(map(typ,stdin.readline().split()))

def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M

def mult(M,v):
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]

def frivalds(A,B,C):
    n = len(A)
    x = [randint(0,1000000) for _ in range(n)]
    return mult(A,mult(B,x)) == mult(C,x)

if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(frivalds(A,B,C))
