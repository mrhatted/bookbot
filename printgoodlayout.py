def printgoodlayout(path, word_count, character_count):
    print (f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for char in character_count:
        print(f"{char["char"]}: {char["num"]}")
    print ("============= END ===============")