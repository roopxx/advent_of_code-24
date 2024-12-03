import re

# Function to sum all the mul() values after multiplication
def multiplyUncorruptedData(data):
    return sum(x * y for x, y in data)

# Memory of uncorrupted data
uncorruptedMemory = []

with open("day_03/input.txt", 'r') as file:
    for line in file:
        # Regex to find all the mul() func digits occurrences
        values = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        uncorruptedMemory.extend((int(x), int(y)) for x, y in values) # type converstion

print(f"The total sum of uncorrupted memory: {multiplyUncorruptedData(uncorruptedMemory)}")
