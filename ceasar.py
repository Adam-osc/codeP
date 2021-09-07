
new_mes = ""
deciBool = False
shift = 0
chrapNum = 0

while deciBool == False:
    
    deci = input("Enter 'e' or 'd' if you want to encode or decode, respectively:")

    print(deci)
    if deci.lower() == "e" or deci.lower() == "d":
        deciBool = True

deciBool = False

while deciBool == False:
    try:
        shift = int(input("Enter the shift:"))
        deciBool = True

    except:
        print("The fuck.")
        deciBool = False

if deci.lower() == "e":

    emessage = input("Your message to encrypt:")

    for chrap in emessage:
        chrapNum = ord(chrap)
        chrapNum += shift

        print(chr(chrapNum))
        new_mes = new_mes + chr(chrapNum)

if deci.lower() == "d":

    dmessage = input("Your message to dencrypt:")

    for chrap in dmessage:
        chrapNum = ord(chrap)
        chrapNum -= shift

        print(chr(chrapNum))
        new_mes = new_mes + chr(chrapNum)

print(new_mes)
        