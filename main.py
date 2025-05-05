def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_the_dict
from printgoodlayout import printgoodlayout

def main():
    #print (f"{get_number_of_words(get_book_text("books/frankenstein.txt"))} words found in the document")
    #print (f"{get_number_of_characters(get_book_text("books/frankenstein.txt"))}")
    #print (sort_the_dict(get_number_of_characters(get_book_text("books/frankenstein.txt"))))
    printgoodlayout("/books/frankenstein.txt",get_number_of_words(get_book_text("books/frankenstein.txt")),sort_the_dict(get_number_of_characters(get_book_text("books/frankenstein.txt"))))

main()