"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path)
    one_string = text_file.read()
    text_file.close()

    return one_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    # your code goes here
    chains = {}
    keys = text_string.split()

    for i in range(len(keys) - 2):
        key = (keys[i], keys[i + 1])
        value = keys[i + 2]

        if key not in chains.keys():
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    # your code goes here
    keys = list(chains.keys())
    key = choice(keys)
    words = [key[0], key[1]]
    word = choice(chains[key])

    while True:
        key = (key[1], word)

        if key in keys:
            words.append(word)
            word = choice(chains[key])
        else:
            break

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
