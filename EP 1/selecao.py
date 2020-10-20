def seleção(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

from random import sample
import time
v = sample(range(10), 10)
#v = [5,4,6,3,2,0,1,7]
print (v)
start_time = time.time()
v = seleção(v)

print(round(time.time() - start_time, 2), "segundos")
print(v)