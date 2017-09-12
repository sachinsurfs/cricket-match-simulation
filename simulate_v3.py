import sys
import os
import yaml
import subprocess as sp
import time
import random

fff = raw_input("Enter Match dataset : ")

bat = open('./IPLBatCluster.tsv','r')
bowl = open('./IPLBowlCluster.tsv','r')

i1_batsman_runs = dict()
i2_batsman_runs = dict()
dbat = {}
dbowl = {}

for i in bat.readlines():
	d = i.split(",")
	for i in d[1:]:
		dbat[i.strip()] = d[0]

for i in bowl.readlines():
	d = i.split(",")
	for i in d[1:]:
		dbowl[i.strip()] = d[0]


#op_result = "\
#		\nTarget  : 162\nScore  : 170"



#op_result += "\n\nWinner : Team2\n\n"
	

winner = ""

def maxamg(plist):
	return plist.index(max(plist))


def play(innings):
	global count
	global trun
	global target
	global innings1
	global innings2
	batsman_runs = ""
	if(innings == innings1):
		batsman_runs = i1_batsman_runs
	else:
		batsman_runs = i2_batsman_runs

	global winner
	for row in innings:
		if(not "extras" in (row[row.keys()[0]])):
			count = count + 1
		try:
			a = dbat[row[row.keys()[0]]['batsman']]
		except:
			a = 1
			print "nf:"+row[row.keys()[0]]['batsman']

		try:
			b = dbowl[row[row.keys()[0]]['bowler']]
		except:
			b = 1
			print "nf:"+row[row.keys()[0]]['bowler']
		#: or _ as the file name is
		f = open('iplclusters/'+str(a)+"_"+str(b), 'r')

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
			
			tballs += 1	
		
		p0 = float(a0)/tballs
		p1 = float(a1)/tballs
		p2 = float(a2)/tballs
		p3 = float(a3)/tballs
		p4 = float(a4)/tballs
		p6 = float(a6)/tballs
		#pe = float(ae)/tballs

		prob_list = [p0,p1,p2,p3,p4,p6]
		run_list = [0,1,2,3,4,6]

		cp1 = 0.0
		cp2 = 0.0
		p11 = 100
		cum_prob = {}
		for i in xrange(len(prob_list)) :
			cp1=cp2
			cp2+=(float(prob_list[i]))*p11
			cum_prob[run_list[i]]=[int(cp1),int(cp2-1)]
		
		r = random.Random().randint(0,99)
		for i in cum_prob.keys():
			if r>=cum_prob[i][0] and r<=cum_prob[i][1]:
				p = i
				break

		batsman_runs[row[row.keys()[0]]['batsman']] = batsman_runs.get(row[row.keys()[0]]['batsman'],0) + p

		trun = trun + p
		
		print("TEAM A")
		print("SCORE : "+str(trun))
		print("Batting :"+str(row[row.keys()[0]]['batsman'])+"(Batting) ; "+str(row[row.keys()[0]]['non_striker']))
		print("Bowling :"+str(row[row.keys()[0]]['bowler']))
		sys.stdout.write("Ball Number : " + str(int(count/6)) + "." + str(count % 6) + "\nRuns scored : " + str(p) + '\n')
		print("---------------------")
		if('wicket' in (row[row.keys()[0]])):
			print(str(row[row.keys()[0]]['batsman'])+" is out!!")
			time.sleep(0.5)
		sys.stdout.flush()
		time.sleep(0.1)
		
		sp.call("clear")			

