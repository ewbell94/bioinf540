import numpy as np
import matplotlib.pyplot as p
from sys import argv
from math import sqrt
from copy import deepcopy
from scipy.linalg import fractional_matrix_power
from scipy.sparse.csgraph import laplacian
             
f=open(argv[1])

#Read in data from the PDB file
coords=[]
inds=[]
for line in f:
    if line[:4]=="ATOM" and line[12:16].strip()=="CA": #only read CA atoms
        coords.append([float(line[30:38]),float(line[38:46]),float(line[46:54])])
        inds.append(int(line[22:26]))
f.close()

#Calculate the distance matrix A from PDB data
A=[[0. for j in range(len(coords))] for i in range(len(coords))]
for i in range(len(coords)):
    for j in range(i+1,len(coords)):
        dist=sqrt(sum([(coords[i][n]-coords[j][n])**2 for n in range(3)]))
        if dist<8.0:
            A[i][j]=1.
            A[j][i]=A[i][j]
#p.matshow(A)
#p.show()
        
#Calculate D and L from data
D=[[0. for j in range(len(A))] for i in range(len(A))]
for i in range(len(A)):
    D[i][i]=sum(A[i])
A=np.asmatrix(A)
D=np.asmatrix(D)
#L=D-A
L=np.asmatrix(np.eye(len(A)))-fractional_matrix_power(D,-0.5)*A*fractional_matrix_power(D,-0.5)
#L=np.asmatrix(laplacian(A,normed=True))
#plotmat=deepcopy(L)
#for i in range(len(A)):
    #plotmat[i,i]=0.
#p.matshow(plotmat)
#p.show()

#Calculate fiedler vector, calculate domain divisons from it
E,V=np.linalg.eig(L)
#p.plot([i for i in range(E.shape[0])],E)
#p.show()
fnum=E[1]
fvec=V[:,1]
p.plot([i for i in range(fvec.shape[0])],fvec)
p.show()

signvec=[0. for i in range(len(A))]
for i in range(len(A)):
    if fvec[i,0]>0.:
        signvec[i]=1.

def giniIndex(x):
    total=0.
    for array in x:
        total+=1-(sum(array)/len(array))**2-(1-(sum(array)/len(array)))**2
    return total

basegini=giniIndex([signvec])
ginis=[giniIndex([signvec[:i],signvec[i:]]) for i in range(1,len(A)-1)]
print(basegini-min(ginis))
print(ginis.index(min(ginis)))
'''
smoothing=30
change=[False for i in range(len(A))]
positive=True
for i in range(1,len(A)):
    if fvec[i,0]<0. and positive:
        change[i]=True
        positive=False
    elif fvec[i,0]>0. and not positive:
        change[i]=True
        positive=True

for i in range(len(A)-smoothing):
    if change[i]:
        for j in range(i+1,i+smoothing):
            if change[j]:
                change[i]=False
                change[j]=False

for i in range(smoothing):
    change[i]=False
for i in range(len(A)-smoothing,len(A)):
    change[i]=False


boundaries=[(inds[i],i) for i in range(len(A)) if change[i]]
output=[str(ind[1]) for ind in boundaries]
print(",".join(output))
#print("Domain residue boundaries:")
'''
