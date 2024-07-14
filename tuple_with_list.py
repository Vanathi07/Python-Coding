my_tuple=(1,2,["apple","banana"])
my_tuple[2].append("grape")
print(my_tuple)

for element in my_tuple:
    if isinstance (element,list):
        for fruit in element:
            print(fruit)
    else:
        print(element)
