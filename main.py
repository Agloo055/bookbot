from stats import count_words, count_characters

def get_book_text(filepath):
    file_contents = filepath.read()

    return file_contents

def main():
    with open ("books/frankenstein.txt") as f:
        text = get_book_text(f)
        num_words = count_words(text)
        num_chars = count_characters(text)

        print(num_chars)

    #    print(f'Found {num_words} total words')
    

main()