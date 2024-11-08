n_list = [1, 2, 3, 4]
# 1. adding item at the desired location
# adding element 100 at the fourth location as the first one is zero
n_list.insert(3, 100)
# list: [1, 2, 3, 100, 4]
print(n_list)
# 2. adding element at the end of the list
n_list.append(99)
# list: [1, 2, 3, 100, 4, 99]
print(n_list)
# 3. adding several elements at the end of list
# the following statement can also be written like this:
# n_list + [11, 22]
n_list.extend([11, 22])
# list: [1, 2, 3, 100, 4, 99, 11, 22]
print(n_list)
