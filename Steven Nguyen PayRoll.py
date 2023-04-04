#!/usr/bin/env python3

fedTaxRate = 0.1
stateTaxRate = 0.03
ficaTaxRate = 0.07
overTimeRate = 1.5

allEmpList = []


def inputData(x):
    empName = str(input("Enter Employee Name: "))
    hoursWorked = int(input("Enter the numbers of hours worked: "))
    payRate = int(input("Enter the hourly pay rate: $"))
    x.insert(0, empName)
    x.insert(1, hoursWorked)
    x.insert(2, payRate)
    return x


def grossPay(x):
    overTimeHours = x[1] - 40

    if x[1] > 40:
        grossP = ((x[2] * (x[1] - overTimeHours)) +
                  (x[2] * overTimeHours * overTimeRate))
    else:
        grossP = x[2] * x[1]

    x.insert(3, round(grossP))
    return x[3]


def deductions(x):

    empFedTax = x[3]*fedTaxRate
    empStateTax = x[3]*stateTaxRate
    empFICA = x[3]*ficaTaxRate
    x.insert(4, round(empFedTax))
    x.insert(5, round(empStateTax))
    x.insert(6, round(empFICA))
    totalDeduction = empFedTax + empStateTax + empFICA
    return totalDeduction


def netPay(x, y):
    netP = x - y
    return netP


def printOutPut(x):
    for i in range(len(x)):
        print(str(x[i]) + "\t\t", end=' ')
    return


print('************************************************\n')
print("Welcome to Steven Nguyen Corporation Payroll")
print("You are using Steven Nguyen Corporation Payroll Program \n")
print('************************************************\n')


empNum = int(input("How many employees do you want to display? :  "))
print("\n")

for j in range(empNum):
    empInfoList = []
    inputData(empInfoList)
    grossPay(empInfoList)
    totalD = deductions(empInfoList)
    empInfoList.append(round(netPay(empInfoList[3], totalD)))
    allEmpList.insert(j, empInfoList)
    print("\n")

print('View all the employee(s) Payroll information:')
print("\n")
print('***********************************************************************************************************************\n')
print("Name\tHours Worked\tpayRate($)\tgrossPay($)\tFed. Tax($)\tState Tax($)\tFICA($)\t\tNet Salary($)")
print('***********************************************************************************************************************\n')
for j in range(empNum):
    printOutPut(allEmpList[j])
    print('\n')
