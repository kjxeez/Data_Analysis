import math

N = 14000
C = {0: 100, 1: 200, 2: 120, 3: 40, 4: 20, 5: 20}
#95% общее колво детей в районе
n=sum(C.get(i) for i in C)
print(n)
y1 = sum(i*C.get(i) for i in C)
print(y1)
y2 = sum(i**2*C.get(i) for i in C)

Y = N*y1/n
print(f'оценка суммарного числа детей: {Y}')
D=1/(n-1)*(y2-y1**2/n)
print(f'D = {D}')

o=math.sqrt(D/n*(1-n/N))
p=0.95
t=3
inc = t*o
yl = (n_mean+Ql*stdy)
print(f'Левая граница Д.И. для среднего: {yl}')
yr = (n_mean+Qr*stdy)
print(f'Правая граница Д.И. для среднего: {yr}')
