#David Gall, 04/01/15, My MadLib story.
#Collect some information here.
'''name = raw_input("What is your name? ")
favorite_meal = raw_input("What is your favorite meal? ")
kitchen_utensil = raw_input("Name a kitchen utensil? ")
verb = raw_input("Name the first verb you think of? ")
favorite_animal = raw_input("What is your favorite animal? ")
slimy = raw_input("Name something slimy? ")
adjective = raw_input("Name a great adjective? ")
person_name1 = raw_input("Give me a persons name? ")# Names will be part of the array.
person_name2 = raw_input("Give me another persons name? ")
person_name3 = raw_input("Give me just one more persons name? ")'''
number1 = raw_input("Please give me a number between 1-10? ")
number2 = raw_input("What is your favorite number? ")
number3 = raw_input("How many people are there in your immediate family? ")

#print name+", "+favorite_meal+", "+kitchen_utensil+", "+verb+", "+favorite_animal+", "+slimy+", "+adjective+", "+person_name1+", "+person_name2+", "+person_name3+", "+number1+", "+number2+", "+number3+"."

def numberMultiply(a,b):
    times = int(a)*int(b)
    return times

def numberAdd(a,b):
    add = int(a)+int(b)
    return add


mult = numberMultiply(number1,number2)
added = numberAdd(number3,number2)

print number1+" * "+number2+" is: "+str(mult)+". "+number3+" + "+number2+" is: "+str(added)