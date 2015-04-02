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
#print number1+" * "+number2+" is: "+str(mult)+". "+number3+" + "+number2+" is: "+str(added)

#End number function variables
#While loop begins
i=5
while i>0:
    print i
    i = i-1
#While loop ends.
#Friends array begins here
friends = [person_name1,person_name2,person_name3]
#print "Your friends "+friends[0]+", "+friends[1]+" and "+friends[2]+", will be joining us for dinner."

#Friends array ends here
#Conditional statements Begin
def company():
    if cond1 == "y" or cond1 == "Y":
        result = "sports team!!"
        print result
    else:
        result = "musical group!!"
        print result

    return result

def prize(cond2):
    if cond2 == "y" or cond2 == "Y":
        results = " bushels of apples "
        print results
    else:
        results = " flats of strawberries "
        print results

    return results
#Conditional statements End
#dictionary statement begin
meal_options = {"Meat":"Chicken with Rice","Veg":"Toficken with Rice","Vegan":"Water"}
#print meal_options["Meat"]+", "+meal_options["Veg"]+" or "+meal_options["Vegan"]
#dictionary statement end



print name+", your challenge is as follows: you are going to be left on a "+verb+" island in the middle of "+favorite_meal+". You will be presented with "+str(number1)+" challenges and you will have "+str(added)+" hours to complete these tasks before you. You will be allowed to carry a "+kitchen_utensil+" with you at all times but nothing more. Just so you know "+name+", you have made "+str(mult)+" people very happy today. So for your jorney today you will be traveling by way of "+favorite_animal+" to "+verb+" island in the middle of "+favorite_meal+". "+name+", you should get there in about "+str(mult)+" days. We will provide you with meal options for your travel meal. They are as follows: "+meal_options['Meat']+", "+meal_options['Veg']+" or "+meal_options['Vegan']+". During your travel you will be accompanied by your favorite "+company()+". "

#+". During your travel you will be accompanied by "+cond1+". You may also take "+friends+" along to pass the time until you get to your destination. For the record "+name+", your friends look a little "+adjective+" to me, yikes. One more thing before we send you off on your adventure, if you do not complete these tasks in "+str(added)+" hours you will still win "+str(mult2)+" flaming "+adjective+" chilies!!  However, if you complete your challenge you are going home with "+number3+" "+cond2+ "for you and your family. Well "+name+" good luck and it is time for you to head off on your journey. Folks let us give "+name+" a proper countdown "+while_loop+", see ya!!"
































