"""Count words in file."""


import sys


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

            for word in words:

                # strip common punctuation off the word:
                word = word.strip("'\",.!?-#$%^&();:_")

                # you could also do this more comprehensively with:
                #   import string
                #   word = word.strip(string.punctuation)

                # lowercase the word so "Kit" and "kit" are counted together
                word = word.lower()

                # add the word to our list of tokens
                tokens.append(word)

    return tokens


def count_words(words):
    """Return dictionary of word: count from list"""

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


##############################################################################
# Sorting

# Simplest sort: by word; we can just sort the tuple for this:

def sorted_by_alpha(word_counts):
    """Return tuples of (word, count) sorted naturally (by first item, word)."""

    return sorted(word_counts.items())


# Trickier: sort by count, then by word. To do this, we'll make a
# "key function" that returns (count, word) from a tuple of (word, count):

def reversed_tuple(word_and_count):
    """Given tuple of (word, count), return (count, word)"""

    return (word_and_count[1], word_and_count[0])


def sorted_by_count_and_word(word_counts):
    """Sort word counts by count, then word. Returns list of (word, count)."""

    return sorted(word_counts.items(), key=reversed_tuple)


# Trickier still: sort by count DESCENDING, then by word. To do this, we'll make a
# "key function" that returns (count, word) from a tuple of (word, count). This
# time, though, we'll use the negative of the count --- so -5 would come before -3,
# so they'll be sorted largest-to-smallest:

def reversed_and_negated_tuple(word_and_count):
    """Given tuple of (word, count), return (-count, word)."""

    return (-word_and_count[1], word_and_count[0])


def sorted_by_count_desc_and_word(word_counts):
    """Sort word counts by count, then word. Returns list of (word, count)."""

    return sorted(word_counts.items(), key=reversed_and_negated_tuple)


##############################################################################

def print_words(sorted_list):
    """Print words: count from a list of tuples"""

    for word, count in sorted_list:
        print(word, count)


# get the filename from the command line
input_filename = sys.argv[1]

# turn the file into a list of lowercased, punctuation-stripped words
tokens = tokenize(input_filename)

# create a dictionary of word counts
word_counts = count_words(tokens)

# sort the word counts alphabetically
sorted_word_counts = sorted_by_alpha(word_counts)

# sort the word counts in descending order of frequency - comment in the line
# below to see this in action
# sorted_word_counts = sorted_by_count_and_word(word_counts)

# sort the word counts in descending order of frequency, and within that, in
# ascending alphabetical order - comment in the line below to see this in action
# sorted_word_counts = sorted_by_count_desc_and_word(word_counts)

# print the words and their counts
print_words(sorted_word_counts)
