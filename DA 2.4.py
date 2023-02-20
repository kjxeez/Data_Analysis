import math
N=83000
n=200
n_mean = 9943/n
n2_mean = 500388/n
print(f'средний вес груза: {n_mean}')
print(f'Общая масса грузов: {83000*n_mean}')
D=n2_mean-n_mean**2
#D=1/(n-1)*500388-n/(n-1)*n_mean**2
print(f'D = {D}')
print(f'Ст. ошибка = {math.sqrt(D)/math.sqrt(n)}')
