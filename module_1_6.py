my_dict = {'Vlad': 1999, 'Max': 1988, 'Anton': 1987}

print(my_dict, my_dict['Vlad'], my_dict.setdefault('Kirill', 1980), sep='\n')
my_dict['Anatoliy'] = 1976
my_dict['Victor'] = 1985
print(my_dict.pop('Max'))
print(my_dict)

my_set = {1, 2, 3, 4, 5, 6, 4, True, (1,), (1,)}
print(my_set)
my_set.add(9)
my_set.add(8)
my_set.remove(1)
print(my_set)

