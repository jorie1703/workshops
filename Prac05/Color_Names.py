__author__ = 'jc226070'

"""
CP1404/CP5632 Practical
Color names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"AliceBlue": "f0f8ff", "AntiqueWhite": "faebd7", "AntiqueWhite1": "ffefdb", "AntiqueWhite2": "eedfcc",
               "Antiquewhite3": "cdc0b0", "Antiquewhite4": "8b8378", "Aquamarine1": "7fffd4"}
# print(COLOR_NAMES)

color = input("Enter color name: ")
for key in COLOR_NAMES:
    print(key, 'is', COLOR_NAMES[key])
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color name")
    color = input("Enter color name: ")


# print('{} is {}' .format(key,COLOR_NAMES[key]))
