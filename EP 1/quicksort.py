def quicksort(v):
  if len(v) <= 1: return v    
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

from random import sample
import time
v = sample(range(10), 10)
#v = [5,4,6,3,2,0,1,7]
#print (v)
start_time = time.time()
v = quicksort(v)

print(round(time.time() - start_time, 2), "segundos")
#print(v)