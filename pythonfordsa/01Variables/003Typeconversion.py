'''
TypeCast And Double It
Difficulty: BasicAccuracy: 62.79%Submissions: 85K+Points: 1
Given an input num as a string. You need to typecast into an integer and double it. 

Examples:

Input: num = "5"
Output: 10
Explanation: Typecast "5" to int and then double it 5 * 2 = 10
Input: num = "12"
Output: 24
Explanation: Typecast "12" to int and then double it 12 * 2 = 24
Constraints:
0 <= num <= 105


'''

num = input()
#code here

doubleNum = int(num) * 2
print(doubleNum)