def min_oper(A, B):
	x = len(A)
	y = len(B)
	if y != x:
		return -1
	count = [0] * 256
	for i in range(y):	 
		count[ord(B[i])] += 1
	for i in range(y):	 
		count[ord(A[i])] -= 1
	for i in range(256): 
		if count[i]:
			return -1
res = 0
i = y-1
j = y-1
while i >= 0:
        while i>= 0 and A[i] != B[j]:
                i -= 1
                res += 1
        if i >= 0:
                i -= 1
                j -= 1
return res
A = input("Enter string A:")
B = input("Enter string B:")
print ("Minimum number of operations required is " + str(min_oper(A,B)))

