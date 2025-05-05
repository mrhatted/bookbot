def get_number_of_words(book_text):
    amount_of_words = len(book_text.split())
    return amount_of_words

def get_number_of_characters(book_text):
    lower_case_book_text = book_text.lower()
    result = dict()
    for letter in lower_case_book_text:
        if letter in result and letter.isalpha():
            result[letter] += 1
        if letter not in result and letter.isalpha():
            result[letter] = 1
    return result
    

def sort_on(dict):
    return dict["num"]

def sort_the_dict(resulting_dict):
    chars_list = []
    for char, count in resulting_dict.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
