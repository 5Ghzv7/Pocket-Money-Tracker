#DONT RUN initialize.py AFTER RUNNING IT ONCE

#Importing datetime module
from datetime import date
today = date.today()

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#User Input
moneyInput = int(input(f"Enter New Money Entry (INR): "))

#Opening initialized.txt
with open("initialized.txt", "r") as iniFile:
    #Reading Old Input
    iniContent = iniFile.read()
    iniContentSplit = iniContent.split() 
iniFile.close() 

#Opening record.txt
with open("record.txt", "a+") as recFile:    
    #The Math
    money = int(iniContentSplit[-1]) + moneyInput
    
    #Logging
    recFile.write(f"{today} >>> Pocket Money: INR {money}\n")
recFile.close()
    
#Updating initialized.txt
with open("initialized.txt", "w") as iniFile2:
    iniFile2.write(f"{today} >>> Pocket Money: INR {money}\n")
iniFile2.close()

#Backup
with open(f"log//Initialized_{today}.log", "a+") as iniFile:
    iniFile.write(f"{current_time} >>> Pocket Money: INR {moneyInput}\n")
iniFile.close()

#Printing Current Value in Console
print(f"Current Pocket Money: INR {money}")

exit()