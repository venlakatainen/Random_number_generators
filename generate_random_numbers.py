# Script to generate random numbers to the file

import random

def random_numbers():

    file_to_write_numbers = open('random_numbers.txt','a')

    for i in range(10000):
        random.seed()
        file_to_write_numbers.write(str(random.random()))
        file_to_write_numbers.write("\n")
        
    file_to_write_numbers.close()
    
random_numbers()