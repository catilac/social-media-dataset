#!/usr/bin/env python

"""generate.py
Generate a language dataset based off of facebook and twitter data dumps
"""

import csv
from fbparser import FBParser

def scrape_twitter(outfile):
    with open('data/t/tweets.csv') as f:
        reader = csv.DictReader(f)
        fieldnames = ['source', 'content']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        for row in reader:
            writer.writerow({'source': 't', 'content': row['text']})

def scrape_fb_messages(outfile):
    message_file = open('data/fb/html/messages.htm', 'r')
    fieldnames = ['source', 'content']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    parser = FBParser(writer)
    parser.feed(message_file.read())

def scrape_facebook(outfile):
    scrape_fb_messages(outfile)

def generate_dataset(output):
    # open output file
    outfile = open(output, 'w+') 
    scrape_twitter(outfile)
    scrape_facebook(outfile)

if __name__ == '__main__':
    print('Generating new dataset...')
    generate_dataset('output.csv')
