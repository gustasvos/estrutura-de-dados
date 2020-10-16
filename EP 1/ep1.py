from random import sample, randint
import time

randomlist = sample(range(2000),2000)
print(len(randomlist))
start_time = time.time()

for i in range(2000):
    randomlist.append(randint(2000, 2000))

print(round(time.time() - start_time, 2) , "segundos")
print(len(randomlist))

#for i in range(5): a.append(randint(1,100))
