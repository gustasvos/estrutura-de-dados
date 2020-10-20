from timeit import timeit
import time

#print(timeit('''from random import sample

#a = sample(range(2000),2000)
#a.sort()''', number=11))

#print(timeit('''from random import sample

#randomlist = sample(range(2000),2000)
#randomlist = randomlist + sample(range(randomlist[-1]+2000),2000)''', number=))

from random import sample

randomlist = sample(range(2000),2000)
start = time.time()
randomlist = randomlist + sample(range(randomlist[-1]+2000),2000)
print(time.time() - start)
print(len(randomlist))