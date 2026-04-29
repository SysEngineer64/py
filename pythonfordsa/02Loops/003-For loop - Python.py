# n = int(input())

def multiplicationTable(n):
        # code here
        for i in range(1, 11):
            if i < 10:
                print(n*i, end=',')
            else:
                print(n*i)
            
multiplicationTable(5)