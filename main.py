import sys 


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


def get_book_text(filepath):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

#Moved to stats.py
#def word_count(text):
#    words = text.split()
#    return len(words)

from stats import word_count
from stats import character_count
from stats import sort_output

def main():
    contents = get_book_text(book_path)
    num_words = word_count(contents)
    characters = character_count(contents)
    sorted = sort_output(characters)
    print(f"Found {num_words} total words")
    #print(characters)
    #print(sorted)

    for characters in sorted:
       char = characters["char"]
       count = characters["count"]

       if char.isalpha():
           print(f"{char}: {count}")
       else:
           pass


main()