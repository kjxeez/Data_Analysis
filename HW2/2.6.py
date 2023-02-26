import math

N = 676 - 326
n=50-23
y=1471
y2=54497
y_mean = ((y-42*23)/n)
Y_676=N*y_mean+326*42
print(f'оценка общего числа подписей: {Y_676}')

y2_mean =(y2-42**2*23)/n
D=n/(n-1)*(y2_mean-y_mean**2)
print(f'оценка среднего кв. откл.: {math.sqrt(D)}')

std = math.sqrt(D)/math.sqrt(n)*math.sqrt(1-n/N)
print(f'std: {std}')

stdY = N*std
print(f'std Y {stdY}')
print(f'\033[31mУлучшенная оценка общего числа подписей = {Y_676} при ст. ошибке {stdY}')