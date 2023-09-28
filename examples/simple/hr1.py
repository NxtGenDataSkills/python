a=[5,6,7]
b=[3,6,10]

A=0;
B=0;

for i in range(3):
    print i
    if(a[i]>b[i]):
        A+=1;
        
    elif(a[i]<b[i]):
        B+=1;
        
print A,B
        
