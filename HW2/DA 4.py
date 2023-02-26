import math

N = 14000
A = {0: 100, 1: 200, 2: 120, 3: 40, 4: 20, 5: 20}
B = {4: 501, 5: 497, 6: 2}
N = N - sum(B.get(i) for i in B)
n = 500 - 40
y_mean = sum(i*A.get(i) for i in range(4))/n
print(f'выборочное среднее: {y_mean}')
Y = N*y_mean + sum(i*B.get(i) for i in B)
print(f'оценка общего числа детей: {Y}')

y2_mean = sum(i**2*A.get(i) for i in range(4))/n
D = n/(n-1)*(y2_mean-y_mean**2)
std = math.sqrt(D)
print(f'оценка среднего кв откл: {std}')
#0.95
Q = 1.96
stdy = 1.96*std/math.sqrt(n)*math.sqrt(1-n/N)
stdY = stdy*N
print(f'Оценка ошибки общей совокупности: {stdY}')
print(f'\033[31mДИ общего кол-ва детей в районе: {Y-stdY,Y+stdY}')