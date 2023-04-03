import math
from scipy.stats import t
# данные выборок
n1 = 29
x1 = 2.5
s1 = math.sqrt(0.67)
n2 = 16
x2 = 2.06
s2 = math.sqrt(0.42)
# вычисление стандартной ошибки
SE = math.sqrt(s1**2/n1 + s2**2/n2)
# вычисление t-статистики
t_stat = (x1 - x2) / SE
# определение критической области
alpha = 0.05
df = n1 + n2 - 2
t_crit = t.ppf(alpha/2, df)
t_crit_upper = t.ppf(1 - alpha/2, df)
# вывод результатов
print('t-статистика:', t_stat)
print('Критическая область: ({:.3f}, {:.3f})'.format(t_crit, t_crit_upper))
if t_stat < t_crit or t_stat > t_crit_upper:
    print('Гипотеза H0 отвергается в пользу гипотезы H1.')
else:
    print('Гипотеза H0 не может быть отвергнута.')
