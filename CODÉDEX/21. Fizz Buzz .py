"""Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝

Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?

Create a fizz_buzz.py program that outputs numbers from 1 to 100.

Here's the catch:

    For multiples of 3, print "Fizz" instead of the number.
    For multiples of 5, print "Buzz" instead of the number.
    Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

The output should look like:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...

Btw, it's totally okay if you can't get this one... it's a tough problem! Take a look at the hint and the solution before moving forward to the Checkpoint Project! ⛳️"""

for numero  in range(1,101):
    

    if numero % 3 == 0 and numero % 5 == 0:
        numero = "FizzBuzz"
    elif numero % 3 == 0:
        numero = "Fizz"
    elif numero % 5 == 0:
        numero = "Buzz"
    

    print(numero)
