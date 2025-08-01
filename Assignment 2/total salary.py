basic = int(input("Enter basic salary:"))

da_amt = basic * 0.1
ta_amt = basic * 0.12
hra_amt = basic * 0.15

total_sal = basic + da_amt + ta_amt + hra_amt

print(f'total_salary:{total_sal}')