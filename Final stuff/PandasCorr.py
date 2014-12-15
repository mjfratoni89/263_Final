import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsRegressor
from sklearn.cross_validation import KFold
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# dataframe to use for correlation
df = pd.DataFrame.from_csv('leagues_NBA_2014_team.csv')

#creating correlation matrix for data
corr = df.corr()
# separating rank from the correlation matrix
rk = corr[:1]
# topcorr = rk.sort('Rk',ascending = True)

# parameters with highest correlation with rank
orderofimportance = 'FG%, 2P%, 3P%, PTS, DRB'

# parameters with really low correlation with rank that can probably be cut
cut = 'MP, 2P, FTA, TRB, STL'

# generating nparray to use for regressors
data = np.genfromtxt('leagues_NBA_2014_team.csv',delimiter=',',skip_header=1)

# separating rank and everything else to use to train regressor
rk = data[:,1]
data = data[:,2:]
data2 = data[:,[4,7,10,15,22]]

# cross-validating regressor
# number of nearest neighbors
n = 5
CVerrors = [200,100]
while CVerrors[-2] > CVerrors[-1]:
	kf = KFold(len(data),n_folds=5,shuffle=True)
	CVerror = []
	for trnind,tstind in kf:
		# creating, fitting, and predicting with the KNN regressor
		knn = KNeighborsRegressor(n_neighbors=n)
		knn.fit(data[trnind,:],rk[trnind])
		p = knn.predict(data[tstind,:])
		error = 0
		for i in range(0,len(p)):
			error += (p[i]-rk[tstind][i])**2
		error = np.sqrt(error)
		CVerror.append(error)
	# finding CV error
	CVerrors.append(np.mean(CVerror))
	# incrementing number of nearest neighbors in hopes of getting lower CV error
	n += 5

print ('CV error for K-Nearest Neighbors Regression is with n = ' + str(n) + ' is ' + str(np.mean(CVerror)))

# decision tree regressor
leaf = 1
split = 2
CVerrors = [200,100]
while CVerrors[-2] > CVerrors[-1]:
	kf = KFold(len(data),n_folds=5,shuffle=True)
	CVerror = []
	for trnind,tstind in kf:
		# creating, fitting, and predicting with the clf regressor
		clf = DecisionTreeRegressor(min_samples_split=split,min_samples_leaf=leaf)
		clf.fit(data2[trnind,:],rk[trnind])
		p = clf.predict(data2[tstind,:])
		error = 0
		for i in range(0,len(p)):
			error += (p[i]-rk[tstind][i])**2
		error = np.sqrt(error)
		CVerror.append(error)
	# finding CV error
	CVerrors.append(np.mean(CVerror))
	# incrementing number of minimum leaves in hopes of getting lower CV error
	leaf += 1

	# same thing for incremeneting minimum number of samples
	if CVerrors[-2] < CVerror[-1] and leaf is not 1:
		CVerrors = [200,100]
		leaf -= 1
		while CVerrors[-2] > CVerrors[-1]:
			kf = KFold(len(data),n_folds=5,shuffle=True)
			CVerror = []
			for trnind,tstind in kf:
				# creating, fitting, and predicting with the clf regressor
				clf = DecisionTreeRegressor(min_samples_split=split,min_samples_leaf=leaf)
				clf.fit(data2[trnind,:],rk[trnind])
				p = clf.predict(data2[tstind,:])
				error = 0
				for i in range(0,len(p)):
					error += (p[i]-rk[tstind][i])**2
				error = np.sqrt(error)
				CVerror.append(error)
			# finding CV error
			CVerrors.append(np.mean(CVerror))
			# incrementing number of minimum leaves in hopes of getting lower CV error
			split += 1

split -= 1

print ('CV error for Decision Tree Regressor is ' + str(np.mean(CVerror)) + ' with min_leaf = ' + str(leaf) + ' and min sampels = ' + str(split))

L = LinearRegression(fit_intercept=True,normalize=True)
kf = KFold(len(data),n_folds=5,shuffle=True)
CVerror = []
for trnind,tstind in kf:
	L.fit(data2[trnind,:],rk[trnind])
	p = L.predict(data2[tstind,:])
	error = 0
	for i in range(0,len(p)):
		error += (p[i]-rk[tstind][i])**2
	error = np.sqrt(error)
	CVerror.append(error)

print (p)

print ('CV error for Linear Regression is ' + str(np.mean(CVerror)))
print (L.get_params(deep=True))

# pickling classifiers and regressors
knn.fit(data2,rk)
L.fit(data2,rk)

with open('LinReg.pickle','wb') as f:
	pickle.dump(L,f)

with open('knn.pickle','wb') as f:
	pickle.dump(knn,f)
