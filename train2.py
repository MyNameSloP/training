import random

# function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("Louis","ALexis",15) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are know as the functions's return value.

def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)
print(x)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# keyword arguments = arguments preceded by an identifier when we pass them to a function.
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives.

def hello1(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello1(last="Loulou",middle="Louis",first="Alexis") # by telling at which position they are we don't have to respect the order, else it would be 123 instead of 321

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

#num = input("Enter a whole positive number")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

cat = "Minou"  # global scope (available inside and outside functions)

def display_name():
    cat = "Goyave"      # local scope (available only inside this function)
    print(cat)

# Will use the local version before the global if it is defined
#   The order is :
#
#   L = Local 
#   E = Enclosing
#   G = Global
#   B = Built-in

display_name()
print(cat)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#         We can name it whatever we want but we just need to keep the asterisk (*) before

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword arguments
#            We can name it whatever we want but we just need to keep the asterisks (**) before

def hello(**names):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key,value in names.items():
        print(value, end=" ")

hello(title ="Mr.",first="Louis",middle="Pierre",last="Alexis")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# str.format() = optional method that gives users more control when displaying output

animal1 = "cow"
planet1 = "moon"

print("The "+animal1+" jumped over the "+planet1)
print("The {} jumped over the {}".format(animal1,planet1))                           # or "cow","moon"
print("The {1} jumped over the {0}".format(animal1,planet1))                         # positional argument ( will use the index instead of order), can put the same number
print("The {animal} jumped over the {animal}".format(animal="cow",planet="moon"))    # keyword argument, can put the same kwargs

text = "The {} jumped over the {}"
print(text.format(animal1,planet1))

dog = "Rantanplan"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# padding

print("Hello, my dog's name is {}".format(dog))
print("Hello, my dog's name is {:20}. Care, he bites sometimes".format(dog))      # You can put padding with ":" and the number of space you want after
print("Hello, my dog's name is {:<20}. Care, he bites sometimes".format(dog))     # To left-align in the padding do <
print("Hello, my dog's name is {:>20}. Care, he bites sometimes".format(dog))     # To right-align in the padding do >
print("Hello, my dog's name is {:^20}. Care, he bites sometimes".format(dog))     # To center-align in the padding do ^
print("Hello, my dog's name is {0:20}. Care, he bites sometimes".format(dog))     # If you need to put kwargs or positional args do it before colon

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# representation

pii = 3.14159
number10 = 1000

print("The number pi is {:.2f}".format(pii))    # Will only display the first two digits after the decimal and it round the number
print("The number is {:,}".format(number10))    # Will display a comma at the end of the number
print("The number is {:b}".format(number10))    # Will display the value in a binary representation
print("The number is {:o}".format(number10))    # Will display the value in an octal representation
print("The number is {:x}".format(number10))    # Will display the value in hexadecimal representation with lowercase
print("The number is {:X}".format(number10))    # Will display the value in hexadecimal representation with uppercase
print("The number is {:e}".format(number10))    # Will display the value in scientific notation with lowercase
print("The number is {:E}".format(number10))    # Will display the value in scientific notation with uppercase

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pseudo-random number

x1 = random.randint(1,6)
y1 = random.random()                     # random number between 0 and 1

myList = ["rock","paper","scissors"]
z1 = random.choice(myList)               # random choice from the list

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(x1)
print(y1)
print(z1)
print(cards)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# exception =       events detected during execution that interrupt the flow of a program

try:                                                 # Used to try a part of the code, so we can catch exception and write them then
    numerator = int(input("Enter a number to divide"))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:                       # To get the type of exeption watch the console
    print(e)                                         # "e" will display the error that occured
    print("You can't divide by zero!")
except ValueError as e:                              # To get the type of exeption watch the console
    print(e)
    print("Enter only numbers")
except Exception as e:                               # Will aply itself for all kind of exception that weren't defined on top of it
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:                                             # Whether or not we catch an exception will launch the code behind after
    print("This will always execute")