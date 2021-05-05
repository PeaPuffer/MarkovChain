"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    

    return contents


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

    chains = {}

    contents = open_and_read_file('green-eggs.txt')
    words = contents.split()

    for idx in range(len(words) - 2):
        bigram = (words[idx], words[idx + 1])
        
        # print(bigram)
        # print(words[idx], words[idx + 1], words[idx + 2])

    
        if bigram not in chains:
            chains[bigram] = []
        chains[bigram].append(words[idx +2])

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # chain['bigrams'] = [random.choice()]
    # chains.get(bigrams, 0)
    

    bigrams = choice(list(chains.keys()))
    words.append(bigrams[0])
    words.append(bigrams[1])
    while True: #set condition
        next_words = chains[bigrams] 
        rand_word = choice(next_words)
        words.append(rand_word)
        bigrams = (bigrams[1], rand_word)

 
    
    # for bigrams, word_choices in chains.items():
        # pick_word = choice(word_choices)
        # new_set = list()
        # new_set.append(bigrams[0])
        # new_set.append(bigrams[1])
        # new_set.append(pick_word)
        # words.extend(new_set)
        # # print(words)
        # bigrams = (bigrams[1], pick_word)

        # for bigrams in chains.items():
        #     new_set2 = list()
        #     new_set2.append(bigrams[0])
        #     new_set2.append(bigrams[1])
        #     new_set2.append(pick_word)
        #     words.extend(new_set2)
           
        



    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
