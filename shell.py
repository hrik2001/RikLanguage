'''
The shell of the RIK programming language, supposed to be in the same folder of the source code.
'''
from rikprogramming import *
import rikprogramming
import sys
 
def shell():
	sys.stdout.write( "Rik Shell (REPL) V2.1 BETA, Written by Shatabarto Bhattacharya\n Type help for help, author and about to know about this project\n")
	about='this is just a toy language built by Rik (Shatabarto Bhattacharya). Just for leisure. '
	data=''
	helps="press ^C to escape from a loop and ^D to quit"
	while 1:
		try:
		 r=raw_input(">")
		except:
		 quit() 
		if r=='quit':
			break
		elif r=='author':
			sys.stdout.write( "Shatabarto \'Rik\' Bhattacharya\n")
		elif r=='about':
			sys.stdout.write( about+'\n')
		elif r=='help':
			sys.stdout.write( helps+'\n')
		elif r=='open file' or r=='run file':
			a=raw_input('enter da file name')
			b=open(a,'r').read()
			rikprogramming.run(b)
			reload(rikprogramming)

		else:
			try:
			 	special(r+'\n')
		 	except:
		 	 	sys.stdout.write( "something went wrong, please ensure you code is correct")

try:
	rikprogramming.run(open(sys.argv[1],"r").read())
except:
	shell()
