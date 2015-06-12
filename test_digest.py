#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import unittest
from digest import to_sortable


logging.basicConfig(level=logging.INFO, format="%(message)s")


class DigitToSortableTest(unittest.TestCase):

    def testGetNoneFromOnlyDash(self):
        self.assertIsNone(to_sortable('-'))

    def testGetLeftSideOfDash(self):
        self.assertEqual(to_sortable('2-3'), [2])

    def testSplitDotIntoList(self):
        self.assertEqual(to_sortable('5.2'), [5, 2])


if __name__ == '__main__':
    unittest.main()
