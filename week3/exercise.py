#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----

def fizzbuzz(num) :
    if num % 15 == 0 :
        print("fizzbuzz")
    elif num % 3 == 0 :
        print("fizz")
    elif num % 5 == 0 :
        print("buzz")
    else :
        print(num)

for i in range(1, 20) :
    fizzbuzz(i)

# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----



# -----END PAYROLL CODE-----
