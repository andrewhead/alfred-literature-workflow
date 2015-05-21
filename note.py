#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
from feedback import Feedback
import argparse


logging.basicConfig(level=logging.INFO, format="%(message)s")

SECTIONS = (
    'concept',
    'system',
    'evaluation',
    'result',
    'formula',
    'exercise',
    'related work',
    'pattern',
)


def autocomplete(sect, pg, note):
    feedback = Feedback()
    add = lambda s: feedback.add_item(
        title='[%s] Write note' % s.title(), 
        subtitle="pg %s, Category: %s, \": %s...\"" % (pg, s, note[:20]), 
        arg='\\t'.join([s, pg, note])
    )
    [add(s) for s in SECTIONS if sect.lower() in s.lower()]
    add(sect)
    return feedback


def default_feedback():
    feedback = Feedback()
    feedback.add_item(
        "Write note: <PageNo> <Category> <Note...>",
        "Save a note for a document.",
    )
    return feedback


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        'Get Alfred autocomplete for the types of note you want to upload')
    parser.add_argument('query',
        help='query of form: page number, partial category name, text of note')
    args = parser.parse_args()
    tokens = args.query.split(' ', 2)
    if len(tokens) <= 1:
        results = default_feedback()
    elif len(tokens) == 2:
        results = autocomplete(tokens[1], tokens[0], '')
    elif len(tokens) > 2:
        results = autocomplete(tokens[1], tokens[0], tokens[2])
    print results
