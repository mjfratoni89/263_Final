import numpy as np
import os
from sklearn import tree
import pickle

owd=os.getcwd()
x=0 #see the x below
League=[]
PMP=[]
names=[]
teamnames = []

# getting the predicted minutes played for each player
# that was calculated in PredictMinsPlayed2015.py
with open('predicted_minutes_played.csv','r') as q:
    for line in q:
        l =line.strip().split(',')
        PMP.append([float(l[0]),str(l[1])])
PMP=np.array(PMP)
names=PMP[:,1]

# cycling through each team, and within each team
# cycling through each player
for team in os.listdir('./Teams'):
    if team not in '.ipynb_checkpoints':
        Team_Tot=[]
        if team not in '.DS_Store':
            teamnames.append(team)
            for player in os.listdir('./Teams/' + team):
                data=[]
                with open('./Teams/' + team + '/' + player,'r') as q:
                    for line in q:
                        l = line.strip().split(',')
                        for i in range(len(l)):
                            if l[i]=='':
                                l[i]=0 #any empty stats are assigned 0
                        #all the if statements gets rid of everything thats not yearly stats
                        if l[0]==0:
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
                            #here I have the yr, MP, age, FG, FGA, 2G, 2GA, 3G, 3GA, PTS, DRB 
                            data.append([str(l[0]),float(l[7]),float(l[1]),float(l[8]),float(l[9]),float(l[14]),float(l[15]),float(l[11]),float(l[12]),float(l[29]),float(l[22])])
                data=np.array(data)
                stats=[]
                tst_stats=[]

                # only getting the past 5 years and the current year stats
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
                    if data[i,0].split('-')[0]=='2014':
                        stats.append(data[i,:])                    
                stats=np.array(stats)

                # this assures that each yr has the total stats for that player        
                trn_stats=[]
                for j in range(len(stats)):
                    if j>0:
                        if not stats[j,2]==stats[(j-1),2]:
                            trn_stats.append(stats[j,:])
                    else:
                        trn_stats.append(stats[j,:])
                trn_stats=np.array(trn_stats)

                # getting rid of the year string and turning all the numbers to floats
                # we keep the age to use as a time component in the regression
                trn_stats=trn_stats[:,1:]
                trn_stats=trn_stats.astype(np.float)

                # minutes player and age are the X
                # the rest of the stats are the Y
                # the X_tst is the predicted total minutes for this season and the age this year
                X_trn=trn_stats[:,:2]
                Y_trn=trn_stats[:,2:]
                X_tst=np.array([float(PMP[np.where(names==player),0][0][0]),X_trn[-1,1]])

                # the regression    
                dt=tree.DecisionTreeRegressor()
                fit=dt.fit(X_trn,Y_trn)
                final_stats=fit.predict(X_tst)

                # aggregating the stats into a single list per team
                Team_Tot.append(final_stats)

            # we aggregate all the stats per team, and getting FG%, 2P%, 3P%    
            Team_Tot=np.array(Team_Tot)
            FG, FGA, tG, tGA, hG, hGA, PTS, DRB = [],[],[],[],[],[],[],[]
            for i in range(len(Team_Tot)):
                FG.append(Team_Tot[i][0][0])
                FGA.append(Team_Tot[i][0][1])
                tG.append(Team_Tot[i][0][2])
                tGA.append(Team_Tot[i][0][3])
                hG.append(Team_Tot[i][0][4])
                hGA.append(Team_Tot[i][0][5])
                PTS.append(Team_Tot[i][0][6])
                DRB.append(Team_Tot[i][0][7])
            FG=sum(FG)
            FGA=sum(FGA)
            FGp=FG/FGA
            tG=sum(tG)
            tGA=sum(tGA)
            tGp=tG/tGA
            hG=sum(hG)
            hGA=sum(hGA)
            hGp=hG/hGA
            PTS=sum(PTS)
            DRB=sum(DRB)
            Team_tot=[FGp,tGp,hGp,PTS,DRB]
            print(team,'stats are',Team_tot)

    # aggregating all the teams into this year    
    if team not in '.ipynb_checkpoints':  
        if team not in '.DS_Store':  
            League.append(Team_tot)
                                            
    os.chdir(owd)
League=np.array(League)
teamnames = np.array(teamnames)

L = pickle.load(open('LinReg.pickle','rb'))
p = L.predict(League)
print (p)
                        
