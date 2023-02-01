# Joshua May
# 02/01/23
workhours = int(input('Enter number of work hours: '))

regular_hours = 40
overtime_hours = max(0, workhours - regular_hours)
regular_charge = regular_hours * 18.25
overtime_charge = overtime_hours * 27.78
total_wages = regular_charge + overtime_charge

print('Regular hours: ' + str(regular_hours))
print('Regular charge: $' + str(regular_charge),'\n')
print('Overtime Hours:' + str(overtime_hours))
print('Overtime charge: $' + str(overtime_charge),'\n')
print('Total wages: $' + str(total_wages))
