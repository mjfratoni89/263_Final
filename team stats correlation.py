import numpy as np

data = np.genfromtxt('leagues_NBA_2014_team.csv',delimiter=',',skip_header=1,usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
#1st col was team names (introduced as 'nan')
#2nd col is wins (now the 1st)
#I don't think we need the names to correlate, just the wins

# if someone knows how to condense the usecols to ignore 
# just the first col, do that

cor_matrix=np.corrcoef(data)
cor_matrix=cor_matrix[0,:]

max_corr=0
for i in range(len(cor_matrix)):
    if max_corr<cor_matrix[i] and cor_matrix[i]<1:
        max_corr=cor_matrix[i]
max_corr2=0
for i in range(len(cor_matrix)):
    if max_corr2<cor_matrix[i] and cor_matrix[i]<max_corr:
        max_corr2=cor_matrix[i]
max_corr3=0
for i in range(len(cor_matrix)):
    if max_corr3<cor_matrix[i] and cor_matrix[i]<max_corr2:
        max_corr3=cor_matrix[i]

print(cor_matrix)
print(max_corr,max_corr2,max_corr3)

indexes=[np.where(cor_matrix==max_corr),np.where(cor_matrix==max_corr2),np.where(cor_matrix==max_corr3)]
print(indexes)
