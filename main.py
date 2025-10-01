import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)

    print("============ BOOKBOT ============")
    print(f"""Analyzing book found at {filepath}...""")

    print("----------- Word Count ----------")
    print(f"""Found {num_words} total words""") 

    print("--------- Character Count -------")
    charcter_count_dict = get_character_count(text)
    sorted_list = get_sorted_list(charcter_count_dict)
    
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"""{dict["char"]}: {dict["num"]}""")
    
    print("============= END ===============")

main()