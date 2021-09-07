def lists(a, b, c, d):
    z1= []
    z2 = []
    z3 = []

    i = 0
    j = 0

    while i <= a:
        z1.append(i)
        i = i + 1

    while j < len(z1):
        z2.append(z1[j]+10)
        j = j + 1

    z2[len(z2)-1] = "KSI"

    if b in z2:
        z2.remove(b)
    
    else:
        print("Not here")

    if c > len(z1):
        z3 = z1
    
    else:
       z3 = z3 + z1[0:c]
       z2 = z2 + z3

    z3.reverse()

    z1[1] = d
    z1.sort()

    return(z1, z2, z3)
    pass

print(lists(5, 12, 3, 20))

def lists2(a, b, c, d):
    first_list = [x for x in range(0, a + 1)]
    second_list = []
    for prvok in first_list:
        second_list.append(prvok + 10)
    second_list[-1] = 'KSI'
    if b in second_list:
        second_list.remove(b)
    else:
        print("Not here")
    third_list = first_list[:c]
    second_list.extend(third_list)
    third_list.reverse()
    first_list[1] = d
    first_list.sort()
    return (first_list, second_list, third_list)


print(lists2(5, 12, 3, 20))
print(lists2(10, 3, 2, 11))
print(lists2(3, 15, 3, 3))
print(lists2(15, 25, 2, 2))