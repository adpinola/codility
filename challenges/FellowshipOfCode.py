# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

def solution(S, K):
    SL = list(S)
    remainingIterations = K
    base = 0
    while remainingIterations:
        auxList = SL[base:base+remainingIterations + 1]
        if len(auxList) == 0:
            break
        minValue = min(auxList)
        index = auxList.index(minValue)
        remainingIterations -= index
        SL.pop(index+base)
        SL.insert(base, minValue)
        base += 1
    print(''.join(SL))
    return ''.join(SL)

if __name__ == "__main__":
    a = sys.argv[1]
    b = int(sys.argv[2])
    solution(a, b)


# D E C A D E A S A C

# 0 1 2 3 4 5 6 7 8 9

# D E C A D
