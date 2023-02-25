import math

A = {0: 8, 1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 6: 0, 7: 0, 8: 0, 9: 1, 10: 1}
B = {0: 60, 1: 200 - 60}
N = 200
# рассмотрим первые результаты
n1 = 20
y1 = sum(i * A.get(i) for i in A)
y1_2 = sum(i**2*A.get(i) for i in A)
print(f'Всего испорченных зубов среди {n1} детей: {y1}')
n1_mean = y1 / n1
print(f'Среднее число испорченных зубов: {n1_mean}')

Y = N * n1_mean
print(f'\033[32mОценка суммарного числа испорченных зубов по результатам A: {Y}\033[39m')
D = 1/(n1-1)*(y1_2 - (y1 ** 2)/n1)
print(f'Дисперсия: {D}')
f = n1/N
print(f'Доля отбора: {f}')
std = math.sqrt(D)
stdy = (std*math.sqrt(1-f)/math.sqrt(n1))
print(f'Ст. ошибка среднего = {stdy}')
stdY = (N*std*math.sqrt(1-f)/math.sqrt(n1))
print(f'\033[31mСт. ошибка оценки общего количества испорченных зубов = {stdY}\033[39m')
n2 = n1-8
n2_mean = y1/n2
print(f'Среднее число испорченных зубов среди нездоровых ребят: {n2_mean}')
N2 = N-60
Y2 = N2 * n2_mean
print(f'\033[32mОценка суммарного числа испорченных зубов по результатам и А и Б: {Y2}\033[39m')
D = 1/(n2-1)*(y1_2 - (y1 ** 2)/n2)
print(f'Дисперсия: {D}')
f = n2/N2
print(f'Доля отбора: {f}')
std = math.sqrt(D)
stdy = (std*math.sqrt(1-f)/math.sqrt(n2))
print(f'Ст. ошибка среднего = {stdy}')
stdY = (N2*std*math.sqrt(1-f)/math.sqrt(n2))
print(f'\033[31mСт. ошибка оценки общего количества испорченных зубов = {stdY}\033[39m')

