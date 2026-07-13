# age = int(input("Enter your age: "))
# if age >=18:
#     print("You are old enough to learn a driving license.")
# else:
#     print("You need " + str(18 - age) + " more years to learn a driving license.")

# fruits = ['banana', 'orange', 'mango', 'lemon']
# userFruit = input("Enter a fruit name: ")
# if userFruit in fruits:
#     print("This fruit already exists in the list.")
# else:
#     fruits.append(userFruit)
#     print("Fruit added to the list.")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print('Python is a skill')
    if "JavaScript" in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'Python' in person['skills']:
        print('He is a backend developer')

if 'is_married' in person and person['is_married'] == True and 'country' in person and person['country'] == 'Finland':
    print(person['first_name'] + ' ' + person['last_name'] + ' lives in ' + person['country'] + '. He is married.')
