"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()
    # text = text.replace("\n", " ") # replace /n with spaces
    # text = text.rstrip() #remove the last space

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_string = text_string.split(" ")

    # your code goes here
    for index in range(len(text_string)-1):
        tup = (text_string[index], text_string[index+1])
        if index < len(text_string)-2:
            chains[tup] = chains.get(tup, [])
            word_following = text_string[index+2]
            chains[tup].append(word_following)

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    words = []

    # your code goes here

    list_keys = list(chains.keys())
    

    starting_key = choice(list_keys)
    # append the two starting key
    words.append(starting_key[0])
    words.append(starting_key[1])

    while True:
        current_key = tuple(words[-2:])
        # print (current_key)
        if chains.get(current_key) is None:
            break
        else:
            next_word = choice(chains[current_key])
            words.append(next_word)
    
    return " ".join(words)


input_path = "green-eggs.txt"
# input_text = "hi there mary hi there juanita"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

print(input_text)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
