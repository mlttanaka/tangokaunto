#!/usr/bin/env python
"""
Tangokaunto, "word count" in Japanese, reads Japanese text from an input file,
splits the text into words (as defined by TinySegmenter), and prints out a
word count as well as all the word it segmented from the text.

author:  mochipuff
"""
import sys
import codecs
import tinysegmenter as ts

script, filename = sys.argv


def read_unicode_file():
    """
    Reads unicode data from input file and returns it as a text string.
    """
    f = codecs.open(filename, encoding='utf-8')
    unicode_text = f.read()
    f.close()
    return unicode_text


def segment_words(unicode_text):
    """
    Segments words from unicode text using TinySegmenter and returns
    the them as a list.  Please note that TinySegmenter also treats
    punctuation as words.
    """
    segment = ts.TinySegmenter()
    unfiltered_words = segment.tokenize(unicode_text)
    return unfiltered_words


def isRealWord(word):
    """
    Returns true if a word is not found in the list of punctuaction
    characters.
    """
    punctuation_list = range(33, 63)  # some English punctuation
    # some Japanese punctuation (Extend the list as you see fit.)
    punctuation_list.extend(range(ord(u'\u3000'), ord(u'\u3020')))
    punctuation_list.extend(range(ord(u'\uff00'), ord(u'\uff0f')))
    punctuation_list.extend(range(ord(u'\uff10'), ord(u'\uff1f')))
    punctuation_list.append(ord(u'\u30fb'))

    if len(word) > 1:
        return True
    elif len(word) == 1 and ord(word) not in punctuation_list:
        return True
    else:
        return False


def filter_words(unfiltered_wordlist):
    """
    Filters out punctuation from an unfiltered list of words; returns
    a more accurate wordlist.
    """
    filtered_wordlist = filter(isRealWord, unfiltered_wordlist)
    return filtered_wordlist


def main():
    # Read the file
    unicode_text = read_unicode_file()

    # Get the entire list of words as defined by TinySegmenter.
    unfiltered_wordlist = segment_words(unicode_text)

    # Filter out punctuation from the list.
    filtered_wordlist = filter_words(unfiltered_wordlist)

    # Print entire unfiltered word list & word count.
    for index, word in enumerate(unfiltered_wordlist):
        print index, word
    print '-' * 30
    print "Unfiltered Word Count:", len(unfiltered_wordlist)
    print '\n'

    # Print entire filtered word list & word count.
    for index, word in enumerate(filtered_wordlist):
        print index, word
    print '-' * 30
    print "Filtered Word Count:", len(filtered_wordlist)


if __name__ == '__main__':
    main()
