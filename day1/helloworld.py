my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list)//2):
    my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]

print(my_list)  # Output: [5, 4, 3, 2, 1]
