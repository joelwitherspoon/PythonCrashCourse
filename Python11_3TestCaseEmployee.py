# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:54:34 2020

@author: joel
"""


import unittest
from Python11_3Employee import Employee

class TestCaseEmployee(unittest.TestCase):
    """Create a set of Tests for the Employee Class"""
    
    def setUp(self):
        
        self.emp = Employee('J','D')
        
    def test_give_default_raise(self):

        self.assertEqual(self.emp.give_raise(''),'J D 5000')
        
    def test_give_custom_raise(self):

        self.assertEqual(self.emp.give_raise(5000),'J D 10000')
    
