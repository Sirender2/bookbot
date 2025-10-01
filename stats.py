def count_words(text):
    return len(text.split())

def get_character_count (text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
    
#text = "Abcdefg hijklmnop aBCdefg abcde"
#print(get_character_count(text))