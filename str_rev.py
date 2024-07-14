def rev(st):
    string = st.split()  
    rev_str = ''
    for string1 in string:
        string1 = string1[::-1]  
        string1 = string1.capitalize() + ' '  
        rev_str += string1
    return rev_str
s = input("Enter the string:")
print(s)
print("The string after reversal is:")
print(rev(s))

