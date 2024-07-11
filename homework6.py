my_dict = {'Lera' : 1996, 'Ruslan' : 1993, 'Misha' : 2020}
print(my_dict)
print(my_dict.get('Lera'))
print(my_dict.get('Dasha'))
my_dict.update({'Tanya' : 1976,
                'Olya' : 1977})
print(my_dict)
a = my_dict.pop('Lera')
print(a)
print(my_dict)

my_set = {1, 'list', True, 3, 4, 5, 4, 3}
print(my_set)
print(my_set.add(9))
print(my_set.add(8))
print(my_set.discard(1))
print(my_set)