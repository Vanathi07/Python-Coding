def retrieve_int(str):
    lst=[]
    for ele in str:
        s=""
        for x in ele:
            if(x.isdigit()):
                s=s+x
        if(s!=""):
            lst.append(s)
    return(lst)
str=input("Enter a string:").split()
lst=[]
lst=retrieve_int(str)
for y in lst:
    print(y,end=" ")
            
