#This is a MadLibs project 
#My name: Sreehitha
#Who I collaborated with: 

print("************************************")
print("|                                  |")
print("|      Welcome to MadLibs          | ") 
print("|                                  |")
print("************************************")

print('MadLibs is a fill-in-the-blanks story game. The player must choose words based on the given prompts, and the computer will return a short story that includes the words the user chose.')

play = input("Do you want to play MadLibs?(y/n) ")

if play == "y":
    person_name = input("Choose a name for a person: ")
    place = input("Choose a place: ")
    noun_1 = input("Choose a singlular noun: ")
    animal_1 = input("Choose an animal: ")
    adjective_1 = input("Choose an adjective for a feeling: ")
    adjective_2 = input("Choose an adjective: ")
    adjective_3 = input("Choose an adjective: ")
    animal_2 = input("Choose an animal: ")
    food = input("Choose a food: ")
    
    print("""
    Over break I am going camping with """ +person_name+""". It is important 
    to be prepared when camping at place , so I made sure to pack a 
    sleeping bag, flashlight, and a """ +noun_1+""". The possibility of seeing a 
    """ +animal_1+""" makes me feel """ +adjective_1+""". I am excited to go 
    hiking on the """ +adjective_2+""" trail. If I see a """ +adjective_3 +""" """ +animal_2+"""
    on the hike, I will take it home as my new pet! The best part of 
    camping is eating """ +food+""" by the campfire!
    """)
    
    print("Thanks for playing! Goodbye!")
    
else:
    print("Goodbye!")


#quiz part 2

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

choose = input("Do you want to do addition or subtraction? ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choose == "addition":
    result = add_numbers(num1, num2)
    print("the result of adding is:", result)
elif choose == "subtract":
    result = subtract_numbers(num1, num2)
    print("the result of subtracting is:", result)

else:
    print("Invalid choice. Please pick either add or subtract")