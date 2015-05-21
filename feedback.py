#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import xml.etree.ElementTree as et


logging.basicConfig(level=logging.INFO, format="%(message)s")


'''
REUSE: Feedback class From Youtube plugin by willfarrell
https://github.com/willfarrell/alfred-youtube-workflow/blob/master/src/Feedback.py
'''
class Feedback(object):

    def __init__(self):
        self.feedback = et.Element('items')

    def __repr__(self):
        """XML representation used by Alfred
        Returns:
            XML string
        """
        return et.tostring(self.feedback)

    def add_item(self, title, subtitle = '', arg = '', valid = 'yes', autocomplete = '', icon = 'icon.png'):
        item = et.SubElement(self.feedback, 'item', uid=str(len(self.feedback)), arg=arg, valid=valid, autocomplete=autocomplete)
        _title = et.SubElement(item, 'title')
        _title.text = title
        _sub = et.SubElement(item, 'subtitle')
        _sub.text = subtitle
        _icon = et.SubElement(item, 'icon')
        _icon.text = icon
