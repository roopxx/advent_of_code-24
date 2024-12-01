from collections import Counter

leftList = []
rightList = []

with open("day_01/input.txt", 'r') as file:
    for line in file:
        val = line.split()
        leftList.append(int(val[0]))
        rightList.append(int(val[1]))

rightListCounter = Counter(leftList)

def totalSimilarityScore(left, rightListCounter):
    totalSimilarity = 0
    for num in left:
        occurence = rightListCounter.get(num, 0)
        num_similarity = occurence * num
        totalSimilarity += num_similarity
    return totalSimilarity

rightArr = sorted(leftList)
leftArr = sorted(rightList)

score = totalSimilarityScore(leftArr, rightListCounter)

print(f"Total similrity score: {score}")
