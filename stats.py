def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}

    for char in text:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1

    return characters

def sort_chars_on(letter):
    return letter["num"]

def sort_chars(characters):
    letters = []
    for char in characters:
        if char.isalpha():
            letters.append({"char":char, "num": characters[char]})
    
    letters.sort(reverse=True, key=sort_chars_on)
    
    return letters