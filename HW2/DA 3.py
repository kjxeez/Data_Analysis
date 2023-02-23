import math

N = 483
n = 60
n_mean = round(81796/n)
n2_mean = round(112805447/n)
print(f'среднее кол-во студентов: {n_mean}')
print(f'Общее колво студентов: {N*n_mean}')
#D=n2_mean-n_mean**2
#D=1/(n-1)*112805447-n/(n-1)*n_mean**2
D=round((112805447-81796**2/n)/((n-1)))
print(f'D = {D}')
f=n/N
print(f'Доля отбора: {f}')
std=math.sqrt(D)
stdy=round(std*math.sqrt(1-f)/math.sqrt(n))
#std=math.sqrt(D)/math.sqrt(n-1)
print(f'Ст. ошибка среднего = {stdy}')
stdY=round(N*std*math.sqrt(1-f)/math.sqrt(n))
print(f'Ст. ошибка оценки общего количества студентов ({N*n_mean}) = {stdY}')
a=1-0.95
Ql=-1.96
Qr=1.96
yl=round(n_mean+Ql*stdy)
print(f'Левая граница Д.И. для среднего: {yl}')
yr=round(n_mean+Qr*stdy)
print(f'Правая граница Д.И. для среднего: {yr}')
print(f'\033[32mД.И для среднего количества студентов: {yl,yr}\033[39m')

Yl =round(N*n_mean+Ql*stdY)
print(f'Левая граница Д.И. для суммарного: {Yl}')
Yr = round(N*n_mean+Qr*stdY)
print(f'Правая граница Д.И. для суммарного: {Yr}')
print('(',Yl, ';', Yr,')')
