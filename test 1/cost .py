area = float(input("Enter area of one wall:"))
interior_cost = float(input("Enter the interior_cost:"))
exterior_cost = float(input("Enter the exterior cost:"))

total_walls = 8

interior_total = total_walls * area * interior_cost
exterior_total = total_walls * area * exterior_cost

print(f'interior_cost:{interior_cost}')
print(f'exterior_cost:{exterior_cost}')