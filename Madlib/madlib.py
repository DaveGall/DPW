#David Gall, 04/01/15, My MadLib story.
#Collect some information here.
name = raw_input("What is your name? ")
favorite_meal = raw_input("What is your favorite meal? ")
kitchen_utensil = raw_input("Name a kitchen utensil? ")
verb = raw_input("Name the first verb you think of? ")
favorite_animal = raw_input("What is your favorite animal? ")
adjective = raw_input("Name a great adjective? ")
person_name1 = raw_input("Give me a persons name? ")# Names will be part of the array.
person_name2 = raw_input("Give me another persons name? ")
person_name3 = raw_input("Give me just one more persons name? ")
number1 = raw_input("Please give me a number between 50-100? ")
number2 = raw_input("What is your favorite number? ")
number3 = raw_input("How many people are there in your immediate family? ")
cond1 = raw_input("Do you like sports? y/n? ")
cond2 = raw_input("Do you like apples? y/n?")

#Check to see that all data is collected.
#print name+", "+favorite_meal+", "+kitchen_utensil+", "+verb+", "+favorite_animal+", "+", "+adjective+", "+person_name1+", "+person_name2+", "+person_name3+", "+number1+", "+number2+", "+number3+"."

#number functions start
def numberMultiply(a,b):
    times = int(a)*int(b)
    return times

def numberAdd(a,b):
    add = int(a)+int(b)
    return add
#End number functions
#begin number function variables

#Number functions use is here.
mult = numberMultiply(number1,number2)
added = numberAdd(number3,number2)

print number1+" * "+number2+" is: "+str(mult)+". "+number3+" + "+number2+" is: "+str(added)

#End number function variables
#While loop begins
i=5
while i>=0:
    print i
    i = i-1
#While loop ends.
#Friends array begins here
friends = [person_name1,person_name2,person_name3]
print "Your friends "+friends[0]+", "+friends[1]+" and "+friends[2]+", will be joining us for dinner."

#Friends array ends here
#Conditional statements Begin
if cond1 == "y" or cond1 == "Y":
    sports = "You will also be traveling with your favorite sports team!!"
    print sports
else:
    band = "You will be traveling with your favorite musical group!!"
    print band



#Conditional statements End













