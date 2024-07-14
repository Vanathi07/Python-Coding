def search(n,x):
    for i in range(len(n)):
        if n[i] == x:
            return i
    return -1
a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").strip().split()))
print(n)
#nums = [4, 5, 6, 7, 0, 1, 2, 3]
x = int(input("Enter an element to search:"))
print("The index in which the target is present is", search(n, x))
