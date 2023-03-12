from scipy import stats
from scipy.stats import kendalltau

population = [1372859000, 1271775000, 31861500, 252812245, 203261122, 189612027, 178516904, 157503337, 146267288, 126910000, 119713203, 101108300]
area = [9598962, 3287590, 9519431, 1904556, 8514877, 803940, 923768, 144000,17125407, 377835, 1972550, 299764]

r, p_value = stats.pearsonr(population, area)

print("Коэффициент корреляции Пирсона: ", r)
print("p-value: ", p_value)

if p_value < 0.05:
    print("\033[32mпо пирсону: Зависимость статистически значима\033[39m")
else:
    print("\033[32mпо пирсону: Зависимость статистически не значима\033[39m")

r_s, p_value_s = stats.spearmanr(population, area)

print("Коэффициент корреляции Спирмена: ", r_s)
print("p-value: ", p_value_s)

if p_value_s < 0.05:
    print("\033[32mпо спирмену: Зависимость статистически значима\033[39m")
else:
    print("\033[32mпо спирмену: Зависимость статистически не значима\033[39m")



# Рассчитываем ранги для численности населения
population_rank = [sorted(population).index(x)+1 for x in population]

# Рассчитываем ранги для площади
area_rank = [sorted(area).index(x)+1 for x in area]

# Рассчитываем коэффициент корреляции Кендалла и p-value
corr, pval = kendalltau(population_rank, area_rank)

# Выводим результаты
print("Коэффициент корреляции Кендалла: ", corr)
print("p-value: ", pval)
alpha = 0.05
if p_value < alpha:
    print("\033[32mПо критерию Кендалла отвергаем нулевую гипотезу о независимости переменных.\033[39m")
else:
    print(
        "\033[32mПо критерию Кендалла не получилось отвергнуть нулевую гипотезу о независимости переменных.\nПеременные независимы\033[39m")
