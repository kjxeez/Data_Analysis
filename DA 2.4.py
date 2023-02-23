import math

N=83000
n=200
n_mean = 9943/n
n2_mean = 500388/n
print(f'средний вес груза: {n_mean}')
print(f'Общая масса грузов: {83000*n_mean}')
#D=n2_mean-n_mean**2
#D=1/(n-1)*500388-n/(n-1)*n_mean**2
D=(500388-9943**2/n)/((n-1))
print(f'D = {D}')
f=n/N
print(f'Доля отбора: {f}')
std=math.sqrt(D)
stdy=std*math.sqrt(1-f)/math.sqrt(n)
#std=math.sqrt(D)/math.sqrt(n-1)
print(f'Ст. ошибка среднего = {stdy}')
stdY=N*std*math.sqrt(1-f)/math.sqrt(n)
print(f'Ст. ошибка оценки массы груза ({83000*n_mean}) = {stdY}')
a=1-0.95
Ql=-1.96
Qr=1.96
yl=n_mean+Ql*stdy
print(f'Левая граница Д.И. для среднего: {yl}')
yr=n_mean+Qr*stdy
print(f'Правая граница Д.И. для среднего: {yr}')
Yl = N*n_mean+Ql*stdY
print(f'Левая граница Д.И. для суммарного: {Yl}')
Yr = N*n_mean+Qr*stdY
print(f'Правая граница Д.И. для суммарного: {Yr}')
print('(',Yl, ';', Yr,')')