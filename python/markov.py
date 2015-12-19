#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). 
# Your program should be called from the command line with two arguments: 
# the name of a file containing text to read, 
# and the number of words to generate. 
# For example, if `chains.txt` contains the short story by Frigyes Karinthy, 
# we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import random
import re
import string


class Markov(object):

    def __init__(self, f, w):
        """Initializes a Markov instance. Parses a text file, self.file,
        to generate from for a given number of words, self.length.
        """
        f = open(f, 'r')
        self.file = f.readlines()
        #line = next(f.readlines())
        self.length = w
        self.order = 1  # will progress by 2-word chunks
        f.close()

    def find_chunk(self):
        m = 0
        n = 1
        string = ''
        chunk = ''
        text = [ ]
        
        while string == '' or string == '\n':
            for num, aline in enumerate(self.file):
                n = random.randrange(num + 2)
                m = random.randrange(num + 22)
                if m == n:
                    string += aline
        string = string.split()         
        
        start = random.randint(0, len(string) - self.order)
        chunk = string[start]
        if self.order == 1:
            pass
        else:
            for i in range(1, self.order):  #should start from 2 not 1?
                chunk = chunk + ' ' + string[start + i]
        text.append(chunk)       
        return text
       
        #chunk = '' 
        #for line in self.file:
        #    filter
        
        # retrive a string len self.order, randomly, from self.file
        # append chunk to text
        # return chunk

    def chunk_seq(self, text):
        """Generates a string of chuncks from an initial chunk.
        Imput: list containing initial chunk.
        Output: a string, wordcount self.length, of chunks.
        """
        chunk = text[-1]
        chunklist = chunk.split()
        acceptable_characters = string.letters + string.digits + ' '

        while len(text) * self.order < self.length:
            # I. Gather possible next chunks
            candidates = [ ]
            for line in enumerate(self.file):   
                if chunklist[-1] in line[1]:
                    line = line[1].split()
                    for n in range(0, len(line) - self.order):
                        candidate_str = ''
                        if line[n] == chunklist[-1]:  
                            candidate_str += line[n+1]                       
                            if self.order == 1:
                                pass
                            else:
                                for i in range(2, self.order + 1):
                                    candidate_str += ' ' + line[n+i]             
                        candidate_str = filter(lambda x: x in acceptable_characters, candidate_str)                                                           
                        candidates.append(candidate_str)
            # II. Edit chunks
            candidates_edited = [ ]
            for i in candidates:
                if i != '':
                    candidates_edited.append(i)
            # III. Pick next chunk
            if candidates_edited == [ ]:
                text.append(chunk)
            else:
                r = random.randint(0, len(candidates_edited) - 1)
                chunk = candidates_edited[r]
                text.append(chunk)
                #print r
        
        return ' '.join(text)


tractatus = Markov('/Users/Ben/Documents/tractatus.txt', 50)
text = Markov.find_chunk(tractatus)
print Markov.chunk_seq(tractatus, text)

# Next step: make program run from command line,
# e.g., tractatus = Markov(raw_input(), raw_input())

# Next step: learn how to call functions w/in functions 
# w/in a class hierarchy and split find_chunk and chunk_seq
# into many smaller functions
