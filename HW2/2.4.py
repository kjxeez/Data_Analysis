import math

import numpy as np

N = 14848

C = [5, 6, 3, 3, 2, 3, 3, 3, 4, 4, 3, 2, 7, 4, 3, 5, 4, 4, 3, 3, 4, 3, 3, 1, 2, 4, 3, 4, 2, 4]
n = 30

y = sum(x for x in C)
y2 = sum(x ** 2 for x in C)
print(f'y: {y}')
print(f'y2: {y2}')
Y = N * y / n
print(f'\033[32mY, общее число людей в районе: {Y}\033[39m')
f=n/N
D = (1 / (n - 1)) * (y2 - y ** 2 / n)
print(f'D: {D}')
a=1-0.1
Ql=-1.64
Qr=1.64

stdy = math.sqrt(D)
stdY = N*math.sqrt(D)*math.sqrt(1-f)/math.sqrt(n)
yl=np.mean(C)+Ql*stdy
print(f'Левая граница Д.И. для среднего: {yl}')
yr=np.mean(C)+Qr*stdy
print(f'Правая граница Д.И. для среднего: {yr}')
print(f'Д.И для среднего колва людей: {yl,yr}')

Yl = N*np.mean(C)+Ql*stdY
print(f'Левая граница Д.И. для суммарного: {Yl}')
Yr = N*np.mean(C)+Qr*stdY
print(f'Правая граница Д.И. для суммарного: {Yr}')
print(f'\033[32m({Yl}; {Yr})\033[39m')
a = 0.131
P=1-a
print(f'доверительная вероятность +- 10% : {P}')