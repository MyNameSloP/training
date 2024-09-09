import math
import time

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pi = 3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(max(pi,5))
print(min(pi,5))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice ()
#           [start:stop:step] with numbers ( L = 0 )
#           step = saut, 2 = saut de 2 par 2 caractères en commençant par le premier

name = "Louis ALEXIS"

firstname = name[0:5] # = name[:5]
lastname = name[6:12] # = name[6:]
funkyname = name[0:12:2] # = name[::2]
reversedname = name[::-1]

print(firstname)
print(lastname)
print(funkyname)
print(reversedname)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # compter en positif pour le start à gauche et en négatif pour le stop à droite
print(website1[slice])
print(website2[slice])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#logical operators (and, or, not) = used to check if two or more conditional statements is true
#"not" is gonna inverse the condition, but need to put:  not(condition)

temp = 23

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name1 = ""  # name1 = None

while len(name1) == 0: # = while not name:
    name1 = input("Enter your name: ")

print("Hello "+name1)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# for loop = a statement that will execute its block of code a limited amount of times


for i in range(50,101,2): # i va faire de 50 à 100 de 2 en 2
    print(i)

for j in "Louis Alexis":
    print(j)

for seconds in range(10,0,-1): # seconds va faire de 10 à 0 de -1 en -1
    print(seconds)
    time.sleep(0.2)

print("Happy New Year !")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#nested loops =     The "inner loop" will finish all of its interactions before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for k in range(rows):
    for l in range(columns):
        print(symbol, end="") # end="" will prevent our cursor from returning to the next line
    print()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

while True:
    name3 = str(input("Enter your name: "))
    if name3 != "": # si différent de rien
        break

phone_number = "123-456-7890"

for m in phone_number:
    if m =="-":
        continue
    print(m,end="")
print()

for w in range(1,21):

    if w == 13:
        pass
    else:
        print(w)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti"]

food[0] = "sushi"

food.append("ice cream")    # will add at the end of the list
food.remove("spaghetti")    # will remove whatever you want, put the thing directly 
food.pop()                  # will remove the last item
food.insert(0,"cake")       # will add an item wherever you want
food.sort()                 # will sort the list (trier) par collection
#food.clear()                 will clear the list


for c in food:
    print(c," ", end="")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2D lists = a list of lists 

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

foood = [drinks,dinner,dessert]

print(foood)
print(foood[0])         # will show the first list of foood
print(foood[0][0])      # will show the first item of the first list

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for v in student:
    print(v)

if "Bro" in student:
    print("Bro is here!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.update(dishes)  #will add all elements in dishes to utensils
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))      # What does utensils has that dishes doesn't ?
print(utensils.intersection(dishes))    # What does utensils and dishes have in common ? 

for b in dinner_table:
    print(b)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"Usa":"Las Vegas"})
capitals.pop("China")               # will remove a key and its value from the dictionnary
#capitals.clear()

print(capitals["Russia"])           # will print the value assiocied
print(capitals.get("Germany"))      # will get the value of a key, if it's not associed, it will put None
print(capitals.keys())              # will print only the keys
print(capitals.values())            # will print only the values
print(capitals.items())             # will print the whole dictionnary

for key,value in capitals.items():
    print(key, value)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# index operator [] = gives access to a sequence's element (str, list, tuples)

nam = "louis Alexis"

if(nam[0].islower()):
    nam = nam.capitalize()

first_nam = nam[:5].upper()
last_nam  = nam[6:].lower()
last_character = nam[-1]        # Si négatif, compter à l'envers donc s;i;x pour -1,-2,-3

print(nam) 
print(first_nam)
print(last_nam)
print(last_character)