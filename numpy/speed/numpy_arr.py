import numpy as np
N = 1000000


a = np.arange(N)
b = np.arange(N)

## a * b (means that res[i] = a[i] * b[i])
res = a * b
print(res[:10])