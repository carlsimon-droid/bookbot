from stats import get_num_words, get_num_sym, sorted_sym
import sys

def get_book_text(filepath):
    with open(filepath) as f:
            file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sym_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for syms in sym_sorted_list:
        if not syms["sym"].isalpha():
            continue
        print(f"{syms['sym']}: {syms['num']}")
    print("============= END ===============")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    symbol_count = get_num_sym(text)
    sym_sorted_list = sorted_sym(symbol_count)
    print_report(book_path, word_count, sym_sorted_list)

main()