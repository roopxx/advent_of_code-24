import re

# Function to sum all the mul() values after multiplication
def multiplyUncorruptedData(data):
    return sum(x * y for x, y in data)

# Memory of uncorrupted data
uncorruptedMemory = []
# Flag to multiply or not based on do() or don't()
mul_enabled = True

with open("day_03/input.txt", 'r') as file:
    for line in file:
        # Regex to find mul(), do() or don't()
        instructionsList = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', line)
        for instruction in instructionsList:
            # If do(), flag set to true to store
            if instruction == "do()":
                mul_enabled = True
            # If don't(), flag set to false to discard
            elif instruction == "don't()":
                mul_enabled = False
            # Based on flag the data is stored in the array - uncorruptedMemory
            elif mul_enabled:
                [(x, y)] = re.findall(r'mul\((\d+),(\d+)\)', instruction) # type converstion
                uncorruptedMemory.append((int(x), int(y)))

print(f"The sum after applying the conditions: {multiplyUncorruptedData(uncorruptedMemory)}")
