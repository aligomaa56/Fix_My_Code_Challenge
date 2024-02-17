#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three, print "Fizz" instead of the number.
    - For multiples of five, print "Buzz".
    - For numbers which are multiples of both three and five, print "FizzBuzz".
    """
    if n < 1:
        return

    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    print(" ".join(output))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    fizzbuzz(number)
