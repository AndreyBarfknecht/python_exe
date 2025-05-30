"""The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

    🦁 Gryffindor
    🦅 Ravenclaw
    🦡 Hufflepuff
    🐍 Slytherin

Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

    If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
    Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
    Else, output the message "Wrong input."

Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

    If the answer is 1, Hufflepuff +2.
    Else if answer is 2, Slytherin +2.
    Else if answer is 3, Ravenclaw +2.
    Else if answer is 4, Gryffindor +2.
    Else, output the message "Wrong input."

Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

    If the answer is 1, Slytherin +4.
    Else if the answer is 2, Hufflepuff +4.
    Else if the answer is 3, Ravenclaw +4.
    Else if the answer is 4, Gryffindor +4.
    Else, output "Wrong input."

Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!"""

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("\nWelcome to Hogwarts!!!\n\nThe Sorting Hat will ask you some questions to find out which house you belong to.")#inicio dando bem vindo 
#questão 1
Q1 = int (input("\nDo you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nAnswer: "))
if Q1 == 1:
    Gryffindor += 1 
    Ravenclaw += 1
   
elif Q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

#questão 2 
Q2 = int (input("\nQ2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nAnswer: "))
if Q2 == 1:
    Hufflepuff += 2
elif Q2 == 2:
    Slytherin += 2
elif Q2 == 3:
    Ravenclaw += 2
elif Q2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

#Questão 3
Q3 = int (input("\nQ3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nAnswer:"))
if Q3 == 1:
    Slytherin += 4
elif Q3 == 2:
    Hufflepuff += 4
elif Q3 == 3:
    Ravenclaw += 4
elif Q3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

#Contador de pontos
#print( "\n 🦁 Gryffindor = ",Gryffindor,"\n","🦅 Ravenclaw = ",Ravenclaw,"\n","🦡 Hufflepuff = ",Hufflepuff,"\n","🐍 Slytherin = ",Slytherin)

"""if Gryffindor > Ravenclaw:
    if Gryffindor > Hufflepuff:
        if Gryffindor > Slytherin:
            print("you are from the house 🦁 Gryffindor")
        
if Ravenclaw > Gryffindor:
    if Ravenclaw > Hufflepuff:
        if Ravenclaw > Slytherin:
            print("you are from the house 🦅 Ravenclaw")   

if Hufflepuff > Gryffindor:
    if Hufflepuff > Ravenclaw:
        if Hufflepuff > Slytherin:
            print("you are from the house 🦡 Hufflepuff")

if Slytherin > Gryffindor:
    if Slytherin > Ravenclaw:
        if Slytherin > Hufflepuff:
            print("you are from the house 🐍 Slytherin")"""

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("\nYou are from the house 🦁 Gryffindor")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("\nYou are from the house 🦅 Ravenclaw")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("\nYou are from the house 🦡 Hufflepuff")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print("\nYou are from the house 🐍 Slytherin")
else:
    # This 'else' handles ties or other scenarios not covered by the above conditions.
    print("\nThere was a tie, or the conditions were not fully met for a single house.")



    
 