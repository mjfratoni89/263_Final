import numpy as np
import os

os.chdir('Teams')
for f in os.listdir('/'):
    #v=os.path.join(f)
    print (f)
    for r in os.listdir(v):
        data = np.genfromtxt(r,delimiter=',',skip_header=1)
        print(data)
