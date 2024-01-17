from sys import stdin
from random import randint

def readint():
    return int(stdin.readline())

def readarray(typ):
    return list(map(int,stdin.readline().split()))

def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M

def mult(M,v):
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]

def frievalds(A,B,C):
    n = len(A)
    x = [randint(0,1000000) for _ in range(n)]
    return mult(A,mult(B,x)) == mult(C,x)

if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(frievalds(A,B,C))