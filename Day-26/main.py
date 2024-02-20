# LIST COMPREHENSION

# items = ["Pune", "Mumbai", "Indapur", "Thane", "Sangali"]
#
# new_items = [item + "s" for item in items if item == "Pune"]
# print(new_items)

# numbers = [1, 2, 3, 4]
#
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

#
# cities = ["Pune", "Mumbai", "Indapur", "Thane", "Sangali"]
#
# capital_cities_names = [city.upper() for city in cities if len(city) > 5]
#
# print(capital_cities_names)

# DICTIONARY COMPREHENSION

names = ["Alex", "Beth", "Dayanand", "Sagar", "Ram"]

import random

students_scores = {name: random.randint(1, 100) for name in names}

print(students_scores.items())

passed_students = {name: score for (name, score) in students_scores.items() if score > 60}
print(passed_students)
