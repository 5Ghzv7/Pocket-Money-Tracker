#RUN THIS SCRIPT ONLY ONCE!!!

#Importing datetime & Time module
from datetime import date
today = date.today()

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#User Input
print("#RUN THIS SCRIPT ONLY ONCE!!!\n")
moneyInput = int(input(f"Enter New Money Entry (INR): "))

#Logging
with open("initialized.txt", "w+") as recFile:
    recFile.write(f"{today} >>> Intialized Pocket Money: INR {moneyInput}\n")
recFile.close()
    
#Backup
with open(f"log//Initialized_{today}.log", "a+") as iniFile:
    iniFile.write(f"{current_time} >>> Intialized Pocket Money: INR {moneyInput}\n")
iniFile.close()

exit()