from random import randint
from time import time

def seleção(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

x = 0 
lista = []
start = time()
for x in range(12):
    x+=2000
    print("\nNumero de deregue: ", len(lista))
    lista+=[randint(0,x) for x in range(2000)]
    final = time() - start
    seleção(lista)
    print("Tempo: ", round(final, 3))