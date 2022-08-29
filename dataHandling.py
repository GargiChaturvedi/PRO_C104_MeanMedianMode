import csv
from collections import Counter

with open("SOCR-HeightWeight.csv") as f:
    df = csv.reader(f)
    dfList = list(df)
dfList.pop(0)

weights = []

for i in range(len(dfList)):
    data = dfList[i][2]
    weights.append(data)

sum = 0

for i in weights:
    sum += float(i)

mean = sum/len(weights)

median = 0
length = len(weights)

if(length % 2 == 0):
    median1 = float(weights[length//2])
    median2 = float(weights[length//2 + 1])
    median = (median1 + median2)/2
else:
    median = weights[length//2 + 1]

mode = Counter(weights).most_common(1)[0][0]

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))