import sys

def get_book_text(filename):
    """
    Reads the text of a book from a file and returns it.
    """
    with open(filename) as f:
        book_text = f.read()
    return book_text

def number_of_words(book_text):
    """Counts the number of words in the book text.
    """
    words = book_text.split()
    return len(words)

def number_of_characters(book_text):
    book_text = book_text.lower()
    char_counts = {}
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted_characters(char_counts):
    """
    Returns a sorted list of characters in the book text.
    """
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python stats.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    book_text = get_book_text(filename)
    print(f"Number of words: {number_of_words(book_text)}")
    char_counts = number_of_characters(book_text)
    print("Character counts (sorted):")
    for char, count in sorted_characters(char_counts):
        print(f"{repr(char)}: {count}")
    