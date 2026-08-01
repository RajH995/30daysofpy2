# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 -(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)
#     print("worked")
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')




# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
#     # Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))



# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# *nordic_countries, es, ru = names

# print(nordic_countries)

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

my_nums = [1, 2, 3, 4, 5]

my_letters = ["A", "B", "C", "D", "E"]

print(dict(zip(my_nums, my_letters)))  # {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

# user_dict = {'name': 'Alice', 'age': 30}
# status = ['Verified', 'Active']

# for (key, value), stat in zip(user_dict.items(), status):
#     print(f"{key}: {value} -> Status: {stat}")
