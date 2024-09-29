# write a program to print grade obtained a test. Take marks obtained from user and display the grade.

x=int(input("Enter Marks "))
if x>90:
    print("Grade-A")
elif x>80:
    print("Grade-B")
elif x>70:
    print("Grade-C")
elif x>60:
    print("Grade-D")
elif x>=50:
    print("Grade-E")
else:
    print("Grade-F") 
