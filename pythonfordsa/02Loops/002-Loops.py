from __future__ import print_function

n = 4
for i in range(0, n):
    print(i)


print("-----------")
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

print("-----------")

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

print("-----------")

s = "abc"
for x in s:
    print(x)

print("-----------")

d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))

print("-----------")

set1 = {10, 30, 20}
for x in set1:
    print(x)

print("-----------")

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])


'''
While Loop
'''


print("-----------")

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

print("-----------")

while (True):
    print("Hello Geek")
    break

print("-----------")


for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()

print("-----------")

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

print("-----------")

for letter in 'geeksforgeeks':
    if letter == 'k' or letter == 's':
        break

print('Current Letter :', letter)
print("-----------")

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

print("-----------")












