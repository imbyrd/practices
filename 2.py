#!/usr/bin/env python3
import sys
try:
    for m in sys.argv[1:]:
        sn_num = int(m.split(':')[0])
        salary = int(m.split(':')[1])
        starting_points = 3500
        insurance = int(salary) * 0.08 + int(salary) * 0.02 + int(salary) * 0.005 + int(salary) * 0.06
        taxable_income = int(salary) - insurance - starting_points
        if taxable_income < 0:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance)))
        elif taxable_income < 1500:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.03))))
        elif taxable_income < 1500:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.1 - 105))))
        elif taxable_income < 5500:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.2 - 555))))
        elif taxable_income < 9000:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.25 - 1005))))
        elif taxable_income < 35000:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.3 - 2755))))
        elif taxable_income < 55000:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.35 - 5505))))
        elif taxable_income > 80000:
            print('{:2d}:{:.2f}'.format(sn_num, (int(salary) - insurance - (taxable_income * 0.45 - 13505))))
except:
    print("Parameter Error")
