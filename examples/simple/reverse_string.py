def reverse(text):
    x="";
    for i in range(0,len(text)):
        print text[len(text)-(i+1)]
        
        x=x+(text[len(text)-(i+1)]);
    return x;

print reverse("sai")
