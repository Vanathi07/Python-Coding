def step_count(n):
    if(n == 0):
        return 1
    elif(n < 0):
        return 0
    else:
        return step_count(n - 3) + step_count(n - 2) +step_count(n - 1)
n=int(input("Enter n value:"))
print("The step count for "+str(n)+" steps is "+str(step_count(n)))

