#!/usr/bin/env python3

# Author: Dylan Muller
# Date Received: 20/01/2022
# Date Completed: 22/01/2022

# ##########################################
# Problem Statement:                       #
#                                          #
# 10! = 10 x 9 x 8 ... 3 x 2 x 1 = 3628800 #
# Find the sum of the digits               #
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27           #
############################################

# Break problem up into multiple parts
# 1. Calculate n! (done)
# 2. Use as few casting operators as possible (none casted)
# 3. Use numpy for all math operations (done)
# 4. Calculate sum of n! digits (done)
# 5. Implement multithreading (done)

# The approach taken to calculations was to use Python's
# built in arbitrary length integer type (bignum) as well 
# as numpy's object_ class (dtype=numpy.object_)

# Import libraries
import sys
import numpy
from multiprocessing import Pool

# Convert string to integer without casting,
# returns integer
def str_to_int_without_cast(string):
    '''string - input string to convert'''
    number = 0
    char_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
    for index, char in enumerate(reversed(string)):
        if char not in char_dict:
            return -1
        z = numpy.power(10,index,dtype=numpy.object_)
        y = numpy.multiply(char_dict[char], z)
        number = numpy.add(number,y)
    return number

# Extract individual digits from number n, 
# returns list
def extract_digits(n):
    '''n - number to extract digits from'''
    v = []
    base = 10
    if numpy.equal(n,0):
        v = [0]
    while n:
        z = n
        n = numpy.floor_divide(z, base, dtype=numpy.object_)
        d = numpy.mod(z, base, dtype=numpy.object_)
        v.append(d)
    return v


# Count number of digits of number
def count_digits(n):
    '''n - number to count digits from'''
    if n <= 999999999999997:
        # Use numpy.log10 for small integers
        return int(numpy.log10(n)) + 1
    else:
        counter = 15
        # Step is an important variable
        # that affects performance
        # This value should be high for
        # large factorial results
        step = 50000
        # Use rough estimation for
        # larger integers
        power = 1
        while numpy.greater_equal(n,power):
            power = numpy.power(10, counter, dtype=numpy.object_)
            counter += step
        return counter

# Seperate digits into segments
def seperate_digits(n, segments):
    '''n - number to seperate
       segments - number of segments to create
    '''
    digit_count = count_digits(n)
    count = numpy.floor_divide(digit_count, segments , dtype=numpy.object_)
    # Ensure single digit factorials are processed
    if(numpy.equal(count, 0)):
        count = 1
    v = []
    while n > 0:
        z = n
        # 10 ** count
        p = numpy.power(10, count, dtype=numpy.object_)
        # z // p
        n = numpy.floor_divide(z, p, dtype=numpy.object_)
        # z % p
        r = numpy.mod(z, p, dtype=numpy.object_)
        v.insert(0,r)
    return v


# Print program usage
def print_usage():
    '''No arguments'''
    print("Usage: factorial-digits [n!]")
    print("[n!] = n factorial")


# Add list chunk
def adder(arr):
    '''arr - list to sum'''
    result = 0
    for i in arr:
        result = numpy.add(result, i)
    return result


# Main entry point
def main():

    ###############################################
    #               Performance                   #
    #                                             #
    #     $ python3 solution.py 100000            #
    #     Time to run: 7.2s                       #
    #     CPU: 3.5GHz Dual-Core AMD Athlon 3000G  #
    #     RAM: 8GB DDR3                           #
    #                                             #
    ###############################################
    
    if(len(sys.argv) != 2):
        print_usage()
        return

    # Converts the first argument into an integer
    # without casting
    factorial = str_to_int_without_cast(sys.argv[1])

    # Ensure numpy.math.factorial() can
    # handle input
    if(numpy.greater(len(sys.argv[1]), 18)):
        print("Cannot compute factorial.")
        print("Input too large!")
        return

    if(numpy.equal(factorial, -1)):
        print("Invalid input!")
        return


    # Calculate factorial of input using numpy
    result = numpy.math.factorial(factorial)


    #############################################
    #         MULTITHREADING BLOCK 1            #
    #                                           #
    #    The first part of this code block uses #
    #    Python's multiprocessing features in   #
    #    order to implement parallelism for     #
    #    extracting individual digits from a    #
    #    group of digits                        #
    #                                           #
    #############################################

    # Allocate number of workers (multithreading)
    # adjust as neccessary (effects performance)
    workers = 10
    p = Pool(processes=workers)

    # Seperate digits into groups for processing
    groups = seperate_digits(result, workers)

    # Setup output array (contains all factorial digits)
    digits = []
    # Mapping the groups for processing where each digit
    # is seperated from each group
    chunks = p.map(extract_digits, groups)
    p.close()
    p.join()

    # Add all the digits together
    for chunk in chunks:
        digits += chunk

    #############################################
    #         MULTITHREADING BLOCK 2            #
    #                                           #
    #    Here all the digits that have been     #
    #    extracted are broken into groups again #
    #    and summed in their own thread to      #
    #    produce the final result (answer)      #
    #                                           #
    #############################################
   
    p = Pool(processes=workers)
    # Splitting the digits array into slices for processing 
    slices = [digits[i::workers] for i in range(workers)]
    # Mapping the slices array to processes where sum of each slice is calculated
    chunks = p.map(adder, slices)
    p.close()
    p.join()

    # Sum of factorial result stored in accumulator
    accumulator = 0
    for chunk in chunks:
        accumulator = numpy.add(accumulator, chunk)

    # Print answer
    print(accumulator)
    

# Call main entry point
if __name__ == '__main__':
    main()
