# Tuto funkci implementuj.
def penguins_in_group(total: int, group_size: int) -> int:

    if group_size == 0:
        return 0

    print(total)

    if total == 0 or total < group_size:
        return 0

    for i in range(group_size):
        total -= 1

    return penguins_in_group(total, group_size) + 1

# Testy:
print("Máme 20 tučniakov, potrebujeme 5 tímov, v jednom tíme bude musieť byť ",penguins_in_group(20, 5))  # 4
print(penguins_in_group(392, 3))  #98
