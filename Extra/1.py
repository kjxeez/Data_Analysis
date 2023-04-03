import numpy as np
from scipy.stats import ttest_ind
before = np.array([52.4, 56.1, 48.6, 46.5, 46.0, 42.2, 48.8, 56.6, 59.8, 49.7, 51.6])
after = np.array([49.3, 47.7, 52.9, 48.3, 49.1, 46.4, 47.0, 52.0, 51.5, 51.2, 49.8])
mean_before = np.mean(before)
std_before = np.std(before, ddof=1)
mean_after = np.mean(after)

std_after = np.std(after, ddof=1)
print(f'std before: {std_before}')
print(f'std after: {std_after}')
t_statistic, p_value = ttest_ind(before, after, equal_var=True)
print('хоть и среднестатистическое отклонение уменьшилось, посмотрим на результаты по Фишеру')
if p_value < 0.05:
    print("Результат является статистически значимым, точность изготовления деталей увеличилась после наладки станка.")
else:
    print("Результат не является статистически значимым, точность изготовления деталей не увеличилась после наладки станка.")