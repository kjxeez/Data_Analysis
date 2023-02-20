import math
import itertools
import statistics

import numpy as np

N=6
y=[8,3,1,11,4,7]

n=2
#C_out=itertools.permutations(y,n) //с повторами
C_out=itertools.combinations(y,n)
C=math.factorial(N)/(math.factorial(n)*math.factorial(N-n))
#M_Y=
C_f_out = []
aa = []
bb = []
print('\033[32mпункт 1:\033[39m\n')
for i in C_out:
    a=np.mean(i)
    b=np.std(i)
    C_f_out.append(i)
    aa.append(a)
    bb.append(b)
    print(f'выборочное среднее пары {i}: {a}')
    print(f'среднеквадратичное отклонение пары {i}: {b}')
    print('')
print((C_f_out))
print(f'выборочное среднее выборок: {np.mean(aa)}')#сначала проходится по кортежам
print(f'среднее по совокупности: {np.mean(y)}')
print(f'\033[32m2 пункт а:\033[39m\nу_ср = {np.mean(aa)} = Y_ср = {np.mean(y)}')
aa=list(aa)

#D = sum((aa[x]-np.mean(y))**2 for x in range(N))
D=np.var(aa)
print(D)

print(f'Дисперсия: {D}')
print(f'\033[32m2 пункт б:\033[39m\nD = {D} = S^2(N-n)/nN = {(statistics.variance(y)/(n))*((N-n)/N)}')