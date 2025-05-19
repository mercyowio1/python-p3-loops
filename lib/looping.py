#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    start = 10
    while start >= 1:
        print(start)
        start -= 1

    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
      return [x ** 2 for x in int_list]


squared = square_integers([1,2,3,4,5])
print(squared)
   
    
    
def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
            
            i += 1
fizzbuzz()