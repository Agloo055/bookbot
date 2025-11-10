from stats import count_words, count_characters, sort_chars

def get_book_text(filepath):
    file_contents = filepath.read()

    return file_contents

def main():
    with open ("books/frankenstein.txt") as f:
        text = get_book_text(f)
        num_words = count_words(text)
        num_chars = count_characters(text)
        sorted_letters = sort_chars(num_chars)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for letter in sorted_letters:
            print(f"{letter["char"]}: {letter["num"]}")
        print("============= END ===============")
    

main()