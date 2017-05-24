just transferred this repo to my real account "hrik2001"



Rik Programming Language
---
This is just a dummy programming language which was and is being being developed by Rik. Lemme be honest, this is not the proper way an interpreter should be written. I just experimented around and I found my own way.</br>
How does this work though?</br>
Suppose I have a code, "print 'hello world';", first I will put the string in a function which I have defined in `rikprogramming.py`. Its the lex function. `lex("print 'hello world';")` will give me `['{print},{STRING:hello world},{EOL}]` . Then I have to feed this list (or array) in the parse function. I think parsing means something else but here it just evaluates and executes the tokenized (or lexed) code.

Synopsis
---
Its just a programming language which i developed just for fun. i was bored and when boredom strikes an idea strikes too. you can kind of consider this a full fledged language except that you cannot write functions and import or include headers or modules, but i will add those features later. I will probably even make this language object oriented

Motivation
---
No motivation at all lol, i was lazy and i was developing it as a part of a bigger project, then this branched out and now i am developing it

Usage
---
a sample script
```
 #this is a comment
 ${a}=12
 print ${a} #will print out 12
 ${a}="i am dynamic,since i am string now" 
 print ${a} #will print the string
 
 if 1==1:
  print 12 #indention is not needed though
 end
 
 if 2==2:
 print 1
 end
 elif 1==2:
 print 0
 end
 else:
 print 12
 end
 while 1:
 print 1
  
  while True: #u can write True instead of 1 too
   print 2
   end
```
But while you are in the shell, where you cannot break your code into multiple lines, you gotta type stuff like this - 
```
while 1 : print 1 ; print 2 ; end     # will print 1\n2
```
Credits
---
i actually made it without any help so no references and thank yous but i will thank Python for their language and their eval() for boolean logics and PEMDAS. i will code a logical function myself later to be completely indepenedent.

Feedbacks
---
they are welcome.

Contact
---
rik61072@gmail.com
