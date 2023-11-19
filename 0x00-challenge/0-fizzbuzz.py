#!/usr/bin/python3
""" 
FizzBuzz Script

It implements FizzBuzz problem, where numbers from 1 to n are printed,
with certain substitutions:
- For multiples of three, "Fizz" is printed instead of the number.
- For multiples of five, "Buzz" is printed.
- For numbers that are multiples of both three and five, "FizzBuzz" is printed.

Usage:
    ./script_name.py <number>

Example:
    ./script_name.py 89
"""

import sys

def fizzbuzz(n):
    """
    FizzBuzz function it prints nums from 1 to n as described above.
    
    Parameters:
        n (int): Upper limit for the range of numbers to be processed.
    """
    if n < 1:
        return

    tmp_result = []
    for x in range(1, n + 1):
        if (x % 3) == 0 and (x % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (x % 3) == 0:
            tmp_result.append("Fizz")
        elif (x % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(x))
    print(" ".join(tmp_result))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./script_name.py <number>")
        print("Example: ./script_name.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
