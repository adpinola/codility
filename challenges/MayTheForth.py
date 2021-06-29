# You are given N disks and two rods, each with one initial disk.

# On the left rod, disks can be placed in decreasing order of size (smaller disks on top of bigger ones). On the right rod, disks can be placed in increasing order of size (bigger disks on top of smaller ones). Note that it is not permissible to place two disks of equal size on top of each other. The initial disks cannot be moved.

# Write a function:

# def solution(A, L, R)

# that, given an array A of integers representing the sizes of the N disks and two integers L and R representing the size of the initial disks on the left and right rods respectively, returns the maximum number of disks from A that can be placed on the rods while satisfying the rules presented above.

# Examples:

# 1. Given A = [2, 3, 3, 4], L = 3 and R = 1, your function should return 3, since only three disks can be placed on the rods. Note that the disk of size 2 can be placed on either the left rod or the right rod.

# 2. Given A = [1, 4, 5, 5], L = 6 and R = 4, your function should return 4.

# 3. Given A = [5, 2, 5, 2], L = 8 and R = 1, your function should return 4.

# 4. Given A = [1, 5, 5], L = 2 and R = 4, your function should return 2.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# L and R are integers within the range [1..1,000,000,000].

def solution(A, L, R):
    N = len(A)
    A.sort()
    result = 0
    for i in range(N):
        if A[i] > 0:
            if A[i] > R: # the disk I have is bigger than the one in RIGHT rod
                result += 1
                R = A[i] # now this is the disk at the top
                A[i] = 0 # mark this disk as used
        if A[N - 1 - i] > 0:
            if A[N - 1 - i] < L: # the disk I have is smaller than the one in LEFT rod    
                result += 1
                L = A[N - 1 - i]
                A[N - 1 - i] = 0
    return result