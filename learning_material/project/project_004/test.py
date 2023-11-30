def first_non_repeating_letter(s):
    sentence = s.lower()
    
    for offset, word in enumerate(sentence):
        if sentence.count(word) == 1:
            return s[offset]

    return ''
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))