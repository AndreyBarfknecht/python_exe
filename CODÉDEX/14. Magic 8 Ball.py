"""The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8-ball with some of the following answers:

    1 Yes - definitely.
    2 It is decidedly so.
    3 Without a doubt.
    4 Reply hazy, try again.
    5 Ask again later.
    6 Better not tell you now.
    7 My sources say no.
    8 Outlook not so good.
    9 Very doubtful.

Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

Question:      [Question]
Magic 8 Ball:  [Answer]

For example:

Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""

import random
question = input("What is your question? ")
num = random.randint(1,9) #Número aleatorio sorteado
print("\nthe question is: ",question)
#print(num)
if num == 1:#Respostas da bola 8
    print("\nMagic 8 Ball: Yes - definitely.")
if num == 2:
    print("\nMagic 8 Ball: It is decidedly so.")
if num == 3:
    print("\nMagic 8 Ball: Without a doubt.")
if num == 4:
    print("\nMagic 8 Ball: Reply hazy, try again.")
if num == 5:
    print("\nMagic 8 Ball: Ask again later.")
if num == 6:
    print("\nMagic 8 Ball: Better not tell you now.")
if num == 7:
    print("\nMagic 8 Ball: My sources say no.")
if num == 8:
    print("\nMagic 8 Ball: Outlook not so good.")
if num == 9:
    print("\nMagic 8 Ball: Very doubtful.")