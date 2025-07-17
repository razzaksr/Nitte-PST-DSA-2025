def staircase(case):
    if case < 1: return 0
    elif case == 1: return 1
    elif case == 2: return 2
    else: return (staircase(case-1)+staircase(case-2))

print(staircase(2))
print(staircase(1))
print(staircase(-2))
print(staircase(5))
print(staircase(8))