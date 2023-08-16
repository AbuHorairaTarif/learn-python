my_tuple = (1, 2, 3, 4)
my_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
print(my_dict.get(0))
print(my_dict.get(1))
print(my_dict.get(2))
print(my_dict.get(3))

merged_list = []
for i in range(len(my_tuple)):
    merged_list.append((my_tuple[i], my_dict.get(i)))
print(merged_list)
