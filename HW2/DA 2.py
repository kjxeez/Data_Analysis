import math

N = 47500
n = 1970
n_mean = 559037 / n
n2_mean = 163533026 / n
print(f'средняя ЗП: {n_mean}')
print(f'Общая сумма ЗП: {N * n_mean}')
# D=n2_mean-n_mean**2
# D=1/(n-1)*163533026-n/(n-1)*n_mean**2
D = (163533026 - 559037 ** 2 / n) / ((n - 1))
print(f'D = {D}')
f = n / N
print(f'Доля отбора: {f}')
std = math.sqrt(D)
stdy = std * math.sqrt(1 - f) / math.sqrt(n)
# std=math.sqrt(D)/math.sqrt(n-1)
print(f'Ст. ошибка среднего = {stdy}')
stdY = N * std * math.sqrt(1 - f) / math.sqrt(n)
print(f'Ст. ошибка оценки суммы ЗП ({N * n_mean}) = {stdY}')
a = 1 - 0.95
Ql = -1.645
Qr = 1.645
yl = n_mean + Ql * stdy
print(f'Левая граница Д.И. для среднего: {yl}')
yr = n_mean + Qr * stdy
print(f'Правая граница Д.И. для среднего: {yr}')
print(f'\033[32mД.И для средней ЗП: {yl, yr}\033[39m')

Yl = N * n_mean + Ql * stdY
print(f'Левая граница Д.И. для суммарного: {Yl}')
Yr = N * n_mean + Qr * stdY
print(f'Правая граница Д.И. для суммарного: {Yr}')
print('(', Yl, ';', Yr, ')')
