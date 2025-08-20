a = int(input("Enter your budget: "))
b = int(input("enter the number of toys: "))
c = int(input("enter the price of the first toy: "))

lst = [c]

for i in range (1,b):
    c += 20
    lst.append(c)

d = sum(lst)

if d>a:
    while d>a:
        del lst[-1]
        d = sum(lst)

        


else :
    print ("You can afford all the toys")



print("You can afford the folowing toys : ",lst)
