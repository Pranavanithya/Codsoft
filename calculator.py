#------CALCULATOR-------
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print('Operations:\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION')
ch=int(input("Enter your choice:"))
if ch==1:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    print(add(a,b))
elif ch==2:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    print(subtract(a,b))
elif ch==3:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    print(multiply(a,b))
elif ch==4:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    if a>b:
        print(divide(a,b))
    else:
        print("error")

else:
    print("----Invalid Choice----")
    
