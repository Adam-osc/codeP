def my_abacus(base: int, exp: int) -> int:

    if exp == 1:
        return base
    
    store = 0
    addon = my_abacus(base, (exp-1))

    for i in range(base):
        store += addon
    
    return store

# Testy:
print(my_abacus(10, 10))  # 1000
print(my_abacus(34, 3))  # 39 304
print(my_abacus(8, 5))  # 32 768
print(my_abacus(2, 10))  # 1024