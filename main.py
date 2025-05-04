import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_contents = get_book_text(sys.argv[1])
    ### book_name = sys.argv[1].removeprefix("books/")
    word_count = get_word_count(file_contents)
    character_dictionary = get_character_count(file_contents)
    sorted_dictionary = sort_dictionary(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character in sorted_dictionary:
        print(f"{character['char']}: {character['num']}")
    
    print("============= END ===============")

main()    