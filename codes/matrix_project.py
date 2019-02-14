import numpy as np
import matplotlib.pyplot as plt
import math 
import subprocess
import shlex

x = np.zeros((4,2))
b = np.array([[1.0],[2.0]])
s=0.0
for i in range (3):
   a = math.pi/6 + (math.pi/2)*(i)
   x[i+1,:] = np.transpose(np.matmul(np.array([[x[i,0],math.cos(a)], [x[i,1],math.sin(a)]]),b))   
   s=s+x[i+1,0]
print x
print s




A= x[0,:]
B= x[1,:]
C= x[2,:]
D= x[3,:]

len =10
lam_1=np.linspace(0,1,len)
x_AB=np.zeros((2,len))
x_BC=np.zeros((2,len))
x_CD=np.zeros((2,len))
x_DA=np.zeros((2,len))

for i in range(len):
 temp1=A+lam_1[i]*(B-A)
 x_AB[:,i]=temp1.T
 temp2=B+lam_1[i]*(C-B)
 x_BC[:,i]=temp2.T
 temp3=C+lam_1[i]*(D-C)
 x_CD[:,i]=temp3.T
 temp4=D+lam_1[i]*(A-D)
 x_DA[:,i]=temp4.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(A[0],A[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(C[0],C[1],'o')
plt.plot(D[0],D[1],'o')

plt.text((0.05),(-0.1),'A')
plt.text(B[0]*(1),B[1]*(1-0.15),'B')
plt.text(C[0]*(1+0.1),C[1]*(1),'C')
plt.text(D[0]*(1+0.1),D[1]*(1-0.1),'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()

