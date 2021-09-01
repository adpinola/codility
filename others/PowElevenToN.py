# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # The main idea is that 11^N can be calulated by adding digits
    # example: 11^2 = 121
    # so --> 11^0 =           0   1
    #                         |_+_|
    #                         |   |
    #    --> 11^1 =       0   1   1
    #                     |_+_|_+_|
    #                     |   |   |  
    #    --> 11^2 =   0   1   2   1 
    #                 |_+_|_+_|_+_|
    #                 |   |   |  
    #    --> 11^3 =   1   3   3   1 
    stringNumber = '1'
    ones = 1 # this belongs to 11^0
    for i in range(1,N + 1):
        resultLen = len(stringNumber)
        newCalculatedNumber = '1'
        ones = 1 
        carry = 0
        for c in range(resultLen):
            # Here I'm iterating over the last calculated number
            currentDigit = int(stringNumber[resultLen - 1 - c])
            prevDigit = 0 if resultLen - 2 - c < 0 else int(stringNumber[resultLen - 2 - c])
            newDigit = currentDigit + prevDigit + carry
            carry = 0
            if newDigit >= 10:
                carry = 1 # this carry affects the new adding operation (check 11^4 --> 11^5)
            newCalculatedNumber = str(newDigit % 10) + newCalculatedNumber
            if newDigit % 10 == 1: 
                # this is because when adding the result may be 11
                # so that is why I'm not only checking for newDigit == 1
                # in line 32, I need to print newDigit % 10 (so that's the same logic!!)
                ones += 1
        stringNumber = newCalculatedNumber
    return ones