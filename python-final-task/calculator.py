i=0
while (1):
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    op=input("Enter the operator (+, -, *, /, **) : ")
    if (op=="+"):
        print(f"The result is : {a+b}")
    elif (op=="-"):
        print(f"The result is : {a-b}")
    elif (op=="*"):
        print(f"The result is : {a*b}")
    elif (op=="/"):
        if(b!=0):
            print(f"The result is : {a/b}")
        else:
            print("Dividing by 0 is not possible")
    elif (op=="**"):
        print(f"The result is : {a**b}")