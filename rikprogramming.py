__doc__="Just a simple, stupid and a dummy toy programming Language"
__version__='2.2'
#this is the souce code of rik programming language
#this is the one
def read(files):
	data=open(files,"r").read()
	return data

	
def wsdelete(files):
	#this was for experiment to actually figure out how to exclude stuffs from string, cuz in the later part I took
	#inspirations from it to code the lexer
	lul=''
	b=0
	for cha in list(files):
		if cha=='\'' or cha=='\"':
			b+=1
		elif cha==' ' or cha=='\t':
			if b%2==0 or b==0:
				cha=''
			else:
				cha=' '
		lul+=cha
	return lul

def lex(files):
	#we gotta make sure that we don't identify something as a token which is inside a freaking string so yah
	#it will provide tokens to known functions like print, ninput, sinput and idk what else
	#no eol required, but for parsing, its required
	hidrepoka=[]
	files+=' '
	n=-1
	b=0
	data=''
	range='.0123456789()'
	var=0
	for cha in files:
		n+=1
		if cha=='\'' or cha=='\"':
			if files[n-1]!='\\':
				b+=1
				if b%2==0:
					data+='}'
					data=data.replace('\\\'','\'')
					data=data.replace('\\n','\n')
					data=data.replace('\\t','\t')
					data=data.replace('\\\"','\"')
					hidrepoka.append(data)
					data=''
				else:
					data+='{STRING:'
			else:

				data+=cha
		elif b%2!=0:
			data+=cha
		elif cha=='p' and files[n+1]=='r' and files[n+2]=='i' and files[n+3]=='n' and files[n+4]=='t':
			if b%2==0 or b==0:
				data+='{print}'
				hidrepoka.append(data)
				data=''
		elif cha=='n' and files[n+1]=='i' and files[n+2]=='n' and files[n+3]=='p' and files[n+4]=='u' and files[n+5]=='t':
			if b%2==0 or b==0:
				data+='{ninput}'
				hidrepoka.append(data)
				data=''
		elif cha=='s' and files[n+1]=='i' and files[n+2]=='n' and files[n+3]=='p' and files[n+4]=='u' and files[n+5]=='t':
			if b%2==0 or b==0:
				data+='{sinput}'
				hidrepoka.append(data)
				data=''
		elif cha=='i' and files[n+1]=='f' and files[n-1]!='l':
			if b%2==0 or b==0:
				data+='{if}'
				hidrepoka.append(data)
				data=''
		elif cha=='e' and files[n+1]=='l' and files[n+2]=='s' and files[n+3]=='e':
			if b%2==0 or b==0:
				data+='{else}'
				hidrepoka.append(data)
				data=''
		elif cha=='e' and files[n+1]=='l' and files[n+2]=='i' and files[n+3]=='f':
			if b%2==0 or b==0:
				data+='{elif}'
				hidrepoka.append(data)
				data=''
		elif cha=='f' and files[n+1]=='o' and files[n+2]=='r':
			if b%2==0 or b==0:
				data+='{for}'
				hidrepoka.append(data)
				data=''
		elif cha=='w' and files[n+1]=='h' and files[n+2]=='i' and files[n+3]=='l' and files[n+4]=='e':
			if b%2==0 or b==0:
				data+='{while}'
				hidrepoka.append(data)
				data=''
		elif cha=='d' and files[n+1]=='e' and files[n+2]=='f':
			if b%2==0 or b==0:
				data+='{def}'
				hidrepoka.append(data)
				data=''
		elif cha=='r' and files[n+1]=='e' and files[n+2]=='t' and files[n+3]=='u' and files[n+4]=='r' and files[n+5]=='n':
			if b%2==0 or b==0:
				data+='{return}'
				hidrepoka.append(data)
				data=''
		elif cha=='e' and files[n+1]=='n' and files[n+2]=='d':
			if b%2==0 or b==0:
				data+='{end}'
				hidrepoka.append(data)
				data=''
		elif cha==':':
			if b%2==0 or b==0:
				data+='{start}'
				hidrepoka.append(data)
				data=''
		elif cha=='=':
			if files[n+1]=='=':
				data+='{==}'
				hidrepoka.append(data)
				data=''
			elif files[n-1]=='!':
				data+='{!=}'
				hidrepoka.append(data)
				data=''
			elif files[n-1]!='=':
				data+='{=}'
				hidrepoka.append(data)
				data=''
		elif b%2!=0:
			data+=cha
		elif cha in range:
			if files[n-1] in range and files[n+1] not in range:
				data+=cha
				data+='}'
				hidrepoka.append(data)
				data=''
			elif files[n+1] in range and files[n-1] not in range:
				data+='{EXPR:'
				data+=cha
			elif files[n+1] not in range and files[n-1] not in range:
				data+='{EXPR:'
				data+=cha
				data+='}'
				hidrepoka.append(data)
				data=''
			elif files[n-1] in range and files[n+1] in range:
				data+=cha
		elif cha=='+':
			if b%2==0 or b==0:
				data+='{+}'
				hidrepoka.append(data)
				data=''
		elif cha=='*':
			if b%2==0 or b==0:
				data+='{*}'
				hidrepoka.append(data)
				data=''
		elif cha=='-':
			if b%2==0 or b==0:
				data+='{-}'
				hidrepoka.append(data)
				data=''
		elif cha=='/':
			if b%2==0 or b==0:
				data+='{/}'
				hidrepoka.append(data)
				data=''

		elif cha=='%':
			if b%2==0 or b==0:
				data+='{%}'
				hidrepoka.append(data)
				data=''
		elif cha=='=' and files[n+1]=='=':
			if b%2==0 or b==0:
				data+='{==}'
				hidrepoka.append(data)
				data=''

		elif cha=='|' and files[n+1]=='|':
			if b%2==0 or b==0:
				data+='{||}'
				hidrepoka.append(data)
				data=''
		elif cha=='&' and files[n+1]=='&':
			if b%2==0 or b==0:
				data+='{&&}'
				hidrepoka.append(data)
				data=''
		elif cha==';' or cha=='\n':
			if b%2==0 or b==0:
				data+='{EOL}'
				hidrepoka.append(data)
				data=''
		elif cha=='F' and files[n+1]=='a' and files[n+2]=='l' and files[n+3]=='s' and files[n+4]=='e':
			if b%2==0 or b==0:
				data+='{BOOL:False}'
				hidrepoka.append(data)
				data=''
		elif cha=='T' and files[n+1]=='r' and files[n+2]=='u' and files[n+3]=='e':
			if b%2==0 or b==0:
				data+='{BOOL:True}'
				hidrepoka.append(data)
				data=''
		elif cha=='=':
			if files[n-1]!='!' or files[n-1]!='=':
				if b%2==0 or b==0:
					data+='{=}'
					hidrepoka.append(data)
					data=''
		elif cha=='{' and files[n-1]=='$':
			if b%2==0 or b==0:
				var+=1
				data+='{VAR:'
		elif cha=='}':
			if b%2==0 or b==0:
				data+='}'
				hidrepoka.append(data)
				data=''
				var=0
		elif var!=0:
			data+=cha

	return hidrepoka

