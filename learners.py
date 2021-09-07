import os

print(os.getcwd())

rawData = []
file = open("Learners+", "r")

for record in file:
    rawData.append(record.strip())

examResults = []

for item in rawData:
    nextLearner = item.split(",")
    examResults.append(nextLearner)

studentTotal = 0
subjectTotal = 0

for learner in examResults:
    for j in range(1, int(len(learner))):
        subjectTotal += int(learner[j])

print(j)
studentTotal = subjectTotal / j
subjectAverage = studentTotal / len(examResults)

print(rawData)
print(examResults)
print(studentTotal)
print(subjectAverage)
