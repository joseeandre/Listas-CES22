def is_palindrome(str):
    str_reverse = str[len(str)::-1]

    if str == str_reverse:
        return True
    else:
        return False


print(is_palindrome("reviver"))
