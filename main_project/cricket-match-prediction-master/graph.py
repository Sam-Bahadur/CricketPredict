import matplotlib.pyplot as mt
import numpy as np
def graphofplayer(ty,name):
    if ty=="batsman":
        x,y=np.loadtxt('D:/major project/Code/New folder/'+name+'.csv',delimiter=',',unpack=True)
        mt.subplot(211)
        mt.bar(x,y,color=['orange'])
        mt.xlabel('YEAR')
        mt.ylabel('RUNS')
        mt.title(name)
        mt.legend()
        mt.show()
        mt.subplot(212)
        mt.scatter(x,y,color=['red','green','blue'])
        mt.xlabel('YEAR')
        mt.ylabel('RUNS')
        mt.grid()
        mt.title(name)
        mt.legend()
        mt.show()
    else:
        x,y=np.loadtxt('D:/major project/Code/New folder/'+name+'.csv',delimiter=',',unpack=True)
        mt.subplot(2,1,1)
        mt.bar(x,y,color=['red','green','blue'])
        mt.xlabel('YEAR')
        mt.ylabel('WICKETS')
        mt.title(name)
        mt.legend()
        mt.show()
        mt.subplot(2,1,2)
        mt.scatter(x,y,color=['red','green','blue'])
        mt.xlabel('YEAR')
        mt.ylabel('WICKETS')
        mt.grid()
        mt.title(name)
        mt.legend()
        mt.show()
