from random import randint
from time import time
 
def quicksort(v):
  if len(v) <= 1: return v    
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)


# tamanho=0
# l=[]
# start = time.time()
# while(tamanho <=20000):
#     tamanho+=2000
#     print("\nNumero de elementos: ",len(l))
#     l+=[random.randint(0,tamanho) for x in range (2000)]
#     final = time.time() - start
#     quicksort(l)
#     print("tempo: ", final)


x = 0
lista = []
start = time()
for x in range(12):
    x+=2000
    print("\nNumero de deregue: ", len(lista))
    lista+=[randint(0,x) for x in range(2000)]
    final = time() - start
    print("tempo: ", round(final, 3))
    quicksort(lista)
    #mergesort(lista)
    #seleção(lista)
    #lista.sort()

