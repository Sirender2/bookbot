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

def sort_on(items):
    return items["num"]

def get_sorted_list(dict) :
    dict_list = []
    for char, num in dict.items():
        dict_char = {"char" : char, "num": num}
        dict_list.append(dict_char)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


# text = "FFFFFF Abcdefg hijklmnop aBCdefg abcde"
# print(get_sorted_list(get_character_count(text)))