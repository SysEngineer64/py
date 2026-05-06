marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")


age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")



age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")



### Ternary Conditional Statement


# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


### Match-Case Statement
'''
match-case statement is Python's version of a switch-case found in other languages. 
It allows us to match a variable's value against a set of patterns.
'''

number = 3

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