def parse(bun,var={}):
	files=bun#############gotta fix this split function OMG SO MUCH HEADACHE CLEARLY THIS THING IS GETTING MESSY
	original=files
	data=''
	tree=1
	bambam=0
	n=-1
	hu=0
	uuu=0
	wheel=[]
	b=0
	c=len(files)
	fiat=None
	op=''
	func=''
	math=''
	m=None
	tags=['{elif}','{else}']
	keywords=['{print}','{ninput}','{sinput}','{if}','{else}','{for}','{while}']
	#parsing is hard, parsing is something that ate my brains
	for cha in files:
		n+=1
		if cha=='{+}' and bambam==0:
			if files[n-1][0:8]=='{STRING:' and files[n+1][0:8]=='{STRING:' and files[n+2]=='{+}':
				op+=files[n-1][8:len(files[n-1])-1]
			elif files[n-1][0:8]=='{STRING:' and files[n+1][0:8]=='{STRING:' and files[n+2]!='{+}':
				op+=files[n-1][8:len(files[n-1])-1]
				op+=files[n+1][8:len(files[n+1])-1]
			##########numerical functions needed##########
			#######doing it using the eval function#######
			elif files[n-1][0:6]=='{EXPR:' and files[n+1][0:6]=='{EXPR:':
				if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
					math+='+'+files[n+1][6:len(files[n+1])-1]
				else:
					math+=files[n-1][6:len(files[n-1])-1]+'+'+files[n+1][6:len(files[n+1])-1]
				######################variable functions######################################
			elif files[n-1][0:6]=='{EXPR:' and files[n+1][0:5]=='{VAR:':
				if var[files[n+1]][0:6]=='{EXPR:':
					if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
						math+='+'+var[files[n+1]][6:len(var[files[n+1]])-1]
					else:
						math+=files[n-1][6:len(files[n-1])-1]+'+'+var[files[n+1]][6:len(var[files[n+1]])-1]
		elif cha=='{-}' and bambam==0:
			if files[n-1][0:6]=='{EXPR:' and files[n+1][0:6]=='{EXPR:':
				if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
					math+='-'+files[n+1][6:len(files[n+1])-1]
				else:
					math+=files[n-1][6:len(files[n-1])-1]+'-'+files[n+1][6:len(files[n+1])-1]


			######################variable functions######################################
			elif files[n-1][0:6]=='{EXPR:' and files[n+1][0:5]=='{VAR:':
				if var[files[n+1]][0:6]=='{EXPR:':
					if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
						math+='-'+var[files[n+1]][6:len(var[files[n+1]])-1]
					else:
						math+=files[n-1][6:len(files[n-1])-1]+'-'+var[files[n+1]][6:len(var[files[n+1]])-1]

		elif cha=='{*}' and bambam==0:
			if files[n-1][0:6]=='{EXPR:' and files[n+1][0:6]=='{EXPR:':
				if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
					math+='*'+files[n+1][6:len(files[n+1])-1]
				else:
					math+=files[n-1][6:len(files[n-1])-1]+'*'+files[n+1][6:len(files[n+1])-1]


				######################variable functions######################################
			elif files[n-1][0:6]=='{EXPR:' and files[n+1][0:5]=='{VAR:':
				if var[files[n+1]][0:6]=='{EXPR:':
					if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
						math+='*'+var[files[n+1]][6:len(var[files[n+1]])-1]
					else:
						math+=files[n-1][6:len(files[n-1])-1]+'*'+var[files[n+1]][6:len(var[files[n+1]])-1]
		elif cha=='{/}' and bambam==0:
			if files[n-1][0:6]=='{EXPR:' and files[n+1][0:6]=='{EXPR:':
				if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
					math+='/'+files[n+1][6:len(files[n+1])-1]
				else:
					math+=files[n-1][6:len(files[n-1])-1]+'/'+files[n+1][6:len(files[n+1])-1]


				######################variable functions######################################
			elif files[n-1][0:6]=='{EXPR:' and files[n+1][0:5]=='{VAR:':
				if var[files[n+1]][0:6]=='{EXPR:':
					if files[n-2]=='{+}' or files[n-2]=='{-}' or files[n-2]=='{*}' or files[n-2]=='{/}':
						math+='/'+var[files[n+1]][6:len(var[files[n+1]])-1]
					else:
						math+=files[n-1][6:len(files[n-1])-1]+'/'+var[files[n+1]][6:len(var[files[n+1]])-1]
		elif cha=='{print}' and bambam==0:
			func='print'
		elif cha=='{EOL}' and bambam==0:
			if func=='print':
				if op!='':
					print op
					func=''
					op=''
				elif math!='':
					print eval(math)
					math=''
					func=''
				elif files[n-1][0:8]=='{STRING:':
					print files[n-1][8:len(files[n-1])-1]
					func=''
				elif files[n-1][0:6]=='{EXPR:':
					print files[n-1][6:len(files[n-1])-1]
					func=''
				elif files[n-1]=='{BOOL:True}':
					print "True"
				elif files[n-1]=='{BOOL:False}':
					print "False"	
				elif files[n-1][0:5]=='{VAR:':
					if var[files[n-1]][0:6]=='{EXPR:':
						print var[files[n-1]][6:len(files[n-1])-1]
					elif var[files[n-1]][0:8]=='{STRING:':
						print var[files[n-1]][8:len(files[n-1])-1]
					elif var[files[n-1]]=='{BOOL:True}':
						print "True"
					elif var[files[n-1]]=='{BOOL:False}':
						print "False"

			elif func[0:5]=='{VAR:' and bambam==0:
				if op!='':
					var[func]=op
					func=''
					op=''
				elif math!='':
					var[func]='{EXPR:'+str(eval(math))+'}'
					func=''
					math=''
				elif op=='' and math=='':
					var[func]=files[n-1]
					func=''
			else:
				if files[n-1]!="{EOL}" and files[n-1]!="{end}":
					print files[n-1] #only for shell, comment this out during compiling mode

		elif cha[0:5]=='{VAR:' and bambam==0:

			if files[n+1]=='{=}':
				if files[n+2]=='{ninput}':
					#do stuff
					var[cha]='{EXPR:'+str(input())+'}'
				elif files[n+2]=='{sinput}':
					#do stuff
					var[cha]='{STRING:'+raw_input()+'}'
				else:
					func=cha
			elif files[n+1]!='{=}':
				files[n]=var[cha]

		elif cha=='{while}' and bambam==0:
			hu=n
			uuu=n
			hydra=n
			while files[uuu]!='{start}':
				uuu+=1

			wheel=files[hu+1:uuu]

			n=uuu
			#wheel contains the boolean statements
			while tree!=0:

				uuu+=1
				if files[uuu]=='{start}':
					tree+=1
				elif files[uuu]=='{end}':
					tree+= -1
			mamma=files[n+1:uuu]
			dada=original[n+1:uuu]
			dada2=dada
			while boom(wheel,var):
				var=fi(mamma,var)
				mamma=original[n+1:uuu]

			n=hydra
			tree=1
		elif cha=='{start}':
			func=''
			math=''
			op=''
			bambam+=1

		elif cha=='{end}':
			bambam-=1

		elif cha=='{if}' and bambam==0:
			hu=n
			uuu=n
			hydra=n
			while files[uuu]!='{start}':
				uuu+=1

			wheel=files[hu+1:uuu]

			if boom(wheel,var)==True:
				fiat=True
			else:
				fiat=False
			if fiat==True:
				n=uuu
				while tree!=0:

					uuu+=1
					if files[uuu]=='{start}':
						tree+=1
					elif files[uuu]=='{end}':
						tree+= -1
				mamma=files[n+1:uuu]
				fi(mamma,var)
			n=hydra
			tree=1
		elif cha=='{elif}' and bambam==0:
			if fiat==False:
				hu=n
				uuu=n
				hydra=n
				while files[uuu]!='{start}':
					uuu+=1

				wheel=files[hu+1:uuu]

				if boom(wheel,var)==True:
					fiat=True
				else:
					fiat=False
				if fiat==True:
					n=uuu
					while tree!=0:

						uuu+=1
						if files[uuu]=='{start}':
							tree+=1
						elif files[uuu]=='{end}':
							tree+= -1
					mamma=files[n+1:uuu]
					fi(mamma,var)
				n=hydra
				tree=1
		elif cha=='{else}' and bambam==0:
			if fiat==False:
				hu=n
				uuu=n
				hydra=n
				while files[uuu]!='{start}':
					uuu+=1

				wheel=files[hu+1:uuu]


				n=uuu
				while tree!=0:

					uuu+=1
					if files[uuu]=='{start}':
						tree+=1
					elif files[uuu]=='{end}':
						tree+= -1
				mamma=files[n+1:uuu]
				fi(mamma,var)
			n=hydra
			tree=1

	return var


