# Лабораторная работа №4, вариант 10
# Инвентарь 3x3 (9 ячеек), болезни нет, стартовые очки = 10

from itertools import product

# Предметы: обозначение, размер (ячеек), очки выживания
items = [
    ('r', 3, 25), ('p', 2, 15), ('a', 2, 15), ('m', 2, 20),
    ('i', 1, 5), ('k', 1, 15), ('x', 3, 20), ('t', 1, 25),
    ('f', 1, 15), ('d', 1, 10), ('s', 2, 20), ('c', 2, 20),
]

capacity = 9       # 3x3 ячеек
start_points = 10  # стартовые очки

best_score = -1000
best_items = []

# Перебираем все комбинации: 1 - предмет берём, 0 - оставляем
for choice in product([0, 1], repeat=len(items)):
    score = start_points
    used = 0
    chosen = []
    for item, take in zip(items, choice):
        name, size, points = item
        if take == 1:
            score += points   # взяли - очки прибавляем
            used += size      # и занимаем место
            chosen.append(item)
        else:
            score -= points   # оставили - очки вычитаем

    # Запоминаем лучшую комбинацию, которая помещается в рюкзак
    if used <= capacity and score > best_score:
        best_score = score
        best_items = chosen

# Раскладываем предметы по ячейкам (предмет размером 3 занимает 3 ячейки)
inventory = []
for name, size, points in best_items:
    inventory += [name] * size

# Пустые ячейки обозначаем знаком '-'
inventory += ['-'] * (capacity - len(inventory))

# Выводим инвентарь по 3 ячейки в строке
for i in range(0, capacity, 3):
    print(','.join('[' + c + ']' for c in inventory[i:i + 3]))

print()
print('Итоговые очки выживания:', best_score)

# Итоговый счёт должен быть положительным
if best_score > 0:
    print('Счёт положительный, Том дойдёт до вышки!')
else:
    print('Счёт не положительный, решения нет.')
