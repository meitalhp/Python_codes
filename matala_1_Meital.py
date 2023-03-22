######1st question######

def my_func(x1,x2,x3):
    try:
        if x1+x2+x3==0:
            return 'Not a number – denominator equals zero'
    except:
        for i in {x1,x2,x3}:
            if type(i)!=float: 
                if type(i)==int:
                    return 'Error: parameters should be float'
                if type(i)!=int:
                    return None
                else:
                    break
        ans=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        return ans


#######2nd question############

def revword(word:str):
    word=word.lower()[::-1]
    return word

def countword():
    inp=input('enter a file address:\n ')
    file=open(file=inp)
    word=file.readline()
    c=0
    for l in file:
        line=l.strip(' ').split()
        for w in line:
            new_w=revword(w)
            if new_w in word:
                c=c+1
    file.close()
    return c




    
        
    
    
        
