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
v = sample(range(10), 10)
#v = [5,4,6,3,2,0,1,7]
print (v)
v = mergesort(v)
print (v)


#=================================================================


def quicksort(v):
  if len(v) <= 1: return v    
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

from random import sample
v = sample(range(10), 10)
print (v)
v = quicksort(v)
print (v)

#==================================================================

def seleção(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

from random import sample
v = sample(range(10), 10)
print (v)
v = seleção(v)
print (v)


#==================================================================

