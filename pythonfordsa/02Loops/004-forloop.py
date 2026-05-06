def getTable(n):
        # code here
        # return [n * i for i in range(1, 11)]
        result = []

        for i in range(1, 11):
            result.append(n * i)

        return result

print(getTable(9))
