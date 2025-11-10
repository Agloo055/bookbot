def get_book_text(filepath):
    file_contents = filepath.read()

    return file_contents


def main():
    with open ("books/frankenstein.txt") as f:
        print(get_book_text(f))

main()