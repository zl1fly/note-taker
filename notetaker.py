#!/usr/bin/python

import time
import os

## Declared vars.
filename = "logfile.txt"
loop = 1



while (loop == 1):
 os.system('clear')
 str = raw_input("Enter your note QUIT to quit: ")
 if (str == "QUIT"):
   loop = 0
 else:
   datestamp = time.asctime( time.localtime( time.time( ) ) )
   logstring = datestamp + "\n===\n" + str+ "\n\n"
 
   #Open and write string to the file and close the file
   logfile = open(filename, "a+")
   logfile.write(logstring    )
   logfile.close()
 
 
 
 

 
 



