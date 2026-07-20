from random import *

# def list_of_hexa_colors(n):
#     hexa_colors = []
#     for i in range(n):
#         color = '#'
#         for j in range(6):
#             color += choice('0123456789ABCDEF')
#         hexa_colors.append(color)
#     return hexa_colors

# def list_of_rgb_colors(n):
#     rgb_colors = []
#     for i in range(n):
#         color = f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'
#         rgb_colors.append(color)
#     return rgb_colors

# def generate_colors(color_type, n):
#     if color_type == 'hexa':
#         return list_of_hexa_colors(n)
#     elif color_type == 'rgb':
#         return list_of_rgb_colors(n)
#     else:
#         raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")
    
# print(generate_colors('hexa', 5))  # Example usage
# print(generate_colors('rgb', 5))   # Example usage

# def shuffle_list(list):
#     shuffled_list = list.copy()
#     shuffle(shuffled_list)
#     return shuffled_list

# my_list = [1, 2, 3, 4, 5]
# shuffled_list = shuffle_list(my_list)
# print(shuffled_list)  # Output: A shuffled version of my_list

# def random_number_list():
#     list_of_random_numbers = []
#     for i in range(9):
#         random_number = randint(0, 9)
#         if random_number not in list_of_random_numbers:
#             list_of_random_numbers.append(random_number)
#     return list_of_random_numbers

# print(random_number_list())  # Output: A list of 9 unique random numbers between 0 and 9

def random_number_list():
    list_of_random_numbers = set()
    while len(list_of_random_numbers) < 9:
        list_of_random_numbers.add(randint(0, 2345))
    return list_of_random_numbers

print(random_number_list())  # Output: A list of 9 unique random numbers between 0 and 9
    