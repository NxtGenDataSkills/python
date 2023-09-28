##
##value=5;
##def the_flying_circus():
##    if (value == 5):
##        
##        print("This is 5")
##        return True
##        # Start coding here!
##        # Don't forget to indent
##        # the code inside this block!
##    elif (value > 5):
##        
##        print("This is greater than 5")
##        # Keep going here.
##        # You'll want to add the else statement, too!
##        
##    else :
##         print("This is less than 5")
##         
##print(the_flying_circus())   
##the_flying_circus()
##the_flying_circus()
Word=raw_input("Enter the word you want to convert to \"piglatin\" ");

L=len(Word);

L1=Word[0];
Word1=Word[1:]+Word[0]+"ay"
##Word2=Word1;
##Word2=Word2.replace(Word2[0],'')

print(Word1);
