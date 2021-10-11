import random
import time

Array = []

for i in range(1000000):
    Array.append(i)

random.shuffle(Array)

# print(Array)


start_time = time.time()


def non_brainy(array):
    for entry in array:
        if entry % 2 != 0:
            if entry == 69:
                return


def basic(array):
    for entry in array:
        if entry == 69:
            return


def k_bro(array):
    for entry in array[:(len(array) // 2)]:
        if entry == 69:
            return

    for entry in reversed(array[(len(array) // 2):]):
        if entry == 69:
            return


# basic(Array)
basic(Array)
print("--- %s seconds ---" % (time.time() - start_time))
