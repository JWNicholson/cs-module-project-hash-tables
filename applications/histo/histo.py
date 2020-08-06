# Your code here
#https://docs.python.org/3/howto/sorting.html
#https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/
#https://docs.python.org/3/library/operator.html

from operator import itemgetter


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

#make the histogram
def make_histogram(file_path):
#open and read the file
    with open(file_path) as file:
        text = file.read()


#     #create a dictionary from word_count, storing occurances of words
    freq = word_count(text)

#     #convert dictionary to a list and sort number of occurances in  descending order
    freq_list = freq.items()
    freq_list = sorted(freq_list, key=itemgetter(1, 0), reverse=True)

#     #find the longest word
    longest_word = len(freq_list[0][0])

    for word_data in freq_list:
        if len(word_data[0]) > longest_word:
            longest_word = len(word_data[0])

#     #return words and occurances, with one # from each occurance
    for word_data in freq_list:
        format_word = word_data[0] + (longest_word - len(word_data[0])) * " "
        histogram_bar = "#" * word_data[1]

        histogram_row = format_word + "  " + histogram_bar

        print(histogram_row)

make_histogram("robin.txt")


