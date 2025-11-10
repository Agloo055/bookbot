from stats import count_words

def get_book_text(filepath):
    file_contents = filepath.read()

    return file_contents

def main():
    with open ("books/frankenstein.txt") as f:
       text = get_book_text(f)
       num_words = count_words(text)

       print(f'Found {num_words} total words')

main()