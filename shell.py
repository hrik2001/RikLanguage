'''
The shell of the RIK programming language, supposed to be in the same folder of the source code.
'''
from rikprogramming import *
import rikprogramming
import sys
 
def shell():
	print "Rik Shell (REPL) V2.1 BETA, Written by  \n Type help for help, author and about to know about this project"
	about='this is just a toy language built by Rik ( ). Just for leisure. '
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
			print " \'Rik\' "
		elif r=='about':
			print about
		elif r=='help':
			print helps
		elif r=='open file' or r=='run file':
			a=raw_input('enter da file name')
			b=open(a,'r').read()
			rikprogramming.run(b)
			reload(rikprogramming)

		else:
			try:
			 	run(r+'\n')
		 	except:
		 	 	print "something went wrong, please ensure you code is correct"

try:
	rikprogramming.run(open(sys.argv[1],"r").read())
except:
	shell()
