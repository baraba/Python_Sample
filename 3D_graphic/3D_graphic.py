import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()

ax=Axes3D(fig)

print("Welcometo use 3D graphic generator, the formula model is z=sqrt(x^n1+y^n2).\n")

a1=input("pleaseenter x axis length value(x),actual display range is from - x to x:\n")

a1=float(a1)

print("Thex axis actual display range is from - "+str(a1)+" to"+str(a1)+":\n")

a2=input("pleaseenter y axis length value(y),actual display range is from - y to y:\n")

a2=float(a2)

print("They axis actual display range is from - "+str(a2)+" to"+str(a2)+":\n")

a3=input("pleaseenter n power number of x value:(please enter an integer)\n")

a3=int(a3)

print("The power number of x value is "+str(a3)+".\n")

a4=input("pleaseenter n power number of y value:(please enter an integer)\n")

a4=int(a4)

print("Thepower number of y value is "+str(a4)+".\n")

X=np.arange(-a1,a1,0.5)

Y=np.arange(-a2,a2,0.5)

X,Y=np.meshgrid(X,Y)

Z=np.sqrt(X**a3+Y**a4)

ax.plot_surface(X,Y,Z,rstride=2,cstride=2,alpha=0.5,cmap=plt.cm.rainbow)

x1=input("pleaseenter x label name:\n")

x2=input("pleaseenter y label name:\n")

x3=input("pleaseenter z label name:\n")

x4=input("pleaseenter title label name:\n")

ax.set_xlabel(x1,fontsize=20)

ax.set_ylabel(x2,fontsize=20)

ax.set_zlabel(x3,fontsize=20)

ax.set_title(x4,fontsize=25)

ax.view_init(30,35)

b1=a1+4

b2=a2+4

cset=ax.contour(X,Y, Z, zdir = 'x', offset = -b1, cmap = plt.cm.hot)

cset=ax.contour(X,Y, Z, zdir = 'y', offset = -b2, cmap = plt.cm.hot)

cset=ax.contour(X,Y, Z, zdir = 'z', offset = -7, cmap = plt.cm.hot)

ax.set_xlim(-b1,b1)

ax.set_ylim(-b2,b2)

ax.set_zlim(-8,8)

plt.show()