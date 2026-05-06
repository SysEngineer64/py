'''
Even Positioned Characters
Difficulty: BasicAccuracy: 76.72%Submissions: 64K+Points: 1Average Time: 10m
You are given a String S, you need to print its characters at even indices(index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices (0, 2 & 4) characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.


'''


def utility(s):
    #code here
    for i in range(0, len(s)):
        if(i%2==0):
            print(s[i], end="")