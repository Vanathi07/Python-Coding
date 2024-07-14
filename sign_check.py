def sign_check(n1,n2):
    x=n1^n2
    if(x>=0):
        print("Two integers have same sign")
    else:
        print("Two integers have opposite signs")
n1 = int(input("Enter 1st integer:"))
n2 = int(input("Enter 2nd integer:"))
sign_check(n1,n2)
        
