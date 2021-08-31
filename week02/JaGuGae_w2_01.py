import random
import time

random.seed(time.time())
a = list()

for _ in range(1000000):
    a.append(random.randint(1, 10000000))

start_time = time.time()
a.sort(reverse = True)
print('{} seconds'.format(time.time() - start_time))