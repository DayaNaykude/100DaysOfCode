# with open("weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     not_heading = False
#     for row in data:
#
#         if not_heading:
#             temperature = int(row[1])
#             temperatures.append(temperature)
#         not_heading = True
#         print(row)
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# sum_of_temperatures = sum(temp_list)
# average = sum_of_temperatures / len(temp_list)
# print(average)

# average temperature
# average_temp = data["temp"].mean()
# print(average_temp)
#
# # max value
# maximum_temp = data["temp"].max()
# print(maximum_temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_fahrenheit = (monday_temp * (9/5)) + 32
# print(monday_temp_fahrenheit)

# data_dict = {
#     "students": ["Amy", "James", "Angela","Dayanand"],
#     "scores": [76, 56, 65, 98]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrle_count")