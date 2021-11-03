import re

print("\n")
print("When prompted to enter a logic sentence, you should use capital variable\n")
print("The max amount of variables was not tested\n")
print("Allowed operators are 'and', 'not', 'or', 'xor'\n")

n_inputs = int(input("Enter number of inputs: "))
statement = input("Enter a logic statement: ")

bracket_pos = []
sub_brackets = []
truth_table = []
variables = []

# ((A and B) or C)
# i, j, k, idx, pos, ent, char_pos, n, times
for i in range(len(statement)):
    if statement[i] == ")":
        t_end = i

        j = t_end - 1
        a_bracket = False

        while j != -1:
            if (statement[j] == "(") and (a_bracket == False):
                bracket_pos.append([j, t_end])
                j = -1

            elif statement[j] == ")":
                a_bracket = True
                j -= 1

            elif (statement[j] == "(") and (a_bracket == True):
                a_bracket = False
                j -= 1

            else:
                j -= 1
            
            print(statement[j+1] + " " + str(j+1) + " " + str(a_bracket))

#print(bracket_pos)

for pos in bracket_pos:
    sub_brackets.append(statement[pos[0]+1:pos[1]])

#print(sub_brackets)

for idx,char in enumerate(statement.lower()):
    try:
        if char.isalpha():
            if (not statement[idx + 1].isalpha()) and ((not statement[idx -1].isalpha()) or (statement[idx - 1] == statement[len(statement) - 1])):
                variables.append([char, idx]) 
    except IndexError:
        if char.isalpha() and ((idx - 1) < 0) and (not statement[idx + 1].isalpha()):
            variables.append([char, idx])
        elif char.isalpha() and ((idx + 1) > (len(statement) - 1)) and (not statement[idx - 1].isalpha()):
            variables.append([char, idx])

for k in range(2 ** n_inputs):
    t_bin = bin(k)
    t_bin = t_bin[2:]
    if len(t_bin) != n_inputs:
        t_bin = ("0" * (n_inputs - len(t_bin))) + t_bin
    truth_table.append([t_bin])

print(truth_table)

variables = sorted(variables, key=lambda x:x[0])
print(variables)

for ent_1 in truth_table:
    n = 0
    times = 0

    for char_pos in variables:
        if times != 0:
            # print(ent_1, char_pos, temp_char, times)
            if temp_char != char_pos[0]:
                n +=1

        temp_char = char_pos[0]

        temp_state = statement

        # print(ent_1[0][n])
        statement = temp_state[:char_pos[1]] + str((int(ent_1[0][n]))) + temp_state[char_pos[1] + 1 :]

        times += 1
    
    xor_state = statement

    if "xor" in statement:
        xor_state = re.sub("xor", "^", xor_state)

    print(xor_state)
    print(eval(xor_state.lower()))

#for ent in truth_table:
#    a = bool(int(ent[0][0]))
#    b = bool(int(ent[0][1]))
#    print(eval(statement.lower()))
