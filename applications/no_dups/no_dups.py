def no_dups(s):
    # Your code here
    #split into a list on whitespaces
    words = s.split(" ")

    words_dict = dict()
    dups_removed = []

    for word in words:
        # check if its already in there
        if word not in words_dict:
            # Its not --
            words_dict[word] = 1
            dups_removed.append(word)
            
    # put all items into one string
    return " ".join(dups_removed)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))