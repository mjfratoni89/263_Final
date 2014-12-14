import numpy as np
import os

csvfile=[]
owd=os.getcwd()
x=0 #see the x below
for team in os.listdir('./Teams'):
    MP_Player_Tots = []
    # v=os.chdir(team)
    if team not in '.ipynb_checkpoints':
        #print (str(team)+' predicted player minutes')
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
                        data.append([str(l[0]),float(l[7])])
            data=np.array(data)
            team_mp=[]
            stats=[]
            for i in range(len(data)):
                if data[i,0].split('-')[0]=='2014':
                    stats.append(data[i,:])                
                    
            stats=np.array(stats)
            fstats=[]
            for j in range(len(stats)):
                if j>0:
                    if not stats[j,1]==stats[(j-1),1]:
                        fstats.append(stats[j,1])
                else:
                    fstats.append(stats[j,1])
            fstats=np.array(fstats)
            fstats=fstats.astype(np.float) 
            if not fstats.size==0:            
                MP_Player_Tots.append(fstats[0])
        
        MP_Team_Tot=sum(MP_Player_Tots)
        MP_Player_Frac = MP_Player_Tots/MP_Team_Tot
        MP_Player_Pred = MP_Player_Frac*19827          #19827= avg mins played per season over last 4 seasons
        
        #print(MP_Player_Pred)
        
    
    for i in range(len(MP_Player_Pred)):
        csvfile.append(MP_Player_Pred[i])
        
    
print(csvfile)

#print results to csv
with open('predicted_minutes_played.csv','w') as f:
    for i in range(len(csvfile)):
        f.write("%f\n" % (csvfile[i]))
f.close()
                 
            
     
