num=int(input("enter a number"))
if (num%20):
    print("twist")
elif(num%15):
    pass
elif(num%5):
    print("fizz")
elif(num%3):
    print("buzz")
else:
    print(num+num)