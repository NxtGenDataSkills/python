def digit_sum(n):
    sum=0;
    while(n>0):
        x=n%10;
        n=n/10;
        sum+=x;
    return sum;

print digit_sum(2)
