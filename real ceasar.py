alpha = ["a", "b", "c", "d","e","f", "g", "h", "i", "j", "k" ,"l", "m", "n", "o", "p", "q", "r", "s", "t", "u" , "v", "w", "x", "y", "z"]
getS = input("Prease enter")
shift = int(input("Prease shift"))
thisCar = ""
thisPos = int

finalMsg = ""

for c in getS:
    thisCar = c.lower()
    thisPos = alpha.index(thisCar)

    for a in range(thisPos, thisPos+shift):

        thisPos += 1

        if thisPos > (len(alpha) -1):
            thisPos = 0

    finalMsg = finalMsg + alpha[thisPos]

print(finalMsg)