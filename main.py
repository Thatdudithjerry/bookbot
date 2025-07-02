import sys
from stats import number_of_words
from stats import number_of_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    num_words = number_of_words(book_path)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = number_of_characters(book_path)
    for char, count in char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()
