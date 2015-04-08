#David Gall, 04/01/15, My MadLib story.
'''
Section 1 collect data from user and put into variables
Section 2 functions used for calculating some equations and putting results into variables.
Section 3 array that collects the input from person_name
Section 4 Starts the conditionals section
Section 5 Definition section for food options.
Section 6 Main section of the story
Section 6.1 Which loop for the countdown for part of the main story
Section 6.2 Ending of the story after the loop.
'''
#----------------Section 1-------------------
#Collect some information into the variables here.
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


#---------------Section 2--------------------
#number functions start
#This first function will collect two sets of data(numbers) and multiply them together. It will pull from the numbers that are input in the number1,2 and 3 spot by the user.
def numberMultiply(a,b):
    times = int(a)*int(b)
    return times
#This second function will collect two sets of data(numbers) and add them together.
def numberAdd(a,b):
    add = int(a)+int(b)
    return add
#End number functions
#begin number function variables

#Number functions use is here.
mult = numberMultiply(number1,number2) #This number will return a result of multiplying numbers 1 and 2 through the first function. It uses numbers collected from the user in the number1 and number2 spot and runs them through the function and gives us and answer that we can inject into our print results.
added = numberAdd(number3,number2)#This variable will grab number3 and number2 and run them through the numberAdd function and return a result that we can then apply to our story.
mult2 = numberMultiply(number1,number3)#This variable will again use the multiply function to times two of the numbers given by the user to create a number that we can place in our code.
#End number function variables

#--------------------Section 3-----------------------
#Friends array begins here. The names that go into this array will come from the input of the user as they type in a persons name for person_name 1,2 and 3. They will then be put into the code as friends that they can take along on their journey.
friends = [person_name1,person_name2,person_name3]
#Friends array ends here

#--------------------Section 4----------------------
#Conditional statements Begin
#This first conditional statement takes the users input and looks to see if it is a 'y' or 'Y'. If it is it will run the first result of 'sports team'. If it does not find one of those two variations of y then it will give the result of 'musical group'. This will be placed in the story as a group you get to take along on your trip. 
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

#------------------------Section 5---------------------
#dictionary statement begin
meal_options = {"Meat":"Chicken with Rice","Veg":"Toficken with Rice","Vegan":"Water"}
#dictionary statement end

#------------------------Section 6-----------------------
#Story begins here.
print "\n"+"\033[1m"+name+"\033[0m"+", your challenge is as follows: \nyou are going to be left on a "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". You will be presented with "+"\033[1m"+str(number1)+"\033[0m"+" challenges and you will have "+"\033[1m"+str(added)+"\033[0m"+" hours to complete these tasks before you. \nYou will be allowed to carry a "+"\033[1m"+kitchen_utensil+"\033[0m"+" with you at all times but nothing more. Just so you know "+"\033[1m"+name+"\033[0m"+", you have made "+"\033[1m"+str(mult)+"\033[0m"+" people very happy today. \nSo for your journey today you will be traveling by way of "+"\033[1m"+favorite_animal+"\033[0m"+" to "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". "+"\033[1m"+name+"\033[0m"+", you should get there in about "+"\033[1m"+str(mult2)+"\033[0m"+" days. We will provide you with a meal in route. Your options are as follows: "+"\033[1m"+meal_options['Meat']+"\033[0m"+", "+"\033[1m"+meal_options['Veg']+"\033[0m"+" or "+"\033[1m"+meal_options['Vegan']+"\033[0m"+". \nDuring your travel you will be accompanied by your favorite "+"\033[1m"+company()+"\033[0m"+". You may also take your friends "+"\033[1m"+friends[0]+"\033[0m"+", "+"\033[1m"+friends[1]+"\033[0m"+" and "+"\033[1m"+friends[2]+"\033[0m"+" along to pass the time until you get to your destination. For the record "+"\033[1m"+name+"\033[0m"+", your friends look a little "+"\033[1m"+adjective+"\033[0m"+" to me, yikes. \nOne more thing before we send you off on your adventure, the stakes. If you do not complete these tasks in "+"\033[1m"+str(added)+"\033[0m"+" hours you will go home with "+"\033[1m"+str(mult2)+"\033[0m"+" flaming "+"\033[1m"+adjective+"\033[0m"+" chillies!! However, if you complete the challenge you are going home with "+"\033[1m"+str(number3)+"\033[0m"+" "+"\033[1m"+prize()+"\033[0m"+" for you and your family. Well "+"\033[1m"+name+"\033[0m"+", good luck and it's time for you to head off on your journey. \nFolks let's give "+"\033[1m"+name+"\033[0m"+" a proper countdown: "

#------------------------Section 6.1-----------------------
#Begin the while loop. Counts down from 5 to 1 and places 3 dots after each number.
i=5
while i>0:
    print i,"..."
    i-=1
#End the while loop
#--------------------------Section 6.2------------------------
print "See Ya!!"
#Story ends here































