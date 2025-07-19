def josephusPosition(n, k):
    if n == 1: return 0
    return (josephusPosition(n - 1, k) + k) % n

print(josephusPosition(5, 2))
print(josephusPosition(6, 1))
print(josephusPosition(10, 2))
print(josephusPosition(1, 1))