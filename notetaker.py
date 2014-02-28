#!/usr/bin/python

import time
import os

## Declared vars.
## This is the file it writes the notes to.
filename = "logfile.txt"

## This a the loop var which will keep the loop going
loop = 1

## Enter the loop and continue until loop != 1
while (loop == 1):
 ## Clear the Screen and prompt to enter there text
 os.system('clear')
 str = raw_input("Enter your note QUIT to quit: ")
 
 ## If the input was QUIT then set the loop var to 0
 if (str == "QUIT"):
   loop = 0
 else:
   ## Otherwise pull the current date and build the log string to be written
   ## to the file
   datestamp = time.asctime( time.localtime( time.time( ) ) )
   logstring = datestamp + "\n===\n" + str+ "\n\n"
 
   ## Open and write string to the file and close the file this will ensure that
   ## any writes are not lost should the script be killed unnaturally
   logfile = open(filename, "a+")
   logfile.write(logstring    )
   logfile.close()
 
 
 
 

 
 



