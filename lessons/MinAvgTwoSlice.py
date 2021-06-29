# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

    # A[0] = 4
    # A[1] = 2
    # A[2] = 2
    # A[3] = 5
    # A[4] = 1
    # A[5] = 5
    # A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

    # A[0] = 4
    # A[1] = 2
    # A[2] = 2
    # A[3] = 5
    # A[4] = 1
    # A[5] = 5
    # A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    minAvg = 10001 # be sure to be always lower than this value
    avgTwoElements = minAvg
    avgThreeElements = minAvg
    prefixSum = [0] * (N + 1)
    P = N + 1
    for i in range(1, N + 1):
        prefixSum[i] = prefixSum[i - 1] + A[i - 1]
        if i > 1:
            # start calulating here
            avgTwoElements = (prefixSum[i] - prefixSum[i - 2]) / 2
            if avgTwoElements < minAvg:
                minAvg = avgTwoElements
                P = i - 2
            if i > 2:
                # start calculating size 3 slices
                avgThreeElements = (prefixSum[i] - prefixSum[i - 3]) / 3
                if avgThreeElements < minAvg:
                    minAvg = avgThreeElements
                    P = i - 3
    return P