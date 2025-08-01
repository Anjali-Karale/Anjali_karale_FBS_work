p = int(input("Enter principle amt"))
r = int(input("Enter rate"))
t = int(input("Enter time"))

compound_int = p*(1+r/100)**t-p

print(f'compound_int:{compound_int}')