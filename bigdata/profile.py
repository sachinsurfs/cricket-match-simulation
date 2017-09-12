import os
profile = {}
for r, d, f in os.walk("."):
    for i in d:
        if i == 't20':
            continue
#        print(os.path.join(os.getcwd(),i))
        for r1, d1, f1 in os.walk(os.path.join(os.getcwd(),i)):
#            print("here")
            run = 0
            balls = 0
            for f2 in f1:
                if f2 == 'singledata':
                    continue
#                print(r1)
#                print("hi")
                fi = os.path.join(r1,f2)
                file1 = open(fi,'r')
                file2 = file1.readlines()
                file1.close()
                for row in file2:
                    r2 = row.split(" ")
                    run = run + int(r2[1])
                    balls = balls +1
            profile[i] = {'run':run, 'balls':balls}
        
print(profile)

with open("profile", "a") as f:
     for (n, d) in profile.iteritems():
        f.write(n + "," + str(d['run']) + "," + str(d['balls']) + "," + str(float(float(d['run'])/float(d['balls']))) + "\n") 
