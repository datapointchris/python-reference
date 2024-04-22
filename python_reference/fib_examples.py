import time
from functools import reduce

import pandas as pd


def fib_1(n):
    fibs = []
    i = 1
    a = 0
    b = 1
    if n == 0:
        fibs.append(a)
    else:
        fibs.append(a)
        fibs.append(b)
    while i < n:
        a, b = b, a + b
        fibs.append(b)
        i += 1
    return fibs


for i in range(21):
    print(fib_1(i))


def fib_2(n):
    def fib_recur(n):
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        return fib_recur(n - 1) + fib_recur(n - 2)

    return [fib_recur(n) for n in range(0, n + 1)]


for i in range(21):
    print(fib_2(i))


def fib_3(n):
    stored = {0: 0, 1: 1}

    def fib_store(n):
        if n in stored:
            return stored[n]
        stored[n] = fib_store(n - 1) + fib_store(n - 2)
        return stored[n]

    return [fib_store(n) for n in range(0, n + 1)]


for i in range(21):
    print(fib_3(i))


def time_functions(fib_func, seq_num):
    time_list = []
    for i in range(seq_num + 1):
        start = time.perf_counter()
        [fib_func(i) for _ in range(100)]
        stop = time.perf_counter()
        elapsed = stop - start
        time_list.append([i, elapsed])
    return time_list


fib1_time = time_functions(fib_1, 20)
fib2_time = time_functions(fib_2, 20)
fib3_time = time_functions(fib_3, 20)

df1 = pd.DataFrame(fib1_time, columns=['seq', 'Iterative'])
df2 = pd.DataFrame(fib2_time, columns=['seq', 'Recursive'])
df3 = pd.DataFrame(fib3_time, columns=['seq', 'Recur Cached'])

times_df = reduce(pd.merge, [df1, df2, df3])

times_df.drop(columns='seq').plot(kind='bar', logy=True, figsize=(12, 6), width=0.9)
