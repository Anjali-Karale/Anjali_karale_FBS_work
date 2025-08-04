s1 = int(input("Enter side1:"))
s2 = int(input("Enter side2:"))
s3 = int(input("Enter side3:"))

if(s1 == s2 == s3):
    print("Equilateral triangle.")
elif(s1 == s2 or s2 == s3 or s1 == s3):
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")