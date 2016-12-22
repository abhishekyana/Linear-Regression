import matplotlib.pyplot as plt # To plot the OUTPUT Graphically

#function for a hypothesis calculation
def hypo(t,x):
    h=[]
    for i in range(0,len(x)):
         h.append(t[0]+t[1]*x[i]//1)
    return h
#calc the J(t0,t1) funtion for the gradient
def gradient(lr,x,y,t,m):
    sum1=0
    sum2=1
    for i in range(1,m+1):
        sum1=sum1+(t[0]+t[1]*x[i-1]-y[i-1])
        sum2=sum1*x[i-1]
    
    temp0=t[0]-lr*(sum1/m)
    temp1=t[1]-lr*(sum2/m)
    t[0]=temp0
    t[1]=temp1
    return t,sum2/m
#find the minimum gradient for the J function
def min_grad(lr,x,y,t,m):
    while not( -0.0087268677907587893<=gradient(lr,x,y,t,m)[1]<=0.0087268677907587893):
        a=gradient(lr,x,y,t,m)
        print(a)
    return t
        


#testing area
x=[245,312,279,308,199,219,405,324,319,255]
y=[1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]
t=[0.0,0.0]
m=len(x)
min_grad(0.0000001,x,y,t,m)
print(t,3*'\n')
h=hypo(t,x)
print(h,2*'\n',y)
plt.plot(x,y,'ro')
plt.plot(x,h,'-')
plt.axis([0,500,0,2500])
plt.show()

