def is_palindrome(s):
    copy = ""
    i = len(s) - 1
    while i >= 0:
        copy = copy + s[i]
        i = i - 1
    #print(copy)

    if copy == s:
        return True
    else:
        return False    
pass

# Testy:
print(is_palindrome("anna")) # True
print(is_palindrome("prst")) # False
print(is_palindrome("oko")) # True
print(is_palindrome("oka")) # False