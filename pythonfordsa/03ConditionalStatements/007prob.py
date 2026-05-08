'''
Closest Number
Difficulty: BasicAccuracy: 15.77%Submissions: 146K+Points: 1
Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

Examples :

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.
Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15 and divisible by 6, but -18 has the maximum absolute value. So, output is -18.
Constraints:
-105 ≤ n, m ≤ 105


'''


def closestNumber(n, m):
    # # code here
    # output = int(n / m) 
    # finalOutput = output * m 
    
    # if (finalOutput == n):
    #     return finalOutput

    # else:
    #     smalloutput = abs(n - finalOutput)
    #     output += 1
    #     longoutput = m * output 
    #     fnllongoutput = abs(longoutput - n)


    #     if (n < 0 and smalloutput < fnllongoutput):
    #         return longoutput
    #     else:
    #         return finalOutput
    #         # print(finalOutput)
    #         # print(fnllongoutput)

        m = abs(m)

        output = int(n / m)
        finalOutput = output * m

        if finalOutput == n:
            return finalOutput

        else:
            smalloutput = abs(n - finalOutput)

            if n > 0:
                output += 1
            else:
                output -= 1

            longoutput = m * output
            fnllongoutput = abs(longoutput - n)

            if smalloutput < fnllongoutput:
                return finalOutput
            else:
                return longoutput

print(closestNumber(-6, 39))