def pig_latin1(word):
    word = word.lower()
    vowels = "aeoui"
    consonants = 'qwrtypsdfghjklzxcvbnm'
    first_vowel = ""
    for letter in word:
        if letter in vowels:
            first_vowel = letter
            break
        
    index_of_first_word = word.find(first_vowel)
    letters_before_first_vowel = word[:index_of_first_word]
    
    if word[0] in consonants:
        return word[index_of_first_word:] + word[:index_of_first_word] + "ay"
    else:
        return word + "way"
    
print(pig_latin1("eniel"))
    
       
    
    
        