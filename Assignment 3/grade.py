m1=int(input("Enter the subject 1:"))
m2=int(input("Enter the subject 2:"))
m3=int(input("Enter the subject 3:"))
m4=int(input("Enter the subject 4:"))
m5=int(input("Enter the subject 5:"))

total_marks = m1 + m2 + m3 + m4 + m5

average = total_marks / 5
print("average",average)

if(average >= 90):
    print("first class")
elif(average >= 80):
    print("second class")
elif(average >= 70):
    print("third class")
else:
    print("fail")