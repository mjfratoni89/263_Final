# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 22:14:08 2014

@author: Asus
"""

from ny_utils import *

import datetime
import matplotlib.pyplot as plt
import os
from sklearn import mixture
import pandas as pd
import matplotlib.pyplot as plt

gmm = mixture.GMM(n_components=2, covariance_type='full', n_iter=100)

weektionary={0:1,1:1,2:1,3:1,4:1,5:0,6:0}
    
    
i=0   
for filename in os.listdir("./"):
  if filename.endswith(".csv"):
    if not filename.endswith("_quest.csv"):
      
      #preparing the training data
      data = read_NY_NY(filename)
      
      for j in range(len(data)):
          data[j,3]=weektionary[data[j,3]]
      X=data[:,[0,1,3,4]]
      
      #finding the margins
      max_lat=max(X[:,0])
      min_lat=min(X[:,0])
      max_lon=max(X[:,1])
      min_lon=min(X[:,1])
      
      resolution=800
      lats=np.linspace(min_lat,max_lat,num=resolution)
      l_lats=len(lats)
      lons=np.linspace(min_lon,max_lon,num=resolution)
      l_lons=len(lons)
      
      #keeping one constant and changing the other
      lats=np.tile(lats,l_lons)
      lons=np.repeat(lons,l_lats)
      #This will be the range to distribute over the probabilities
              
      coord_range=np.vstack((lats,lons))
      
          
      #Training
      gmm.fit(X)
      
      
      pred_cases=[]
      lat_lon=[]
      
      #if i>0:
          #break
      #The test file
      test='E:/School/CE263N/Assignment 5/new_york_quest/'+os.path.splitext(filename)[0]+'_quest.csv'
      plt.ioff()
      with open(test,'r') as f:
          for line in f:
              #getting the test cases
              t= datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S') 
              pred_cases.append([[t.weekday()],[t.hour]])
          for case in pred_cases:
              #Preparing the prediction matrix
              Xpred=np.vstack((coord_range,np.ones(int(resolution*resolution))*case[0],np.ones(int(resolution*resolution))*case[1])).T
              pred = np.exp(gmm.score(Xpred))
              #Finding the row that correspondes to the highest probability
              lat_lon.append(Xpred[np.where(pred==max(pred))][0])
              
          df=pd.DataFrame(lat_lon,columns=['lat','lon','weekday','hour'])
          df.to_csv('E:/School/CE263N/Assignment 5/new_york_pred/'+os.path.splitext(filename)[0]+'_pred_off.csv',index=False)
          df.plot(kind='scatter',x='lat',y='lon')
          savefig('E:/School/CE263N/Assignment 5/new_york_pred/'+os.path.splitext(filename)[0]+'_pred_off.png')
          plt.close()


     
      
      
      print i,') Aha! I know what %s did last summer' % filename.split('.')[0]
      i+=1