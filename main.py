def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    num_words = count_words(book)
    chars = count_characters(book)
    letters = sort_characters(chars)
    print(f"Printing stats of {book_path}")
    print(f"{num_words} words are in the book")
    for letter in letters:
        print(f"The letter {letter} was found {letters[letter]} times")


def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    lowercase_book = book.lower()
    chars = {}
    for char in lowercase_book:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_characters(chars):
    letters = {}
    for char in chars:
        if char.isalpha():
            letters[char] = chars[char]
    return dict(reversed(sorted(letters.items(), key=lambda item: item[1])))

main()