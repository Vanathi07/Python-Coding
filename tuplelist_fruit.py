my_list=[("apple",2),("banana",3),("grape",4)]
fruit=my_list[1][0]
print("The fruit indexed is",fruit)

for i in my_list:
    fruit=i[0]
    quantity=i[1]
    print(f"There are {quantity} {fruit}s")
    
