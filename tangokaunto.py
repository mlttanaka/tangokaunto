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


# TODO: write a function (or functions) that filters out punctuation
# for a more accurate word count.


def main():
    unicode_text = read_unicode_file()
    items = segment_words(unicode_text)
    
    for item in items:
        print item

    print '-' * 30
    print "Unfiltered Word Count:", len(items)
    print '-' * 30


if __name__ == '__main__':
    main()
