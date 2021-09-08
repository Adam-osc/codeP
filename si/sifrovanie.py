def encode(n: int, plain_text: str) -> str:  # vraci ciphertext typu String
    pocet = len(plain_text) // n
    #print("Pocet je: " + str(pocet))
    l_velk = len(plain_text) % n

    cast = ""
    casti = []

    encdd = ""

    idx = 0
    while idx <= pocet - 1:
        for i in range((0 + (idx * n)), ((idx * n) + n)):
            #print("toto je i: " + str(i))
            cast += plain_text[i]

        casti.append(cast)
        cast = ""
        idx += 1

    if l_velk != 0:
        for i in range((pocet * n), ((pocet * n) + l_velk)):
            cast += plain_text[i]

    casti.append(cast)

    #print(casti)

    for j, pole in enumerate(casti):

        casti[j] = pole[::-1]
        encdd += casti[j]
        j += 1

    #print("Encodnute: " + encdd)
    return encdd


def decode(n: int, cipher_text: str) -> str:  # vraci plaintext typu String
    pocet = len(cipher_text) // n
    #print("Pocet je: " + str(pocet))
    l_velk = len(cipher_text) % n

    cast = ""
    casti = []

    decdd = ""

    idx = 0
    while idx <= pocet - 1:
        for i in range((0 + (idx * n)), ((idx * n) + n)):
            #print("toto je i: " + str(i))
            cast += cipher_text[i]

        casti.append(cast)
        cast = ""
        idx += 1

    if l_velk != 0:
        for i in range((pocet * n), ((pocet * n) + l_velk)):
            cast += cipher_text[i]

    casti.append(cast)

    #print(casti)

    for j, pole in enumerate(casti):
        casti[j] = pole[::-1]
        decdd += casti[j]
        j += 1

    #print("Decodnute: " + decdd)
    return decdd


print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane")))

# na automaticke testy doporucuji assert