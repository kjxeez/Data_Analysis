import itertools
import statistics
import numpy as np
N=6
y=[8,3,1,11,4,7]
n=3
C=list(itertools.combinations(y,n))
print(f'Кол-во выборок: {len(C)}')
print(C)

s2=[]

#E - среднее по всем возможным выборкам
print('\033[32mпункт 1:\033[39m')
for i in C:
    print(f's^2 для группы {i}: {statistics.variance(i)}')
    s2.append(statistics.variance(i))
#S2=np.mean(s2)
Es2=sum(s2)/len(C)
S2 = statistics.variance(y)
z=0
for i in y:
    z=z+(i-np.mean(y))**2
z=z/5
#S2=z
print('\033[32mпункт 2:\033[39m')
print(f'E(s2) = {Es2} = S2 = {S2}')
