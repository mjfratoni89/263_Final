import numpy as np
import os

owd=os.getcwd()
x=0 #see the x below
for team in os.listdir('./Teams'):
    # v=os.chdir(team)
    if team not in '.ipynb_checkpoints':
        for player in os.listdir('./Teams/' + team):
            #data = np.genfromtxt(r,delimiter=',',skip_header=2)
            #x==n
            #print(r)
            data=[]
            with open('./Teams/' + team + '/' + player,'r') as q:
                for line in q:
                    l = line.strip().split(',')
                    #all the if statements gets rid of everything thats not yearly stats
                    if l[0]=='':
                        x==1
                    elif l[0]=='Career':
                        x==1 
                    elif l[2].split()[0]=='Did':
                        x==1
                    elif l[0]=='Season':
                        x==1
                    elif l[0]=='1 season' or l[0]=='2 seasons' or l[0]=='3 seasons' or l[0]=='4 seasons' or l[0]=='5 seasons' or l[0]=='6 seasons' or l[0]=='7 seasons' or l[0]=='8 seasons' or l[0]=='12 seasons' or l[0]=='10 seasons' or l[0]=='9 seasons' or l[0]=='11 seasons' or l[0]=='15 seasons':
                        x==1
                    else:
                        #these are the stats we decide to use
                        #here I have the yr, age, team, games played
                        data.append([str(l[0]),float(l[1]),str(l[2]),float(l[5])])
            data=np.array(data)
            stats=[]
            for i in range(len(data)):
                if data[i,0].split('-')[0]=='2009':
                    stats.append(data[i,:])
                if data[i,0].split('-')[0]=='2010':
                    stats.append(data[i,:])
                if data[i,0].split('-')[0]=='2011':
                    stats.append(data[i,:])
                if data[i,0].split('-')[0]=='2012':
                    stats.append(data[i,:])
                if data[i,0].split('-')[0]=='2013':
                    stats.append(data[i,:])                
                    
            stats=np.array(stats)
            fstats=[]
            print(player)
            for j in range(len(stats)):
                if j>0:
                    if not stats[j,1]==stats[(j-1),1]:
                        fstats.append(stats[j,:])
                else:
                    fstats.append(stats[j,:])
            fstats=np.array(fstats)
                    
            print(fstats)
        
        
                        
            
    os.chdir(owd)
     
