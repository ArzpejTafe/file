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