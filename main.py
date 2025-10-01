from stats import count_words, get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"""Found {num_words} total words""") 
    print(get_character_count(text))

main()
