# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# print([num for num in numbers if num > 0])  # Output: [2, 4, 6]

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print([num for sublist in list_of_lists for num in sublist])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print([tuple([x] + (lambda base: [base**y for y in range(6)])(x)) for x in range(11)]) hard to understand but it works

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# print(list(map(lambda country, city: [country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()], countries)))


# print(list(map(
#     lambda country, city: [country.upper(), country[:3].upper(), city.upper()],
#     (c[0][0] for c in countries),
#     (c[0][1] for c in countries)
# )))

# print([[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries])

# print([{"Country": country.upper(), "Capital": capital.upper()} for [(country, capital)] in countries])

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# print([first + ' ' + last for [(first, last)] in names])  # Output: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None

intercept = lambda x1, y1, slope: y1 - slope * x1

print(slope(1, 2, 3, 4))  # Output: 1.0
print(intercept(1, 2, slope(1, 2, 3, 4)))  # Output: 1.0