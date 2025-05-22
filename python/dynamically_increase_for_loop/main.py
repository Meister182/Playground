#!/usr/bin/env python3


L = list(range(10))
for index, i in enumerate(L):
    print(index, "-> ", i)
    if i == 4:
        L[index + 1:index + 1] = [10, 20, 30]
