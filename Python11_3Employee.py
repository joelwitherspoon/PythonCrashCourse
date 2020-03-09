# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:55:14 2020

@author: joel
"""
class Employee():
    """Store employee name and salary"""
    
    def __init__(self,fname,lname):
        """Store responses"""
        self.fname = fname
        self.lname = lname
        self.annual_salary = 0
        
    def give_raise(self, new_annual_salary=''):
        """Add an annual salary but add a custom salary if necessary"""
        if new_annual_salary:
            self.annual_salary = new_annual_salary + \
                int(self.annual_salary)
        else:
            self.annual_salary = self.annual_salary + 5000

    def show_results(self):
        print("Salary results: "+self.fname.title()+" "+self.lname.title()+" "\
              +str(self.annual_salary))
        