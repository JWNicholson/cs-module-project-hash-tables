import random

#Read the input file and split into words

#Analyze the text to build up the dataset
## Which wirds can follow a word - andy that actually does
## any word at index + 1
## How to build a dataset?

###Use a hashtable
## #relate on piece of info with other info
### Requent lookups
### key:word, value: list of all words that follow this word


#Choose a random "start word" to begin (Starts with capitol letter or quotation mark)
## First or second character is capitalized

## Make a list of start words

#Loop over, choose a random following word. If its a stop word
##Stop word - ends with a period, question mark, ..., etc

###Use a hash table

# Read in all the words in one go
with open("/mnt/h/CS32/Hashtables/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

# # TODO: analyze which words can follow other words
# # Your code here

#split words on spaces
words = words.split()
# Keep track of all the words that can follow a word
following_words = {}  

prev = None

for w in words:
    if prev is not None:

        # Make an empty list for the first entries
        if prev not in following_words:
            following_words[prev] = []

        # Add word to the list of those that are following_words
        following_words[prev].append(w)

    prev = w

# #Make a list of start words
# Check if word starts with a capital letter
is_start = lambda x: x[0].isupper() or len(x) > 1 and x[1].isupper()
start_words = [w for w in following_words.keys() if is_start(w)]

# # TODO: construct 5 random sentences
# # Your code here
# Print 5 of paragraphs
for _ in range(5):

    # Choose the starting word
    w = random.choice(start_words)

    stopped = False
    stop_sign = ".!?"  # Stop on any of these punctuation marks

    while not stopped:
        print(w, end=" ")
        # condition of ? at end of sentence or someting like !" or any word longer than 1 element
        if w[-1] in stop_sign or len(w) > 1 and w[-2] in stop_sign:
            stopped = True
        else:
            # Follow to the next word in the chain
            next_words = following_words[w]
            w = random.choice(next_words)

    print("\n")