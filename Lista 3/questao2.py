def clean_word(function):
    def cleanword():
        a = ""
        for caractere in function():
           if caractere.isalpha():
             a += caractere
        return a
    return cleanword

@clean_word
def word():
    return 'w@h#o??'


word = word()
print(word)