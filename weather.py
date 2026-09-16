import os

location = ["data", "weather", "observations.txt"]

fullpath = os.path.join(*location)
print(fullpath)

if not os.path.exists(os.path.dirname(fullpath)):
    os.makedirs(os.path.dirname(fullpath))

temps = {
    "Perth": 20,
    "Brisbane": 327,
    "Melbourne": -2,
    "Sydney": 24
}

with open(fullpath, "w") as out_file:
    for city, temperature in temps.items():
        out_file.write(f"{city}:{temperature}\n")

weather_dictionary = dict()
weather_list = list()

with open(fullpath, "r") as in_file:
    all_lines = in_file.readlines()

    for line in all_lines:
        bits = line.split(":")

        city = bits[0].strip()
        temperature = int(bits[1].strip())

        weather_dictionary[city] = temperature
        weather_list.append((city, temperature))

print(weather_dictionary)
print(weather_list)