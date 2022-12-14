#Importing modules
from datetime import date
today = date.today()

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

import os
import sys

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

#Important Initialization
ini1RunFileLoc = os.path.join(app_path, r"pref\config.txt")
with open(ini1RunFileLoc, "r+") as ini1Run:
    ini1RunContent = ini1Run.read()
    
    if ini1RunContent == "ini1Run = True":
        print("Initial Money Entry (INR): ")
        moneyInput__ = int(sys.stdin.readline())

        #Logging
        recFileLoc__ = os.path.join(app_path, "pref\\initialized.txt")
        with open(recFileLoc__, "w+") as recFile__0:
            recFile__0.write(f"{today} >>> Intialized Pocket Money: INR {moneyInput__}\n")
        recFile__0.close()
            
        #Backup
        iniFileLoc__ = os.path.join(app_path, fr"log\Initialized_{today}.log")
        with open(iniFileLoc__, "a+") as iniFile__0:
            iniFile__0.write(f"{current_time} >>> Intialized Pocket Money: INR {moneyInput__}\n")
        iniFile__0.close()
ini1Run.close()
with open(ini1RunFileLoc, "w") as ini1Run__:
    #Changing to False
    ini1Run__.write("ini1Run = False")
ini1Run__.close()
        
#Opening initialized.txt
iniFileLoc = os.path.join(app_path, r"pref\initialized.txt")
with open(iniFileLoc, "r") as iniFile:
    #Reading Old Input
    iniContent = iniFile.read()
    iniContentSplit = iniContent.split() 
iniFile.close() 

#User Input
print("Enter New Money Entry (INR): ")
moneyInput = int(sys.stdin.readline())
#The Math
money = int(iniContentSplit[-1]) + moneyInput

#Opening record.txt
recFileLoc = os.path.join(app_path, r"pref\record.txt")
with open(recFileLoc, "a+") as recFile:
    recFile.write(f"{today} >>> Pocket Money: INR {money}\n")
recFile.close()
    
#Updating initialized.txt
with open(iniFileLoc, "w") as iniFile2:
    iniFile2.write(f"{today} >>> Pocket Money: INR {money}\n")
iniFile2.close()

#Backup
iniFileLogLoc = os.path.join(app_path, fr"log\Initialized_{today}.log")
with open(iniFileLogLoc, "a+") as iniFile:
    iniFile.write(f"{current_time} >>> Pocket Money: INR {money}\n")
iniFile.close()

#Printing Current Value in Console
print(f"Current Pocket Money: INR {money}")

#Stopping script from closing immediately
os.system("pause")