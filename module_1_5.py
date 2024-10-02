immutable_var = (1, True, None, [1, 4], 'True', {3: 5})

print(immutable_var)

"""immutable_var[0] = 12 Не сработает ибо кортеж неизменяем. Как вариант присвоить новый кортеж,
где сначала будет элемент 12"""

mutable_list = [1, True, None, [1, 4], 'True', {3: 5}]

del mutable_list[0]

print(mutable_list)