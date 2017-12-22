import numpy as np

with open("day6.txt") as f:
    banks = np.array([int(i) for i in f.readline().split()])

l = len(banks)
configurations = dict()
configurations[tuple(banks)] = 0

c = 0
while True:
    c += 1
    i_max = np.argmax(banks)
    m = banks[i_max]
    
    q, r = divmod(m,l)
    
    banks[i_max] = 0
    banks += q
    for offset in range(r):
        banks[(i_max + 1 + offset)%l] += 1
    print(banks) 
    conf = tuple(banks)
   
    if conf not in configurations:
        configurations[conf] = c
    else:
        print(c,configurations[conf])
        print(c - configurations[conf])
        break

print(c)
