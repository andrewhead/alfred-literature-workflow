#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import argparse
from note import SECTIONS
import re


logging.basicConfig(level=logging.INFO, format="%(message)s")


def print_digest(notesfile, doc_name, dashes, caps):

    # Aggregate notes by category type
    cat_notes = {}
    with open(notesfile, 'r') as infile:
        for l in infile.readlines():
            name, cat, pg, note = l.strip().split('\t')
            if name == doc_name:
                if cat not in cat_notes:
                    cat_notes[cat] = []
                cat_notes[cat].append((note, pg))

    # Print header
    print "Document: %s\n" % doc_name

    cats_printed = []

    def print_category(cat_notes, cat, dashes, caps):
        print '===' + cat.title() + '==='
        notes_sorted = sorted(cat_notes[cat], key=lambda n: to_sortable(n[1]))
        for text, pg in notes_sorted:
            if dashes:
                print '- ',
            line = text[0].upper() + text[1:] if caps else text
            line = re.sub(r'[ ,]*\(\*\)\s?', r'\n- ', line)
            line = re.sub(r'[ ,]*\((\d)\)\s?', r'\n\1. ', line)
            print line,
            if pg != '-':
                print '(%s)' % (pg)
            else:
                print
        cats_printed.append(cat)

    # Print out default sections in order
    for s in SECTIONS:
        if s in cat_notes.keys():
            print_category(cat_notes, s, dashes, caps)
            print

    # Print remaining custom categories
    for c in cat_notes.keys():
        if c not in cats_printed:
            print_category(cat_notes, c, dashes, caps)
            print


def to_sortable(token):
    if token == '-':
        return None
    firstpart = token.split('-')[0]
    subparts = firstpart.split('.')
    sortables = []
    for s in subparts:
        try:
            sortables.append(int(s))
        except ValueError:
            sortables.append(s)
    return sortables


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Write digest of notes about a paper.")
    parser.add_argument('notesfile', help="Name of TSV file that contains notes")
    parser.add_argument('textname', help="Name of document for which digest should be created")
    parser.add_argument('--dashes', action='store_true', help="Start each line with dash")
    parser.add_argument('--caps', action='store_true', help="Capitalize each line")

    args = parser.parse_args()
    print_digest(args.notesfile, args.textname, args.dashes, args.caps)
