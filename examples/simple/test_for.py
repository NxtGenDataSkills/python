def fizz_count(x):
    count=0;
    for i in x:
        if(i=="fizz"):
            count+=1;
    return count;        
 
x = ["fizz","cat","fizz"]
 
print(fizz_count(x));
