print("Enter two numbers")
a=int(input())
b=int(input())
L= a if a>b else b
while L<=a+b:
    if L%a==0 and L%b==0:
        print("LCM is",L)
        break
    L+=1
print()