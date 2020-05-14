"""Count words in file."""

input_file = open('./test.txt')

word_counts = {}

for line in input_file:
    # strip whitespace from the end of the line, and then split it into words
    # (the default argument in both rstrip() and split() is whitespace)
    line = line.rstrip()
    words = line.split()

    for word in words:
        # Set the word count to whatever it was + 1; if it wasn't found at all,
        # we'll use `.get(word, 0)` to return 0 if the word wasn't already in
        # the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

# print each word and its count
for word, count in word_counts.items():
    print(word, count)


########### Alternate solution, with functions! ###############

def tokenize(filename):
    """Return list of words from file"""

    tokens = []

    with open(filename) as text_file:
        for line in text_file:
            # strip whitespace from the end of the line, and then split it into
            # words (the default argument in both rstrip() and split() is
            # whitespace)
            line = line.rstrip()
            words = line.split()

            # add the words to our list of tokens
            tokens.extend(words)

    return tokens


def count_words(words):
    """Return dictionary of {word: count} from list"""

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_words(word_counts):
    """Print words: count from dictionary"""

    for word, count in word_counts.items():
        print (word, count)


# tokens = tokenize('test.txt')
# word_counts = count_words(tokens)
# print_words(word_counts)
