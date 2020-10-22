from random import randint
from time import time

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


#=================================================================


def quicksort(v):
  if len(v) <= 1: return v    
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

#==================================================================

def selecao(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r


#==================================================================

# talvez esse seja o for dos testes

# x = 0
# lista = []
# start = time()
# for x in range(12):
#     x+=2000
#     print("\nNumero de deregue: ", len(lista))
#     lista+=[randint(0,x) for x in range(2000)]
#     final = time() - start
#     print("Tempo: ", round(final, 3))
#     #quicksort(lista)
#     #mergesort(lista)
#     #seleção(lista)
#     #lista.sort()

def vetormergesort():
  x = 0
  lista = []
  start = time()
  for x in range(12):
    x += 2000
    print("\nlen merge: ", len(lista))
    lista += [randint(0,x) for x in range(2000)]
    mergesort(lista)
    print(time() - start)

def vetorquicksort():
  x = 0
  lista = []
  start = time()
  for x in range(12):
    x += 2000
    print("\nlen quick: ", len(lista))
    lista += [randint(0,x) for x in range(2000)]
    quicksort(lista)
    print(time() - start)

def vetorselecao():
  x = 0
  lista = []
  start = time()
  for x in range(12):
    x += 2000
    print("\nlen selec: ", len(lista))
    lista += [randint(0,x) for x in range(2000)]
    lista = selecao(lista)
    print(time() - start)

def vetornativo():
  x = 0
  lista = []
  start = time()
  for x in range(12):
    x += 2000
    print("\nlen nativ: ", len(lista))
    lista += [randint(0,x) for x in range(2000)]
    lista.sort()
    print(time() - start)

v1 = vetormergesort()
v2 = vetorquicksort()
v3 = vetorselecao()
v4 = vetornativo()

#print(len(v1))