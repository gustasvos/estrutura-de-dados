from random import sample, randint
import time

randomlist = sample(range(2000),2000)
print(len(randomlist))
start_time = time.time()


for i in range(10):
    randomlist = randomlist + sample(range(randomlist[-1]+2000),2000)

print(round(time.time() - start_time, 3) , "segundos")
print(len(randomlist))

#for i in range(5): a.append(randint(1,100))