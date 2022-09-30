#RUN THIS SCRIPT ONLY ONCE!!!

#Importing Modules
from datetime import date
today = date.today()

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

import os

#User Input
print("#RUN THIS SCRIPT ONLY ONCE!!!\n")
moneyInput = int(input(f"Enter New Money Entry (INR): "))

#Logging
recFileLoc = os.path.join(os.getcwd(), "initialized.txt")
with open(recFileLoc, "w+") as recFile:
    recFile.write(f"{today} >>> Intialized Pocket Money: INR {moneyInput}\n")
recFile.close()
    
#Backup
iniFileLoc = os.path.join(os.getcwd(), f"log\\Initialized_{today}.log")
with open(iniFileLoc, "a+") as iniFile:
    iniFile.write(f"{current_time} >>> Intialized Pocket Money: INR {moneyInput}\n")
iniFile.close()

exit()