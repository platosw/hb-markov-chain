"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contexts = ''

    for file in file_path:
        open_file = open(file)
        contexts += open_file.read()
        open_file.close()

    return contexts


def make_chains(text_string, n):
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
    keys = text_string.strip().split()

    for i in range(len(keys) - n):
        key = tuple((keys[i:i + n]))
        value = keys[i + n]

        if key not in chains.keys():
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    # your code goes here
    keys = list(chains.keys())
    key = choice(keys)

    # check the first char of first item in the key is uppercase
    while not key[0][0].isupper():
        key = choice(keys)

    words = list(key)
    word = choice(chains[key])

    punc = ['!', '.', '?']

    while True:
        key = key[1:] + (word,)  # 이 부분 꼭!! 질문하기!!
        words.append(word)

        # if word ends in punctuation, break
        if word[-1] in punc:
            break

        word = choice(chains[key])

    return ' '.join(words)


input_path = sys.argv[1:]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains)

print(random_text)
