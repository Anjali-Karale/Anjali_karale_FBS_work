feet = int(input("Enter distance in feet:"))
inches = int(input("Enter distance in inches:"))

total_meters = (feet * 0.3048) + (inches * 0.0254)

meters = int(total_meters)
centemeters = (total_meters - meters)*100

print(f'distance is in meter:{meters},distance is in centimeters:{centemeters}')