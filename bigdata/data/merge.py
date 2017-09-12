import os
f1 = open(os.path.join(os.getcwd(),"profile"))
f2 = open(os.path.join(os.getcwd(),"singledata"))
d = {}
for row in f1.readlines():
    da = row.split(",")
    d[da[0]] = {'run' : da[1], 'balls' : da[2] , 'avg' : da[3].strip()}

f3 = open("newdata",'w')
for row in f2.readlines():
    da = row.split(",")
    de = ","
    f3.write(da[0] + de + da[1] + de + da[2].split(".")[1] + de + da[3] + de + d[da[0]]['avg'] + de + d[da[0]]['run'] + de + d[da[0]]['balls'] + "\n")


f1.close()
f2.close()
f3.close()
