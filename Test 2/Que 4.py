height = int(input("Enter height:"))
width = int(input("Enter width:"))

total_walls = 4
area = height * width

interior_cost = total_walls * area

print("cost of painting:", interior_cost)