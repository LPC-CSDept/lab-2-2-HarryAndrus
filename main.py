# Joshua May
# 02/01/23
def main():

    workhours = int(input('Enter number of work hours: '))

    regular_hours = 40
    overtime_hours = max(0, workhours - regular_hours)
    regular_charge = regular_hours * 18.25
    overtime_charge = overtime_hours * 27.78
    total_wages = regular_charge + overtime_charge
          
    print(f'Regular Hours: {regular_hours}\nRegular charge: ${regular_charge}\n')
    print(f'Overtime Hours: {overtime_hours}\nOvertime charge: ${overtime_charge}\n')
    print(f'Total wages: ${total_wages}')

if __name__ == '__main__':
    main()

