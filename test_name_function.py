# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:27:59 2020
Test case
@author: joel
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        """ """
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ """
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
        