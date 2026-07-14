# def evens_and_odds(number):
#     evens = []
#     odds = []
#     for num in range(1, number+1, 1):
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
#     return evens, odds

# print(evens_and_odds(10))

# def greet(name="Guest"):
#     return f"Hello {name}"

# print(greet())
# print(greet("John"))

# def show_args(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print(show_args(name="John", age=30, country="USA"))

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(11))  # True
# print(is_prime(4))   # False

# def isUnique(lst):
#     return len(lst) == len(set(lst))

# print(isUnique([1, 2, 3, 4, 5]))  # True
# print(isUnique([1, 2, 3, 4, 5, 1]))  # False

# def sameDataType(lst):
#     if not lst:
#         return True
#     first_type = type(lst[0])
#     for item in lst:
#         if type(item) != first_type:
#             return False
#     return True

# print(sameDataType([1, 2, 3, 4]))  # True
# print(sameDataType([1, "2", 3, 4]))  #false

def validVariable(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

print(validVariable("my_var"))  # True
print(validVariable("2var"))    # False
print(validVariable("in"))      # False