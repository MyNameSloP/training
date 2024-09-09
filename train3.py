import os               # System module
import shutil           # Copy module
import messages as msg                          # import defs from other files, the module can be use as "msg"
from messages import hello,bye                  # you can import all with "*" but it's not recommanded (names conflict)
#help("modules")                                # will list all the modules already available

# file detection

path = "C:\\Users\\Utilisateur\\Desktop\\folder"  # To get a file's path right click > property > ctrl c and need to put \\ instead of \ (escape sequence)

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):                     # Will check if the path lead to a file (text for example)
        print("That is a file")
    elif os.path.isdir(path):                    # Will check if the path lead to a directory (folder)
        print("That is a directory")
else:
    print("That location doesn't exist")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# read a file

try:
    with open("C:\\Users\\Utilisateur\\Desktop\\test.txt","r") as monTexte:          # Will open the file led by the path as a variable you can call whatever you want
        print(monTexte.read())                                                       # "r" means that we will read it
except FileNotFoundError:
    print("That file wasn't found")


print(monTexte.closed)                                                       # Will tell you wheter a file is open or not, they close automaticaly with "with open"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# write and append a file

text = "Yoooooooooooo\nThis is some written text\n"              # "\n" will go the next line. If this text was something else it would overwrite the current file
text1 = "This was appened"

with open("C:\\Users\\Utilisateur\\Desktop\\test.txt","a") as monTexte1:                  # "w" means that we will write on it
    monTexte1.write(text1)                                                                # "a" means that we will append something on it
    
 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# copyfile() =      copies contents of a file
# copy() =          copyfile() + permission mode + destination can be a directory
# copy2() =         copy() + copies metadata (file's creation and modification times)

#shutil.copyfile("C:\\Users\\Utilisateur\\Desktop\\test.txt","C:\\Users\\Utilisateur\\Desktop\\testcopy.txt")            #source, destination
# the code would be the same with copy and copy2 just need to fill it instead of copyfile

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

source = "C:\\Users\\Utilisateur\\Desktop\\testcopy.txt"
destination = "C:\\Users\\Utilisateur\\Desktop\\Python VS Code\\testcopy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)                      # works with files as well as folders
        print(source+" was moved to "+destination)

except FileNotFoundError:
    print(source+" was not found")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# delete a file

path2 = "C:\\Users\\Utilisateur\\Desktop\\Python VS Code\\testcopy.txt"
path3 = "C:\\Users\\Utilisateur\\Desktop\\Python VS Code\\empty_folder"

try:
    os.remove(path2)                                    # delete a file
    os.rmdir(path3)                                     # delete directory because we won't have the permission to do it with os.remove
    #shutil.rmtree()                                    will delete a folder that contains files {Dangerous}
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts.

msg.hello()
msg.bye()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Python Object Oriented Programming (OOP)
# A class can function as a blueprint to create objects we can assign attributes and methods 

class Car:                  # Can be imported from another file : "from ... import ..."

    def __init__(self,make,model,year,color):     # = parameters, dont need to put something for self it's automatic 
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):        # self refers to the object this is using this method
        print("This"+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

car_1 = Car("Chevy","Corvette",2021,"Blue")
car_2 = Car("Ford","Mustang",2022,"Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

