# pasting the documents from the web

sen_1=''' '''
sen_2=''' '''

# the k array will have unique words
k=[]
# here I am defining a function 'arr' which will first convert the strings of para_1 and 2 into words. then the unique words are stored in k while all words of sen_1 will be stored in 'a' 

def arr(sen,a):
    exclude=[',',' ', ':', ';' , '?','"','-', '(', ')']
    if len(sen)==1:
        if sen in exclude:
            return a
        else:
            a.append(sen)
            if sen not in k:
                k.append(a)
            return a
    elif sen[0] in exclude:
        return arr(sen[1:],a)
    else:
        for i in range(len(sen)):
            if sen[i] in exclude:
                a.append(sen[:i])
                if sen[:i] not in k:
                    k.append(sen[:i])
                return arr(sen[i+1:],a)
                
        
            
li_1=[]
li_2=[]

arr(sen_1,li_1)
arr(sen_2,li_2)

# making a dictionary from k and making its copy  for sen_2
d_1={}
for i in k:
    d_1[i]=0
d_2=d_1.copy()

# counting the times the words are repeated in sen_1 i.e. calculating magnitude of words vectors in sen_1 and sen_2
for i in li_1:
    d_1[i]=+1
    
for i in li_2:
    d_2[i]=+1

# calculating u.v

dot=0
for i in k:
    dot=dot+d_1[i]*d_2[i]


#calculating sqrt of u and v
def sq_rt(d):
    sum=0
    for value in d.values():
        sum=sum+value**2
    sum=sum**0.5
    return sum
 
 
 #finding theta

theta=(dot/(sq_rt(d_1)*sq_rt(d_2)))*100
print('the similarity is', theta)


