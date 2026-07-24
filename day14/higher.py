from countries import countries_data


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(map(lambda x: x.upper(), countries)))

# def starts_with_E(country):
#      return country.startswith('E')

# print(list(filter(starts_with_E, countries)))

# def capAnd_filter():
#     return [c for c in map(lambda x: x.upper(), filter(starts_with_E, countries))]

# print(capAnd_filter())

# def catogorize_countries_by_pattern(pattern):
#     return list(filter(lambda country: pattern in country["name"], countries_data))

# print(catogorize_countries_by_pattern('land'))