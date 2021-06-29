# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

  # A[0] = 3
  # A[1] = 1
  # A[2] = 2
  # A[3] = 4
  # A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

  # A[0] = 3
  # A[1] = 1
  # A[2] = 2
  # A[3] = 4
  # A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(A):
    n = len(A)
    p = n // 2
    leftSum = 0
    rightSum = 0
    for i in range(p):
        # Calculate the Sum of evry half of the array
        leftSum += A[i]
        rightSum += A[i + p]
    if n % 2 > 0:
        rightSum+= A[ n - 1]
    diff = abs(leftSum - rightSum) # get the initial differente
    forwardLeftSum = leftSum
    forwardRightSum = rightSum
    reverseLeftSum = leftSum
    reverseRightSum = rightSum    
    # Now I will move through the array forward and reverse
    # to and calculate the new distance on every step
    # and update the diff if the calculated value is lower than
    #in the previous step
    for i in range(p):
        if p + i  < n - 1: # take care of keeping the right side with at least one element
            # Move Right, add a value to left part, remove a value from
            # right part
            forwardLeftSum += A[p + i]
            forwardRightSum -= A[p + i]
            # calculate new diff
            fDiff = abs(forwardLeftSum - forwardRightSum)
            if fDiff < diff:
                diff = fDiff # update diff value if it is lower
        if p - i > 1: # take care of keeping the left side with at least one element       
            # Move Left, remove a value from left part, add it to right part
            reverseLeftSum -= A[p - 1 - i]
            reverseRightSum += A[p - 1 - i]
            # calculate new diff
            rDiff = abs(reverseLeftSum - reverseRightSum)
            if rDiff < diff:
                diff = rDiff
    return diff