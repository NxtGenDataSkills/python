def remove_duplicates(seq):
    x=[];
    for i in seq:
        if i not in x:
            x.append(i);
    return x;
print remove_duplicates([1,2,2])
         
       
