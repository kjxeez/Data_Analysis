import itertools
import math

import numpy as np
import statistics

N=6
y=[8,3,1,11,4,7]

n=2
C=list(itertools.permutations(y,n))
print('\033[32mпункт 1:\033[39m')
print(f'Кол-во выборок: {len(C)}')
print(C)
aa=[]
for i in C:
    aa.append(np.mean(i))
aa=list(aa)
#Vy-истинная дисперсия
z=0
for i in y:
    z=z+(i-np.mean(y))**2
z=z/N
#print(z)
S2 = statistics.variance(aa)

D = np.std(y)**2
#стандарт. ошибка в квадрате = дисперсия
print('\033[32mпункт 2:\033[39m')
print(f'D = {D/n} = S^2(N-1)/nN = {(statistics.variance(y)*(N-1))/(n*N)}')
