import sys
from stats import get_number_words, get_char_count, sort_char_dict


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

pathfile = sys.argv[1]


def get_book_text(pathfile):
    with open(pathfile) as b:
        book_content = b.read()
    return book_content


def main(pathfile):
    book = get_book_text(pathfile)
    print(book)


main(pathfile)
book = get_book_text(pathfile)

word_count = get_number_words(book)

words = get_char_count(book)

sorted_dict = sort_char_dict(book)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {pathfile}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char in sorted_dict:
    print(f"{char["char"]}: {char["num"]}")
print("============= END ===============")
