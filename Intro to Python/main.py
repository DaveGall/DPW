#one line comments
'''
Doc Strings, multiple lines of comments.
'''
#Don't need semicolons in python unless you are putting more than one thing on a single line.
#Style guide: http://legacy.python.org/dev/peps/pep-0008
first_name = "Dave"
last_name = "Gall"
#Python 3.0 uses parenthesis not a space like 2.7
#print first_name

#raw_input collects input as strings.
#response = raw_input("Enter your name  ")
#print "Hello there, ", response

#Expressions

birth_year = 1974
current_year = 2015
age = current_year - birth_year
#print "You are "+str(age)+" years old."
#no increment or decrement in python: e.g. ++ --

#Objects of different type str(var) to change to a string, int(var) to change to a number.
'''
Javascript:
if(condition){
//stuff to do
}
Below is an if statement form in python- no parens or brackets. The indent tells python what is
in the statement.
'''
budget = 10
if budget > 100:
    brand = "Nike"
    print "I can buy some "+brand+"'s"
else:
    print "No cool shoes for me."
