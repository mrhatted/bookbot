import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
    
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_the_dict
from printgoodlayout import printgoodlayout

def main():
    #print (f"{get_number_of_words(get_book_text(sys.argv[1]))} words found in the document")
    #print (f"{get_number_of_characters(get_book_text(sys.argv[1]))}")
    #print (sort_the_dict(get_number_of_characters(get_book_text(sys.argv[1]))))
    printgoodlayout(sys.argv[1],get_number_of_words(get_book_text(sys.argv[1])),sort_the_dict(get_number_of_characters(get_book_text(sys.argv[1]))))    

main()