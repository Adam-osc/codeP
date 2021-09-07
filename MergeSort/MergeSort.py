

def printArray(array):
    for x in range(len(array)):
        print(str(array[x]))

def mergeSort(array):

    if len(array) <= 1:
        return array

    else:
        midpoint = len(array) / 2
        left = []
        right = []

        if len(array) % 2 == 0:
            lSize = len(array) / 2
            rSize = lSize
        
        else:
            lSize = len(array) // 2
            rSize = len(array) - lSize

        for i in range(int(lSize)):
            left.append(array[int(i)]) 

        for j in range(int(rSize)):
            right.append(array[int(j+lSize)])

        left = mergeSort(left)
        right = mergeSort(right)

        result = merge(left, right)
        print(result)

        return result

def merge(left, right):


    global result

    leftPoint = rightPoint = 0

    while leftPoint < len(left) or rightPoint < len(right):

        if leftPoint < len(left) and rightPoint < len(right):

            if(left[leftPoint] < right[rightPoint]):

                result.append(left[leftPoint])

                global resultPoint
                resultPoint += 1
                leftPoint += 1
            
            else:

                result.append(right[rightPoint]) 

                resultPoint += 1
                rightPoint += 1

        elif leftPoint < len(left):

            result.append(left[leftPoint])

            resultPoint += 1
            leftPoint += 1

        elif rightPoint < len(right):

            result.append(right[rightPoint])

            resultPoint += 1
            rightPoint += 1
        
        return result

array = [5, 4, 3, 2, 1]

global result
result = []
global resultPoint
resultPoint = 0


array = mergeSort(array)[:]

print(array)