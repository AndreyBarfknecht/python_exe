"""If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

Pythagorean equation looks like:

c=a2+b2
​

    The a is the length of a short side.
    The b is the length of another short side.
    The c is the length of the hypotenuse.

The hypotenuse is the longest side of the right triangle.

Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c."""
import math
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
raiz = int
c = (a**2) + (b**2)
raiz = math.sqrt(c)
print (raiz)
