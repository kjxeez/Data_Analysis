from scipy.stats import kendalltau

children = [4, 1, 2, 2, 3, 2, 3, 1, 4, 3]
welfare = [5, 3, 1, 4, 2, 5, 1, 3, 4, 2]

corr, p_value = kendalltau(children, welfare)
print("Статистика критерия: ", corr)
print("p-значение: ", p_value)

alpha = 0.05

if p_value < alpha:
    print("\033[32mОтвергаем гипотезу о независимости количества детей и материального благополучия \033[39m")
else:
    print("\033[32mПринимаем гипотезу о независимости количества детей и материального благополучия \033[39m")