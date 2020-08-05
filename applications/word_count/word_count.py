def word_count(s):
    # Your code here
#input string
#ignore certain characters
#count how many times word occurs
#build a dictionary
#if its already in there increment count by 1

    words = s.lower()

    #convert whitespace characters to a space
    char_conv = '\n \t \r'.split(" ")

    for whitespace in char_conv:
        words = words.replace(whitespace, " ")

    #remove ignored characters & split
    ignore_char = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for c in ignore_char:
        words = words.replace(c, "")

    #convert string to array of words
    words = words.split(" ")

    words_dict = dict()
    #skip over any empty strings
    for word in words:
        if word == "":
            continue
        #count occurances of word
        if word in words_dict:
            # there's another one or more
            words_dict[word] +=1
            
        else:# its the only one of its kind
            words_dict[word] = 1

    return words_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))