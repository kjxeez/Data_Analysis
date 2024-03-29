import math
X_before = [218, 588, 477, 537, 619, 614, 691, 543, 517, 563, 318, 417]
mean_before = sum(X_before)/len(X_before) #средневыборочное первое
std_before = (sum([(x - mean_before)**2 for x in X_before])/(len(X_before)-1))**0.5 #выборочное стандартное отклонение первое
X_after = [537, 398, 296, 440, 366, 524, 517, 413]
mean_after = sum(X_after)/len(X_after) #средневыборочное второе

std_after = (sum([(x - mean_after)**2 for x in X_after])/(len(X_after)-1))**0.5#выборочное стандартное отклонение второе

t = (mean_after - mean_before)/(math.sqrt((std_after**2/len(X_after)) + (std_before**2/len(X_before)))) # t-статистика

df = len(X_after) + len(X_before) - 2 #числа степеней свободы

t_critical = 2.010 # Можно использовать таблицу значений t-распределения для df = 18 и alpha = 0.05
print(f'по таблице: df = {df}, alpha = 0.05, t_k = {t_critical}')
if abs(t) > t_critical:
    print("Снижение показателя X после кризиса является статистически значимым")
else:
    print("Снижение показателя X после кризиса не является статистически значимым")