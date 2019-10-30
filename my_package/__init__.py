# lambdata - a colection of data science help functions

import pandas as pd
import numpy as np 
from random import randint
import datetime


#sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(10))
RANDINT = pd.DataFrame(np.random.randint(0,100,10))

#sample functions
def increment(x):
    return(x+1)

class Date:
    """
    Get Date day, month & year

    """
    # the class constructor
    def __init__(self, year=1900, month=1, day=1):
        for arg in [year, month, day]:
            if type(arg) != int:
                raise TypeException('Day, month and year must be `int`')

        self.day = day
        self.month = month
        self.year = year


    def get_day(self):
        """
        print day
        """
        return self.day

    def get_month(self):
        """
        print month
        """
        return self.month

    def get_year(self):
        """
        print year
        """
        return self.year

    def get_full_date(self):
        """
        print full date
        """
        print({}-{}-{}.format(self.year, self.month, self.day))

