easy = "23456,West Kirby,04/11/15"
jednarada = ""
counter = 0

for char in easy:

    if char == ",":
        print(" ")
        print(jednarada)
        jednarada = ""
        counter +=1

    else:
        jednarada = (jednarada + char)
        counter +=1

    if counter == len(easy):
        print(" ")
        print(jednarada)