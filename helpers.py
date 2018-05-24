def unicounter(note):

    # dict top store pairs {"word": frequency)
    unique_words = {}
    counter = 0

    # devide string to list of words
    note = note.split()

    #write down data to dict
    for word in note:
        if word.lower() in unique_words:
            old_quantity = int(unique_words[word.lower()])
            unique_words[word.lower()] = str(old_quantity + 1) //
            print("word exists")
        else:
            unique_words[str(word.lower())] = str(1)
            print("word added")

    #calc unique words
    for pair in unique_words:
        if unique_words[pair] == str(1):
            counter += 1
    return counter

print(unicounter("simple string with simple words"))