def play2(innings):
	global count
	global trun
	global target
	global innings1
	global innings2
	batsman_runs = ""
	if(innings == innings1):
		batsman_runs = i1_batsman_runs
	else:
		batsman_runs = i2_batsman_runs

	global winner
	for row in innings:
		count = count + 1
		try:
			a = dbat[row[row.keys()[0]]['batsman']]
		except:
			a = 1
			print "nf:"+row[row.keys()[0]]['batsman']

		try:
			b = dbowl[row[row.keys()[0]]['bowler']]
		except:
			b = 1
			print "nf:"+row[row.keys()[0]]['bowler']
		#: or _ as the file name is
		f = open('iplclusters/'+str(a)+"_"+str(b), 'r')

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
			
			tballs += 1	
		

		p0 = float(a0)/tballs
		p1 = float(a1)/tballs
		p2 = float(a2)/tballs
		p3 = float(a3)/tballs
		p4 = float(a4)/tballs
		p6 = float(a6)/tballs
		#pe = float(ae)/tballs

		prob_list = [p0,p1,p2,p3,p4,p6]
		run_list = [0,1,2,3,4,6]

		cp1 = 0.0
		cp2 = 0.0
		p11 = 100
		cum_prob = {}
		for i in xrange(len(prob_list)) :
			cp1=cp2
			cp2+=(float(prob_list[i]))*p11
			cum_prob[run_list[i]]=[int(cp1),int(cp2-1)]
		
		r = random.Random().randint(0,99)
		for i in cum_prob.keys():
			if r>=cum_prob[i][0] and r<=cum_prob[i][1]:
				p = i
				break

		batsman_runs[row[row.keys()[0]]['batsman']] = batsman_runs.get(row[row.keys()[0]]['batsman'],0) + p

		trun = trun + p
		
		print("TEAM B")
		print("TARGET : "+str(target))
		print("SCORE : "+str(trun))
		print("Batting :"+str(row[row.keys()[0]]['batsman'])+"(Batting) ; "+str(row[row.keys()[0]]['non_striker']))
		print("Bowling :"+str(row[row.keys()[0]]['bowler']))
		sys.stdout.write("Ball Number : " + str(int(count/6)) + "." + str(count % 6) + "\nRuns scored : " + str(p) + '\n')
		print("---------------------")
		if('wicket' in (row[row.keys()[0]])):
			print(str(row[row.keys()[0]]['batsman'])+" is out!!")
			time.sleep(0.5)
		sys.stdout.flush()
		time.sleep(0.1)
		
		sp.call("clear")			
		if(innings == innings2 and trun > target):
			winner = "2"
			print("++++++++++++++++++++++++++++++++++++++++")
			print("Team B Wins")
			print("++++++++++++++++++++++++++++++++++++++++")
			print("SCOREBOARD")
			print("Team 1 Score: " + str(target))
			print("Team 2 Score: " + str(trun))
			print("-----------------------------------------+")
			break

data = yaml.load(open(fff,'r').read())
count = 0
trun = 0

innings1 = data['innings'][0]['1st innings']['deliveries']
innings2 = data['innings'][1]['2nd innings']['deliveries']

play(innings1)

target = trun
count = 0
trun = 0

play2(innings2)


if(winner != "2"):
	print("++++++++++++++++++++++++++++++++++++++++")
	print("Team A Wins")
	print("++++++++++++++++++++++++++++++++++++++++")
	print("SCOREBOARD")
	print("Team 1 Score: " + str(target))
	print("Team 2 Score: " + str(trun))
	print("-----------------------------------------+")

top3 = sorted(i1_batsman_runs, key = i1_batsman_runs.__getitem__, reverse = True)[:3]
print "TOP 3 PLAYERS(Team A)"
for i in top3:
	print i#,"-",i1_batsman_runs[i]
top3 = sorted(i2_batsman_runs, key = i2_batsman_runs.__getitem__, reverse = True)[:3]

print("-----------------------------------------")
print "TOP 3 PLAYERS(Team B)"
for i in top3:
	print i#,"-",i2_batsman_runs[i]

def maxrunplayer(fff):
	data = yaml.load(open(fff,'r').read())


	innings1 = data['innings'][0]['1st innings']['deliveries']
	innings2 = data['innings'][1]['2nd innings']['deliveries']


	in1_score = 0
	in2_score = 0

	i1_batsman_runs = dict()
	i2_batsman_runs = dict()

	for row in innings1:
		in1_score += row[row.keys()[0]]['runs']['batsman']
		try:
			i1_batsman_runs[row[row.keys()[0]]['batsman']] += row[row.keys()[0]]['runs']['total']
		except KeyError:
			i1_batsman_runs[row[row.keys()[0]]['batsman']] = 0
	
	for row in innings2:
		in2_score += row[row.keys()[0]]['runs']['batsman']
		try:
			i2_batsman_runs[row[row.keys()[0]]['batsman']] += row[row.keys()[0]]['runs']['total']
		except KeyError:
			i2_batsman_runs[row[row.keys()[0]]['batsman']] = 0

	print("-----------------------------------------+")
	print("ACTUAL RESULTS")
	print "Team A",in1_score
	print "Team B",in2_score

	print "TOP PLAYER(Team A)"
	top = sorted(i1_batsman_runs, key = i1_batsman_runs.__getitem__, reverse = True)[0]
	print top#,"-",i1_batsman_runs[top]

	print "TOP PLAYER(Team B)"
	top = sorted(i2_batsman_runs, key = i2_batsman_runs.__getitem__, reverse = True)[0]
	print top#,"-",i2_batsman_runs[top]

maxrunplayer(fff)
