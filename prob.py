import os
bat = open('batting.tsv','r')
bowl = open('bowling.tsv','r')

dbat = {}
dbowl = {}

for i in bat.readlines():
	d = i.split(",")
	for j in d[1:]:
		dbat[j] = d[0]

for i in bowl.readlines():
	d = i.split(",")
	for j in d[1:]:
		dbowl[j] = d[0]

aa = input("Enter name of Batsman : ")
bb = input("Enter name of Bowler : ")
a = dbat[aa]
b = dbowl[bb]



os.chdir('combined')
f = open(str(a)+"_"+str(b), 'r')

a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a6 = 0

tballs = 0

for i in f:
	d = i.split(",")
	if d[3] == '1':
		a1 = a1 + 1
	elif d[3] == '2':
		a2 = a2 + 1
	elif d[3] == '3':
		a3 = a3 + 1
	elif d[3] == '4':
		a4 = a4 + 1
	elif d[3] == '6':
		a6 = a6 + 1
	elif d[3] == '0':
		a0 = a0 + 1
	tballs = tballs +1
print('''Probabilities:
	Scoring 0 : %s
	Scoring 6 : %s
	Scoring 4 : %s
	Scoring 3 : %s
	Scoring 2 : %s
	Scoring 1 : %s
	'''%((float(a0)/tballs),float(a6)/tballs,float(a4)/tballs,float(a3)/tballs,float(a2)/tballs,float(a1)/tballs))
