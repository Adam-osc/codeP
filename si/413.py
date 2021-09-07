# Tuto funkci implementuj. Smaz prikaz 'pass' a pis telo funkce.
def word_frequency(text_nas):
    points = {}
    word = ""

    text_nas = text_nas.lower()
    for char in text_nas:
        if char.isalpha() == True:
            word = word + char
        else:
            if word != "":
                if word not in points:
                    points[word] = 1
                    word = ""
                else:    
                    points[word] += 1
                    word = ""  
    
    if word != "":
        if word not in points:
            points[word] = 1
            word = ""
        else:    
            points[word] += 1
            word = ""

    return points

# testy (upravujte dle libosti)
print(word_frequency("Ksi, Ksa, Ksi, Kse"))       # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Ksi,+Ksa,Ksi;;-;Kse_"))     # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Informatika je chobotina"))  # {'informatika': 1, 'je': 1, 'nejlepsi': 1}
