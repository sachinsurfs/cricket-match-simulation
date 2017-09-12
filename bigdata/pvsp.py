import yaml
import os


def extract(f):
    with open("t20/"+f+".yaml", 'r') as stream:
        data = yaml.load(stream)
    
    date = str(data['info']['dates'][0])



    innings = str(1)
    for rowd in data['innings'][0]['1st innings']['deliveries']:
        balllist = rowd.keys() # has only 1 element always
        ballno = balllist[0]
        row = rowd[ballno]
        
        #get details of one ball
        batsman = str(row['batsman'])
        bowler = str(row['bowler'])
        batscore = str(row['runs']['batsman'])
        extra = str(row['runs']['extras'])
        ball = str(ballno)
    
        #store it in corresponing file
        pwd = os.getcwd()
        try:
            os.chdir(batsman)
        except:
            os.mkdir(batsman)
            os.chdir(batsman)
        filename = batsman + ':' + bowler
        if not os.path.exists(filename):
           open(filename, 'w').close() 
        with open(filename, 'a') as store:
            delimiter = " "
            store.write(ball + delimiter + batscore + delimiter + extra + delimiter + date + delimiter + innings + "\n")
        os.chdir(pwd)            

    try:
        f = data['innings'][1]
    except:
        print("2nd innings not found")
        return

    innings = str(2)
    for rowd in data['innings'][1]['2nd innings']['deliveries']:
        balllist = rowd.keys() # has only 1 element always
        ballno = balllist[0]
        row = rowd[ballno]
        
        #get details of one ball
        batsman = str(row['batsman'])
        bowler = str(row['bowler'])
        batscore = str(row['runs']['batsman'])
        extra = str(row['runs']['extras'])
        ball = str(ballno)
    
        #store it in corresponing file
        pwd = os.getcwd()
        try:
            os.chdir(batsman)
        except:
            os.mkdir(batsman)
            os.chdir(batsman)
        filename = batsman + ':' + bowler
        if not os.path.exists(filename):
           open(filename, 'w').close() 
        with open(filename, 'a') as store:
            delimiter = " "
            store.write(ball + delimiter + batscore + delimiter + extra + delimiter + date + delimiter + innings + "\n")
        os.chdir(pwd)
    return


with open("config.txt") as stream:
    content = stream.readlines()
for i in content:
    f = i.split("-")[4].strip()
    extract(f)
