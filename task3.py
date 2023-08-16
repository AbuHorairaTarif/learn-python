import random

# Generating 10 random lists, each containing 10 random numbers between 1 and 10
num_lists = 10
list_length = 10

random_lists = []

for i in range(num_lists):
    random_list = [random.randint(1, 10) for item in range(10)]
    random_lists.append(random_list)
    print(random_list)
# Convert each list to a tuple and store in a set
list_tuples = [tuple(lst) for lst in random_lists]

tuple_set = set(random_list)

if len(random_list) == len(tuple_set):
    print("No duplicate lists found.")
else:
    print("Duplicate lists found.")