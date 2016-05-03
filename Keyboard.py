##AndroidKeyboard
import getch, os, sys
char = ""
string = ""
letters = { 'q':['w','s','a'],'a':['q', 'w', 's', 'x', 'z'], 'z':['a','s','x',], 'w':['q','a','s','d','e'], 's':['d','e','w','a','z','x'], 'x':['c','d','s','z'], 'e':['r','d','s','w'], 'd':['f','r','e','s','x','c'], 'c':['v','f','d','x'], 'r':['t','f','d','e'], 'f':['g','t','r','d','c','v'], 'v':['b','g','f','c'], 't':['y','g','f','r'], 'g':['h','y','t','f','v','b'], 'b':['n','h','g','v'], 'y':['u','h','g','t'], 'h':['j','u','y','g','b','n'], 'n':['m','j','h','b'], 'u':['i','j','h','y'], 'j':['k','i','u','h','n','m'], 'm':['l','k','j','n'], 'i':['o','l','k','j','u'], 'k':['l','o','i','j','m'], 'o':['p','l','k','i'], 'l':['p','o','k'], 'p':['o','l']}
dict = []
k = 0
newresult = []
count = 0
word = ""

if(sys.argv[1] == 'en.txt'):
	toopen = 'en.txt'
if(sys.argv[1] == 'it.txt'):
	toopen = 'it.txt'

f = open(toopen, 'r')
x = f.readlines()
for i in x:
        dict.append(i[0:len(i) -1])
f.close()



result = dict
os.system("clear")


print(' ')
print("------------------------------------------------------------")
print(' ')
print("------------------------------------------------------------")
print("Words Counter: ", count)




while ((char != '\n')):
	char =  getch.getch()
	if(char == '\n'):
		break
	os.system("clear")
	word += char
	print(string)
	print("------------------------------------------------------------")
	print(word)
	print("------------------------------------------------------------")
	print("Words Counter: ", count)
	for i in (result):
		count += 1
		try:
			if(i[k] == char):
				newresult.append(i)
		except:
			pass
	result = newresult
	newresult = []
	k += 1

	# Error Prediction
	# for i in (result):
	# 	try:
	# 		for j in (letters[char]):
	# 			if(i[k] == j):
	# 				newresult.append(i)
	# 	except:
	# 		pass

	if(char == ' '):
		string += word
		word = ""
		newresult = []
		k = 0
		result = dict
		os.system("clear")
		print(string)
		print("------------------------------------------------------------")
		print(word)
		print("------------------------------------------------------------")
		print("Words Counter: ", count)
	if(len(newresult) < 50):
		for i in (newresult):
			print(i)



	if(len(result) == 1):
		word = result[0]
		word += " "
		string += word
		word = ""
		newresult = []
		k = 0
		result = dict
		os.system("clear")
		print(string)
		print("------------------------------------------------------------")
		print(word)
		print("------------------------------------------------------------")
		print("Words Counter: ", count)
