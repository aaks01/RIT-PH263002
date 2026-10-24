#Experiment No. 6 (look up corresponding pdf)
import math
def compute(fx,fd,fm,fN):
    theta=math.atan(fx/fd)
    l=float(math.sin(theta)/(fN*fm))
    return l
a=int(input("No. of distance adjustments       : "))
b=int(input("No. of readings per adjustment    : "))
N=float(input("Enter grating density (lines/m) : "))
l=0
n=0
i=0
while i<a :
    d=float(input("Enter D"+str(i+1)+" : "))
    j=0
    while j<b :
        m=int(input("M"+str(j+1)+" : "))
        x1=float(input("X1 : "))
        x2=float(input("X2 : "))
        x=float((x1+x2)/2)
        l+=(compute(x,d,m,N))
        n=n+1
        j=j+1
    i=i+1
print("wavelength (m) : "+str(l/n))