def Addition(n1,n2):
    while (n2 != 0):
        carry = n1 & n2
        n1 = n1 ^ n2
        n2 = carry << 1
    return n1
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
print(Addition(n1,n2))
