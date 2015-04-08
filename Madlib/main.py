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
name = raw_input("What is your name? ")#This will be used to make the story personal and we will be able to reuse the users name throughout the stpry.
favorite_meal = raw_input("What is your favorite meal? ")#This will be used to describe the beautiful island that the user will be traveling to.
kitchen_utensil = raw_input("Name a kitchen utensil? ")#This will be used to represent what the user can take to use in their quest.
verb = raw_input("Name the first verb you think of? ")#Grab a verb from the user to place in the story as a description of several different things.
favorite_animal = raw_input("What is your favorite animal? ")#This will be used to describe how the user will be traveling to their destination.
adjective = raw_input("Name a great adjective? ")#An adjective that will hopefully make the story funny or gross.
person_name1 = raw_input("Give me a persons name? ")# Names will be part of the array. Each of the next three inputs will be names that will be used as friends of the user, ones that they won't know but I am sure will have a great time traveling with.
person_name2 = raw_input("Give me another persons name? ")
person_name3 = raw_input("Give me just one more persons name? ")
number1 = raw_input("Please give me a number between 50-100? ")#This next set of data collectors will grab some numbers that will be used throughout the code in equations and as stand alone data to create a personal experience and a funny experience at the same time.
number2 = raw_input("What is your favorite number? ")
number3 = raw_input("How many people are there in your immediate family? ")
cond1 = raw_input("Do you like sports? y/n? ")#This collector will give the user an option to say yes or no and depending on what they choose the result in their story will be different. If they choose yes then they will get to travel with their favorite sports team if it is no then they will be traveling with their favorite music group....who doesn't like music right? It is a great fall back choice.
cond2 = raw_input("Do you like apples? y/n?")#This will collect another yes or no question, if the user selects yes then they will get some great apples as a prize for completing the competition, if they select no then they will get some strawberries, hey after the challenges they will be thanking me for the food, they don't need money.


#---------------Section 2--------------------
#number functions start
#This first function will collect two sets of data(numbers) and multiply them together. It will pull from the numbers that are input in the number1,2 and 3 spot by the user. The int in front of the variables lets the code no that I want those ran through as numbers and not a string. If this is not done it throws off the whole code.
def numberMultiply(a,b):
    times = int(a)*int(b)
    return times
#This second function will collect two sets of data(numbers) and add them together. These numbers are taken in the same way as above and I have used the int to change each input into a number that can be used in the equation.
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
#This section will process the users answer in cond2 and evaluate whether there is a 'y' or a 'Y' to see which results to give. If the response given by the user meets this condition then you will win a bushel of apples. If however it does not detect the y variations then you will get a result of Flats of strawberries.
def prize():
    if cond2 == "y" or cond2 == "Y":
        results = "bushels of apples"
    else:
        results = "flats of strawberries"

    return results
#Conditional statements End

#------------------------Section 5---------------------
#dictionary statement begin
#This variable is going to be used as meal choices for the persons trip. It will just display the value of each key.
meal_options = {"Meat":"Chicken with Rice","Veg":"Toficken with Rice","Vegan":"Water"}
#dictionary statement end

#------------------------Section 6-----------------------
#Story begins here. The \033[1m is the beginning of creating bold text in the terminal window and the \033[0m signals the end of the bold text in the code. Each bold item is what was either input by the user or is a result of the code and not just some words put down for the stories purpose. When writing the print statement I converted the results of my equations back into a string to display them in the story correctly, I also used the string method on the raw numbers put into the story to display correctly.
print "\n"+"\033[1m"+name+"\033[0m"+", your challenge is as follows: \nyou are going to be left on a "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". You will be presented with "+"\033[1m"+str(number1)+"\033[0m"+" challenges and you will have "+"\033[1m"+str(added)+"\033[0m"+" hours to complete these tasks before you. \nYou will be allowed to carry a "+"\033[1m"+kitchen_utensil+"\033[0m"+" with you at all times but nothing more. Just so you know "+"\033[1m"+name+"\033[0m"+", you have made "+"\033[1m"+str(mult)+"\033[0m"+" people very happy today. \nSo for your journey today you will be traveling by way of "+"\033[1m"+favorite_animal+"\033[0m"+" to "+"\033[1m"+verb+"\033[0m"+" island in the middle of "+"\033[1m"+favorite_meal+"\033[0m"+". "+"\033[1m"+name+"\033[0m"+", you should get there in about "+"\033[1m"+str(mult2)+"\033[0m"+" days. We will provide you with a meal in route. Your options are as follows: "+"\033[1m"+meal_options['Meat']+"\033[0m"+", "+"\033[1m"+meal_options['Veg']+"\033[0m"+" or "+"\033[1m"+meal_options['Vegan']+"\033[0m"+". \nDuring your travel you will be accompanied by your favorite "+"\033[1m"+company()+"\033[0m"+". You may also take your friends "+"\033[1m"+friends[0]+"\033[0m"+", "+"\033[1m"+friends[1]+"\033[0m"+" and "+"\033[1m"+friends[2]+"\033[0m"+" along to pass the time until you get to your destination. For the record "+"\033[1m"+name+"\033[0m"+", your friends look a little "+"\033[1m"+adjective+"\033[0m"+" to me, yikes. \nOne more thing before we send you off on your adventure, the stakes. If you do not complete these tasks in "+"\033[1m"+str(added)+"\033[0m"+" hours you will go home with "+"\033[1m"+str(mult2)+"\033[0m"+" flaming "+"\033[1m"+adjective+"\033[0m"+" chillies!! However, if you complete the challenge you are going home with "+"\033[1m"+str(number3)+"\033[0m"+" "+"\033[1m"+prize()+"\033[0m"+" for you and your family. Well "+"\033[1m"+name+"\033[0m"+", good luck and it's time for you to head off on your journey. \nFolks let's give "+"\033[1m"+name+"\033[0m"+" a proper countdown: "

#------------------------Section 6.1-----------------------
#Begin the while loop. Counts down from 5 to 1 and places 3 dots after each number.
i=5
while i>0:
    print i,"..."
    i-=1
#End the while loop
#--------------------------Section 6.2------------------------
print "See Ya!!" #This will print the string see ya at the end of the story just after the countdown.
#Story ends here































