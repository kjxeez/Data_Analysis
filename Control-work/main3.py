import math
A = [9.93, 10, 10.09, 10.04, 9.96, 9.97, 9.91, 9.99, 10.06, 9.98, 9.96, 10.05, 10.12, 10.02, 10.03]
B = [9.96, 9.98, 10.01, 9.98, 10.09, 10.03, 10, 10, 10.01, 10.04, 9.94, 10.02, 9.95, 10.02, 10]

mean_A = sum(A) / len(A) #средневыборочное А
mean_B = sum(B) / len(B) #средневыборочное Б

std_A = (sum((x - mean_A)**2 for x in A) / (len(A) - 1))**0.5 #выборочное стандартное отклонение А
std_B = (sum((x - mean_B)**2 for x in B) / (len(B) - 1))**0.5 #выборочное стандартное отклонение Б

t = (mean_B - mean_A) / (math.sqrt(std_A**2/len(A) + std_B**2/len(B))) # t-статистика
df = len(A) + len(B) - 2 #числа степеней свободы
t_critical=2.048
print(f'по таблице: df = {df}, alpha = 0.05, t_k = {t_critical}')
if abs(t) >t_critical: #по таблице
    print("Различия между выборками значимы, оборудование типа Б справляется со своей задачей лучше, чем оборудование типа А.")
else:
    print("Различия между выборками незначительны, нельзя сделать вывод о том, что одно оборудование лучше другого.")