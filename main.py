import sys
from stats import word_count
from stats import unique_char

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")   
        sys.exit(1)
    book = sys.argv[1]
    # print(book)
    contents = get_book_text(book)
    count = word_count(contents)    
    # print(f"{count} words found in the document")
    ud = unique_char(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("----------- Character Count ----------")
    for entry in ud:        
        print(f"{entry}: {ud[entry]}")
    print("============= END ===============")    