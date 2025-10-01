from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"""Found {num_words} total words""") 

main()
