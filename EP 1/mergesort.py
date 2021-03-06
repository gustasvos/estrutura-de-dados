def mergesort(v):
    if len(v) <= 1: return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

from random import sample
import time
v = sample(range(10), 10)
#v = [5,4,6,3,2,0,1,7]
#print (v)
start_time = time.time()
v = mergesort(v)

print(round(time.time() - start_time, 2), "segundos")
#print(v)