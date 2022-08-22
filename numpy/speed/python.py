"""
Python operation on array.
"""
N = 1000000
a = list(range(N))
b = list(range(N))

res = []
for i in range(N):
    res.append(a[i] * b[i])

for i in range(10):
    print(res[i])
