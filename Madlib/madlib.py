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
mult2 = numberMultiply(number1,number3)
#End number function variables

#Friends array begins here
friends = [person_name1,person_name2,person_name3]
#Friends array ends here
#Conditional statements Begin
def company():
    if cond1 == "y" or cond1 == "Y":
        result = "sports team!!"
    else:
        result = "musical group!!"

    return result

def prize():
    if cond2 == "y" or cond2 == "Y":
        results = "bushels of apples"
    else:
        results = "flats of strawberries"

    return results
#Conditional statements End
#dictionary statement begin
meal_options = {"Meat":"Chicken with Rice","Veg":"Toficken with Rice","Vegan":"Water"}
#dictionary statement end


#Story begins here.
print "\n"+"\033[1m"+name+"\033[0m"+", your challenge is as follows: \nyou are going to be left on a "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". You will be presented with "+"\033[1m"+str(number1)+"\033[0m"+" challenges and you will have "+"\033[1m"+str(added)+"\033[0m"+" hours to complete these tasks before you. \nYou will be allowed to carry a "+"\033[1m"+kitchen_utensil+"\033[0m"+" with you at all times but nothing more. Just so you know "+"\033[1m"+name+"\033[0m"+", you have made "+"\033[1m"+str(mult)+"\033[0m"+" people very happy today. \nSo for your journey today you will be traveling by way of "+"\033[1m"+favorite_animal+"\033[0m"+" to "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". "+"\033[1m"+name+"\033[0m"+", you should get there in about "+"\033[1m"+str(mult2)+"\033[0m"+" days. We will provide you with a meal in route. Your options are as follows: "+"\033[1m"+meal_options['Meat']+"\033[0m"+", "+"\033[1m"+meal_options['Veg']+"\033[0m"+" or "+"\033[1m"+meal_options['Vegan']+"\033[0m"+". \nDuring your travel you will be accompanied by your favorite "+"\033[1m"+company()+"\033[0m"+". You may also take your friends "+"\033[1m"+friends[0]+"\033[0m"+", "+"\033[1m"+friends[1]+"\033[0m"+" and "+"\033[1m"+friends[2]+"\033[0m"+" along to pass the time until you get to your destination. For the record "+"\033[1m"+name+"\033[0m"+", your friends look a little "+"\033[1m"+adjective+"\033[0m"+" to me, yikes. \nOne more thing before we send you off on your adventure, the stakes. If you do not complete these tasks in "+"\033[1m"+str(added)+"\033[0m"+" hours you will go home with "+"\033[1m"+str(mult2)+"\033[0m"+" flaming "+"\033[1m"+adjective+"\033[0m"+" chillies!! However, if you complete the challenge you are going home with "+"\033[1m"+str(number3)+"\033[0m"+" "+"\033[1m"+prize()+"\033[0m"+" for you and your family. Well "+"\033[1m"+name+"\033[0m"+", good luck and it's time for you to head off on your journey. \nFolks let's give "+"\033[1m"+name+"\033[0m"+" a proper countdown: "
#Begin the while loop. Counts down from 5 to 1 and places 3 dots after each number.
i=5
while i>0:
    print i,"..."
    i-=1
#End the while loop
print "See Ya!!"
#Story ends here































