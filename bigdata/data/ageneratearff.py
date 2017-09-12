import sys
pred=open(str(sys.argv[1]),"r")
uniques=open(str("out")+":"+str(sys.argv[1])+	".arff","w")

li=pred.readlines()
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]

uniques.write("@relation "+sys.argv[1] + "\n\n")

for i in li:
	i=i.strip()
	#print(i)
	attr=i.split(",")
	j=0
	while j<7:
		if j==0 and attr[j].strip() not in col1:
			col1.append(attr[j].strip())
			#print(attr[j])
		if j==1 and attr[j].strip() not in col2:
			col2.append(attr[j].strip())
			#print(attr[j])
		if j==2 and attr[j].strip() not in col3:
			col3.append(attr[j].strip())
		if j==3 and attr[j].strip() not in col4:
			col4.append(attr[j].strip())
		if j==4 and attr[j].strip() not in col5:
			col5.append(attr[j].strip())
		if j==5 and attr[j].strip() not in col6:
			#attr[j]=attr[j].strip()[0]
			col6.append(attr[j].strip())
		if j==6 and attr[j].strip() not in col6:
			#attr[j]=attr[j].strip()[0]
			col7.append(attr[j].strip())
		j+=1



uniques.write("@attribute col1 {")
for i in col1:
	if col1.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(","+i)
uniques.write("}\n")
uniques.write("@attribute col2 {")
for i in col2:
	if col2.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")
uniques.write("@attribute col3 {")
for i in col3:
	if col3.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")
uniques.write("@attribute col4 {")
for i in col4:
	if col4.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")
uniques.write("@attribute col5 {")
for i in col5:
	if col5.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")

uniques.write("@attribute col6 {")
for i in col6:
	if col6.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")


uniques.write("@attribute col7 {")
for i in col7:
	if col7.index(i)==0:
		uniques.write(i)
	else:
		uniques.write(",")
		uniques.write(i)
uniques.write("}\n")

uniques.write("@data\n")
for i in li:
	uniques.write(i)

