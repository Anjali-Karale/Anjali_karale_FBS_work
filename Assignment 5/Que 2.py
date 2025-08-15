num_students = int(input("Enter number of students: "))

percentages = []

for i in range(num_students):
    print(f"\nEntering marks for student {i+1}:")
    total = 0
    for j in range(5):
        marks = float(input(f"Enter marks for subject {j+1}: "))
        total += marks
    percentage = (total / 500) * 100
    percentages.append(percentage)

print("\nPercentages of Students:")
for i, p in enumerate(percentages, 1):
    print(f"Student {i}: {p:.2f}%")

average_percentage = sum(percentages) / num_students
print(f"\nAverage Percentage: {average_percentage:.2f}%")
