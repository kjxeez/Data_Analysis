import math

A = {0: 8, 1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 6: 0, 7: 0, 8: 0, 9: 1, 10: 1}
B = {0: 60, 1: 200 - 60}
N = 200
# рассмотрим первые результаты
n1 = 20
y1 = sum(i * A.get(i) for i in A)
y1_2 = sum(i**2*A.get(i) for i in A)
print(f'Всего испорченных зубов среди {n1} детей: {y1}')
n1_mean=(y1 + 8) / n1
print(f'Среднее число испорченных зубов: {n1_mean}')

Y = N * y1 / n1
print(f'\033[32mОценка суммарного числа испорченных зубов по результатам A: {Y}\033[39m')
D = 1/(n1-1)*(y1_2 - (y1 ** 2)/n1)
print(f'Дисперсия: {D}')
f = n1/N
print(f'Доля отбора: {f}')
std = math.sqrt(D)
stdy = (std*math.sqrt(1-f)/math.sqrt(n1))
print(f'Ст. ошибка среднего = {stdy}')
stdY = (N*std*math.sqrt(1-f)/math.sqrt(n1))
print(f'Ст. ошибка оценки общего количества испорченных зубов ({N*n1_mean}) = {stdY}')

n2 = 200
n2_mean = 4
y2 = sum(i * A.get(i) for i in A)
y2_2 = sum(A.get(i) ** 2 for i in A)
print(f'\033[32mОценка суммарного числа испорченных зубов по результатам и А и Б: {n1_mean*(N-60)}\033[39m')

