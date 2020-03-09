# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:45:17 2020

@author: joel
"""


import unittest
from Python11_1City_Country import city_country

class CityCountryTestCase(unittest.TestCase):
    """ Tests from Python11-1City_Country"""
    def test_city_country(self):
        formattedcc = city_country('santiago','chile') 
        self.assertEqual(formattedcc,'Santiago, Chile')
        
    