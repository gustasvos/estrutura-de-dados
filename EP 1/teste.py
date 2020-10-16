from random import randint, sample

a = sample(range(1),1)
print(a)

for i in range(20):
    if i in [9] :
        a.append(randint(i,i+10000))
    #print(i)
    else:
        a.append(randint(1,10))

print(a)
print(len(a))