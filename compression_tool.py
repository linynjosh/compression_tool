#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='Compression Tool',
                    description='This challenge is to build your own command like tool to compress text files.',
                    epilog='For more information check out the link to this challenge: https://codingchallenges.fyi/challenges/challenge-huffman')
    parser.add_argument('filename')  

    args = parser.parse_args()

    char_occurrence_freq = {}

    file = open(args.filename, "r")
    
    for line in file:
        for char in line:
            if char not in char_occurrence_freq:
                char_occurrence_freq[char] = 1
            else:
                char_occurrence_freq[char] += 1

    print(char_occurrence_freq)
    
if __name__ == "__main__":
    main()