#def run(hidre):    #this is like from version one
	#greetings=lex(hidre)
	#parse(greetings)
	
def run(hidre):
	parse(lex(commentor(hidre+'\n')))

def boom(bloo,var={}):
	n=-1
	bol=''
	for cha in bloo:
		n+=1
		if cha[0:8]=='{STRING:':
			bol+=' \''+cha[8:len(cha)-1]+'\''
		elif cha=='{==}':
			bol+='== '
		elif cha=='{BOOL:True}':
			bol+='True '
		elif cha=='{BOOL:False}':
			bol+='False '
		elif cha=='{!=}':
			bol+='!= '
		elif cha=='{&&}':
			bol+='and'+' '
		elif cha[0:6]=='{EXPR:':
			bol+=cha[6:len(cha)-1]+' '
		elif cha[0:5]=='{VAR:':
			if var[cha][0:8]=='{STRING:':
				bol+=' \''+var[cha][8:len(var[cha])-1]+'\''+' '
			elif var[cha][0:6]=='{EXPR:':
				bol+=var[cha][6:len(var[cha])-1]+' '
	#print bol
	bun=eval(bol)
	if bun==True:
		return True
	else:
		return False


def fi(x,var={}):
	trill=parse(x,var)
	return trill

def commentor(code):
	n=-1
	b=0
	var=0
	final=''
	for cha in code:
		n+=1
		if cha=="\"" or cha=="\'":
			if code[n-1]!="\\":
				b+=1
		if b%2==0 and cha=='#':
			var+=1
		elif b%2==0 and cha=='\n':
			var+=1
		if var%2==0 or cha=='\n':
			final+=cha
	return final
