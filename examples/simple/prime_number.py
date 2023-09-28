def is_prime(x):
    if x in(0,1) or x<0:
        return False;
    elif x ==2:
        return True;
    for i in range(2,x):
        if(x%i==0):
            return False
    else:
            return True;    
            
print is_prime(3);
