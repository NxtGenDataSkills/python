def censor(text,word):
    length_of_word=len(word);
    censor_word="*"*length_of_word
    text=text.split();
    print text
    count=0;
    for i in text:
        if(i==word):          
            text[count]=censor_word;
        count+=1   
    return " ".join(text)

print censor("Yo go fro yo go","go");
