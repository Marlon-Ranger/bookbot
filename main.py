import sys
from stats import count_words,count_characters,sort_characters

def get_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   book_path = sys.argv[1]
   print(book_path)
   book_text = get_text(book_path)
   book_words = count_words(book_text)

   header = "============ BOOKBOT ============"
   found_book_under = f"Analyzing book found at {book_path}..."
   word_count = "----------- Word Count ----------"
   found_words = f"Found {book_words} total words"
   character_count = "--------- Character Count -------"
   footer = "============= END ==============="

   print(header + "\n" + found_book_under + "\n" + word_count + "\n" + found_words + "\n" + character_count)
   
   book_char_list = sort_characters(count_characters(book_text))
    
   for item in book_char_list:
       if item["char"].isalpha():
           print(f"{item["char"]}: {item["num"]}")
   
   print(footer)

main()
