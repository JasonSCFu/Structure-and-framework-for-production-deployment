##  a is user input in __name__ , b is hard coded in __call__, c is defined in self.c


import time as time
import argparse
from logger import logger
import utility as utility


class Pipeline():


    def __init__(self, c = 5):  ### specify c
        self.c = c
        self.arg = utility.parse_args()   ### import value of e from parse_args from utility

    def addition(self,): 
        d = self.c + 5   ### calculate d
        return d

    def __call__(self, a , b = 5 ):  ### specify b
        d = self.addition()   ### self-defined function.
        cal_result = a + b + d + args.e
        return cal_result




if  __name__ == "__main__":


    start_time = time.time()
    pipeline = Pipeline()
    args = pipeline.arg
    #args.e = 10     ## we can also define e here
    a = 10   ### specify a
    if a > 5:
        logger.warn("a > 5")
    cal_result = pipeline(a)

    end_time = time.time()
    time_used = end_time - start_time
    print("a =", a , "e = ", args.e, "cal_result =", cal_result)

