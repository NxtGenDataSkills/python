def median(seq):
    length=len(seq);
    seq.sort();
    value=0;
    med=0;
    if(length%2==0):
       med=length/2;
       value=(seq[med]+seq[med-1])/2.0;
    elif(length==1):
        return seq[0];    
    else:
        med=(length/2)+1;
        print "median is" ,med;
        value=float(seq[med-1]);
    return value;

print median([6, 8, 12, 2, 23]);
