# arquivo temporario, so ignora

from random import randint, sample

a = sample(range(1),1)
print(a)

for i in range(20):
    # qnd i for igual a 2000 adicionar uma lista de 2000 numeros 
    if i in [9] :
        a.append(sample(range(5),5))
    #print(i)
    else:
        a.append(randint(1,10))

print(a)
print(len(a))