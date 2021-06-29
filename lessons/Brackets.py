# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

bracketMap = {
    '{': '}',
    '[': "]",
    '(': ")"
}

size = 0
def solution(S):
    N = len(S)
    stack = [0] * N
    def push(x):
        global size
        stack[size] = x
        size += 1
    def pop():
        global size
        if size == 0:
            return -1
        size -= 1
        return stack[size]
    if N % 2 != 0:
        return 0 # I have odd number of elements no way it is correct
    for i in range(N):
        if S[i] == '{' or S[i] == '[' or S[i] == '(':
            push(S[i])
        else:
            lastBracket = pop()
            if S[i] != bracketMap[lastBracket]:
                return 0
    return 1 if size == 0 else 0
