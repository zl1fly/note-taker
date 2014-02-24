#!/usr/bin/python

import time

## Declared vars.
filename = "logfile.txt"
loop = 1



while (loop == 1):
 str = raw_input("Enter your note Q to quit: ")
 datestamp = time.asctime( time.localtime( time.time( ) ) )
 logstring = datestamp + "\n===\n" + str+ "\n\n"
 
 #Open and write string to the file and close the file
 logfile = open(filename, "a+")
 logfile.write(logstring    )
 logfile.close()
 
 
 

 
 



