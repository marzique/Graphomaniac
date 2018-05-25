import re

def unicounter(note):
    '''Function returns number of unique words in string'''


    # dict to store pairs {"word": frequency)
    unique_words = {}
    counter = 0
    s = 0

    '''fixing bug with spaces in the beginning of the string'''

    # count spaces before
    for letter in note:
        if letter == " ":
            s += 1
        else:
            break

    # new string from first letter
    note = note[s:]

    # check
    # print(note)

    # divide string to list of words
    note = re.split('\W+', note)

    #write down data to dict
    for word in note:
        if word.lower() in unique_words:
            old_quantity = int(unique_words[word.lower()])
            unique_words[word.lower()] = str(old_quantity + 1)
            print("word exists (incremented quantity)")
        else:
            unique_words[str(word.lower())] = str(1)
            print("word added")

    #calc unique words
    for pair in unique_words:
        if unique_words[pair] == str(1):

            #check for empty string (re.split() issue)
            if not pair:
                break

            counter += 1

    return counter

# test
# print(unicounter("     viktor maksimych ne normalniy mujik a viktor yanukovich normalniy mujik ne"))










