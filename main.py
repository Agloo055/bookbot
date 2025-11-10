from stats import count_words, count_characters, sort_chars
import sys

def get_book_text(filepath):
    file_contents = filepath.read()

    return file_contents

def main():
    if len(sys.argv) == 2:    
        with open (sys.argv[1]) as f:
            text = get_book_text(f)
            num_words = count_words(text)
            num_chars = count_characters(text)
            sorted_letters = sort_chars(num_chars)

            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {sys.argv[1]}...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")
            for letter in sorted_letters:
                print(f"{letter["char"]}: {letter["num"]}")
            print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()