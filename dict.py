libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]

#Creating dictionary from a list and sorting it
def sort(e):
    return e['read']

libraryForSort = []

librarySrt = []


for student in libraryRecord:
    libraryForSort.append({'name': (student[1] + " " + student[2]), 'read': student[3]})

for num, student in enumerate(libraryForSort):
    student.update({'id': libraryRecord[num][0]})

librarySrt = sorted(libraryForSort, key=lambda e: e['read'], reverse=True)

def dictprint(dlist1):
    
    for student in dlist1:
        library_str = str(student).strip("{}").replace("'", " ")
        print(library_str + ";\n")

dictprint(librarySrt)

print(librarySrt[1]['read'])

print(libraryForSort)
print("\n")
print(librarySrt)