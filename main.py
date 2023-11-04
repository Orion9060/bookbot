def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    print(book)

def get_book(path):
    with open(path) as f:
        return f.read()

main()