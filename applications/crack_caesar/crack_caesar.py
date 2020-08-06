def decode_cipher(encrypted_file):

    # store known frequencies 
    known_frequencies = dict()

    known_frequencies["E"] = 11.53
    known_frequencies["T"] = 9.75
    known_frequencies["A"] = 8.46
    known_frequencies["O"] = 8.08
    known_frequencies["H"] = 7.71
    known_frequencies["N"] = 6.73
    known_frequencies["R"] = 6.29
    known_frequencies["I"] = 5.84
    known_frequencies["S"] = 5.56
    known_frequencies["D"] = 4.74
    known_frequencies["L"] = 3.92
    known_frequencies["W"] = 3.08
    known_frequencies["U"] = 2.59
    known_frequencies["G"] = 2.48
    known_frequencies["F"] = 2.42
    known_frequencies["B"] = 2.19
    known_frequencies["M"] = 2.18
    known_frequencies["Y"] = 2.02
    known_frequencies["C"] = 1.58
    known_frequencies["P"] = 1.08
    known_frequencies["K"] = 0.84
    known_frequencies["V"] = 0.59
    known_frequencies["Q"] = 0.17
    known_frequencies["J"] = 0.07
    known_frequencies["X"] = 0.07
    known_frequencies["Z"] = 0.03

# cdictionary to store letter count
    letter_count = dict()
    #characters to compare to 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #dictionary to store frequency of letters
    letter_frequency = dict()

    for letter in alphabet:
        letter_count[letter] = 0
        letter_frequency[letter] = 0
    
    # store the total number of letters to calculate percentages later
    total_letters = 0

    # store file contents into a variable
    encrypted_text = ""

    # open file and store data in a list
    with open(encrypted_file) as file:
        encrypted_text = file.read()
    
    # count letter occurrences
    for character in encrypted_text:

        if character in letter_count:
            letter_count[character] += 1
            total_letters += 1

    # calculate letter frequency
    for letter in alphabet:
        letter_frequency[letter] = letter_count[letter] / total_letters

    # convert frequency dictionaries to tuples for later caclulation
    letter_frequency = letter_frequency.items()
    known_frequencies = known_frequencies.items()

    # sort letter frequencies and known frequencies by frequency (in tuple)
    letter_frequency = sorted(letter_frequency, key=lambda letter: letter[1])
    known_frequencies = sorted(known_frequencies, key=lambda letter: letter[1])

    # create translation table
    encrypted_letters_decreasing = "".join([letter_data[0] for letter_data in letter_frequency])
    known_letters_decreasing = "".join([letter_data[0] for letter_data in known_frequencies])

    translation_table = encrypted_text.maketrans(encrypted_letters_decreasing, known_letters_decreasing)

    decrypted_text = encrypted_text.translate(translation_table)

    return decrypted_text


decrypted_text = decode_cipher("ciphertext.txt")

with open("decryptedtext.txt", "w") as file:
    file.write(decrypted_text)