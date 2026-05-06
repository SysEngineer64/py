'''
Mark Even and Odd - Python
Difficulty: EasyAccuracy: 59.05%Submissions: 210K+Points: 2Average Time: 5m
Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number).
Note: Return "Even" if the number is even; otherwise, return "Odd".

Examples

Input: x = 4
Output: Even
Input: x = 5
Output: Odd
Constraints:
1 ≤ x ≤ 106


'''


# @param x: int
# @return: string

def checkOddEven(x):
    # code here
    
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"