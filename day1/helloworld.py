# my_list = [1, 2, 3, 4, 5]

# for i in range(len(my_list)//2):
#     my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]

# print(my_list)  # Output: [5, 4, 3, 2, 1]

def romantoint(roman_num):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(roman_num):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
