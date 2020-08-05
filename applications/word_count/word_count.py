def word_count(s):
    # Your code here
#input string
#ignore certain characters
#count how many times word occurs
#build a dictionary
#if its already in there increment count by 1

    #split() s on spaces
    inputStr = s.split("")
    ignore_char = set(['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'])
print(s)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))