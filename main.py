from stats import word_count, char_count, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")

    wc = word_count(get_book_text(book))
    print(f"Found {wc} total words")

    print("--------- Character Count -------")
    cc = char_count(get_book_text(book))
    sorted_cc = sort_on(cc)
    for dic in sorted_cc:
        print(f"{dic['name']}: {dic['count']}")
    
    print("============= END ===============")