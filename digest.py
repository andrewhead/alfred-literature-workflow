#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import argparse
from note import SECTIONS


logging.basicConfig(level=logging.INFO, format="%(message)s")


def print_digest(notesfile, doc_name):

    # Aggregate notes by category type
    cat_notes = {}
    with open(notesfile, 'r') as infile:
        for l in infile.readlines():
            name, cat, pg, note = l.strip().split('\t')
            if name == doc_name:
                if cat not in cat_notes:
                    cat_notes[cat] = []
                cat_notes[cat].append("%s (%s)" % (note, pg))

    # Print header
    print "Document: %s\n" % doc_name

    cats_printed = []

    def print_category(cat_notes, cat):
        print cat.title()
        for n in cat_notes[cat]:
            print '* %s' % n
        cats_printed.append(cat)

    # Print out default sections in order
    for s in SECTIONS:
        if s in cat_notes.keys():
            print_category(cat_notes, s)
            print
 
    # Print remaining custom categories
    for c in cat_notes.keys():
        if c not in cats_printed:
            print_category(cat_notes, c)
            print


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Write digest of notes about a paper.")
    parser.add_argument('notesfile', help="Name of TSV file that contains notes")
    parser.add_argument('textname', help="Name of document for which digest should be created")
    args = parser.parse_args()
    print_digest(args.notesfile, args.textname)

