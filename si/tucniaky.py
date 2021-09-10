# Tuto funkci implementuj.
import random

def penguins_in_group(total: int, group_size: int) -> int:

    #if type(total) is not int or type(group_size) is not int:
        #return 0

    if group_size == 0 or group_size < 0:
        return 0

    #print(total)

    if total == 0 or total < group_size:
        return 0

    total -= group_size

    return penguins_in_group(total, group_size) + 1

# Testy:
print("Number of penguins: " + str(penguins_in_group(10, -1)))
print("Number of penguins: " + str(penguins_in_group(54.3, 14.2)))
for j in range(10):
    n1 = random.randint(0, 999)
    n2 = random.randint(0, 999)

    print("[.]n1 = " + str(n1))
    print("[.]n2 = " + str(n2))

    try:
        if penguins_in_group(n1, n2) == n1 // n2:
            print("Number of penguins: " + str(penguins_in_group(n1, n2)))
            print("Working")
        else:
            print("[.] Not Working")
            print("Number of penguins: " + str(penguins_in_group(n1, n2)))
            print("n1 = " + str(n1))
            print("n2 = " + str(n2))
    except Exception as e:
        print(e)


for j in range(10):
    n1 = random.randint(12, 999)
    n2 = random.randint(0, 12)

    print("[.]n1 = " + str(n1))
    print("[.]n2 = " + str(n2))

    try:
        if penguins_in_group(n1, n2) == n1 // n2:
            print("Number of penguins: " + str(penguins_in_group(n1, n2)))
            print("Working")
        else:
            print("[.] Not Working")
            print("Number of penguins: " + str(penguins_in_group(n1, n2)))
            print("n1 = " + str(n1))
            print("n2 = " + str(n2))
    except Exception as e:
        print(e)

#print("Máme 20 tučniakov, potrebujeme 5 tímov, v jednom tíme bude musieť byť ",penguins_in_group(n1, n2))  # 4

