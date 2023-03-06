import math

N = 7100000
n = 1350
n_mean = 658.01 / n
n2_mean = 336.96 / n
print(f'среднее пребывание в метро: {n_mean}')
print(f'\033[32mОбщая сумма часов: {N * n_mean}\033[39m')
# D=n2_mean-n_mean**2
# D=1/(n-1)*163533026-n/(n-1)*n_mean**2
D = (336.96 - 658.01 ** 2 / n) / ((n - 1))
print(f'D = {D}')
f = n / N
print(f'Доля отбора: {f}')
std = math.sqrt(D)
stdy = std * math.sqrt(1 - f) / math.sqrt(n)
print(f'Ст. ошибка среднего = {stdy}')
stdY = N * std * math.sqrt(1 - f) / math.sqrt(n)
print(f'Ст. ошибка оценки суммы часов в метро ({N * n_mean}) = {stdY}')
a = 1 - 0.95
Ql = -1.96
Qr = 1.96
yl = n_mean + Ql * stdy
print(f'Левая граница Д.И. для среднего: {yl}')
yr = n_mean + Qr * stdy
print(f'Правая граница Д.И. для среднего: {yr}')
print(f'Д.И для средней ЗП: {yl, yr}')

Yl = N * n_mean + Ql * stdY
print(f'Левая граница Д.И. для суммарного: {Yl}')
Yr = N * n_mean + Qr * stdY
print(f'Правая граница Д.И. для суммарного: {Yr}')
print('\033[32m(', Yl, ';', Yr, ')\033[39m')