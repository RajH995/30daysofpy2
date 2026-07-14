from countries import countries_data
# for i in range(10, -1, -1):
#     print(i)

# count = 10
# while count > -1:
#     print(count)
#     count -= 1

# for i in range(7):
#     print("#"*(i+1))

# fruits = ['banana', 'orange', 'mango', 'lemon', "peach", "grapes", "kiwi"]


# for i in range(len(fruits)//2):
#     fruits[i], fruits[~i] = fruits[~i], fruits[i]

# print(fruits)

# languages = {}

# for country in countries_data:
#     for language in country['languages']:
#         if language in languages:
#             languages[language] += 1
#         else:
#             languages[language] = 1

# top_ten_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]

# print(top_ten_languages)

population = {}
for country in countries_data:
    population[country['name']] = country['population']

top_ten_populated_countries = sorted(population.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_ten_populated_countries)
