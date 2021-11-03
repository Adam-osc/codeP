# ((A and B) or C)

# for i in range(len(statement)):
#     if statement[i] == ")":
#         t_end = i

#         j = t_end - 1
#         a_bracket = False

#         while j != -1:
#             if (statement[j] == "(") and (a_bracket == False):
#                 bracket_pos.append([j, t_end])
#                 j = -1

#             elif statement[j] == ")":
#                 a_bracket = True
#                 j -= 1

#             elif (statement[j] == "(") and (a_bracket == True):
#                 a_bracket = False
#                 j -= 1

#             else:
#                 j -= 1

#             print(statement[j+1] + " " + str(j+1) + " " + str(a_bracket))

# print(bracket_pos)

# for pos in bracket_pos:
#     sub_brackets.append(statement[pos[0]+1:pos[1]])

# print(sub_brackets)

# for ent in truth_table:
#    a = bool(int(ent[0][0]))
#    b = bool(int(ent[0][1]))
#    print(eval(statement.lower()))

