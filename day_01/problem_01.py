def totalDistance(left, right):
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total

leftList = []
rightList = []

with open("day_01/input.txt", 'r') as file:
    for line in file:
        values = line.split()
        leftList.append(int(values[0]))
        rightList.append(int(values[1]))

leftArr = sorted(leftList)
rightArr = sorted(rightList)

total_distance = totalDistance(leftArr, rightArr)

print(f"Total distance between two lists: {total_distance}")
