import numpy as np
import os

path=os.chdir('Teams')
owd=os.getcwd()
x=0 #see the x below
for f in os.listdir(path):
    v=os.chdir(f)
    for r in os.listdir(v):
        #data = np.genfromtxt(r,delimiter=',',skip_header=2)
        #x==n
        #print(r)
        data=[]
        with open(r,'r',encoding="utf8") as q:
            for line in q:
                l = line.strip().split(',')
                #all the if statements gets rid of everything thats not yearly stats
                if l[0]=='' or l[2]=='Did Not Play (illness—heart condition)' or l[2]=='Did Not Play (other pro league—Italy)' or l[2]=='Did Not Play (other pro league—Russia Croatia)' or l[2]=='Did Not Play (other pro league—Israel)' or l[2]=='Did Not Play (other pro league—Ukraine)' or l[2]=='Did Not Play (other pro league—Greece Italy)':
                    x==1 #literally just so it doesn't append 'data'
                elif l[0]=='Season' or l[2]=='Did Not Play (other pro league—D-League Spain)' or l[2]=='Did Not Play' or l[2]=='Did Not Play (other pro league—Russia)' or l[2]=='Did Not Play (other pro league—Russia Greece)' or l[2]=='Did Not Play (suspended—substance abuse)' or l[2]=='Did Not Play (other pro league—Ukraine Israel)':
                    x==1
                elif l[2]=='Did Not Play (other pro league—China)' or l[2]=='Did Not Play (injury—shoulder)' or l[2]=='Did Not Play (injury—achilles)' or l[2]=='Did Not Play (injury—knee)' or l[2]=='Did Not Play (other pro league—Spain)' or l[2]=='Did Not Play (other pro league—Puerto Rico)' or l[2]=='Did Not Play (other pro league—Germany)':
                    x==1
                elif l[0]=='Career' or l[0]=='1 season' or l[0]=='2 seasons' or l[0]=='3 seasons' or l[0]=='4 seasons' or l[0]=='5 seasons' or l[0]=='6 seasons' or l[0]=='7 seasons' or l[0]=='8 seasons' or l[0]=='12 seasons' or l[0]=='10 seasons' or l[0]=='9 seasons' or l[0]=='11 seasons' or l[0]=='15 seasons':
                    x==1 
                else:
                    #these are the stats we decide to use
                    #here I have the yr, age, team, games played
                    data.append([str(l[0]),float(l[1]),str(l[2]),float(l[5])])
        data=np.array(data)
        print(data)
        
                
            
    os.chdir(owd)
     
