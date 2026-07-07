import goat

firstcountry, secondcountry, thirdcountry, *rest = goat.countries

print(firstcountry)
print(secondcountry)
print(thirdcountry)
print(rest[-1])