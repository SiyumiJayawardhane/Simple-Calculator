value1=0
value2=0
operator=0
add=0
sub=0
mul=0
div=0
value1=float(input("Enter a number1:"))
print("Select an 1=Add,2=Sub,3=Mul,4=Div")
operator=int(input("Enter a operator:"))
if operator==1:
    value2=float(input("Enter a number2:"))
    add=value1+value2
    print("Addition=",add)
elif operator==2:
    value2=float(input("Enter a number2:"))
    sub=value1-value2
    print("SUbtraction=",sub)
elif operator==3:
    value2=float(input("Enter a number2:"))
    mul=value1*value2
    print("Multiplication=",mul)
elif operator==4:
    value2=float(input("Enter a number2:"))
    if (value2==0):
        print("Invalid")
    else:
        div=value1/value2
        print("Division=",div)
else:
    print("Invalid Input")
    
