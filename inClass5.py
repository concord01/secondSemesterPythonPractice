# learning about dictionaries
students = {
    "Bowie": "F",
    "Kalp": "F",
    "Jacob": "D",
    "Jonathan": "A",
    "Kaleb": "B+"
}

# adding and changing values in a dictionary
students["Jacob"] = "F"
students["Ian"] = "A-"
print(students)

# Looping through a dictionary
del students["Jacob"]

numF = 0
for key in students:
    print(key)
    if (students[key] == "F"):
        numF +=1

print(numF)