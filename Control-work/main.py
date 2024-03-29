import math
N=10396
# размер выборки
n = 30

# число людей в каждом домохозяйстве
x = [5, 6, 3, 3, 2, 3, 3, 3, 4, 9, 3, 2, 7, 4, 3, 5, 6, 4, 3, 3, 4, 3, 1, 1, 2, 4, 3, 4, 2, 4]

# выборочное среднее
x_bar = sum(x) / n

# выборочное стандартное отклонение
s = math.sqrt(sum([(xi - x_bar)**2 for xi in x]) / (n - 1))

# критическое значение стандартного нормального распределения для доверительной вероятности 0.95
z = 1.96 # по таблице

# нижняя граница доверительного интервала
lower = x_bar - z * (s / math.sqrt(n))

# верхняя граница доверительного интервала
upper = x_bar + z * (s / math.sqrt(n))

# общее число людей в районе
total = x_bar * N

print("Общее число людей в районе: {:.0f}".format(total))
print("95%-доверительный интервал для общего числа людей в районе: ({:.0f}, {:.0f})".format(lower * N, upper * N))