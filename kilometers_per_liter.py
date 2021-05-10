#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#10 May 2021
"""
Drivers are concerned with the mileage obtained by their automobiles. One driver has kept
track of several tankfuls of gasoline by recording kilometers driven and liters used for each tankful. Develop
a Python program that prompts the user to input the kilometers driven and liters used for each tankful.
The program should calculate and display the kilometers per liters obtained for each tankful. After
processing all input information, the program should calculate and print the combined kilometers per liters
obtained for all tankful (= total kilometers driven divide by total liters used).
"""


driver_name = input("Enter the name of the driver or 'Done' :")
total_kilometer = 0
total_liters = 0

while (driver_name != "Done"):
    mileage = int(input("Enter the kilometers driven : "))
    liters = float(input("Enter the liters used: "))

    miles_per_liter = mileage / liters

    print(f"kilometers per liters  for {driver_name} is: {miles_per_liter} KM per liter" )
    
    total_kilometer += mileage
    total_liters += liters
    total_kilo_per_lit = total_kilometer / total_liters
    
    
    driver_name = input("Enter the name of the driver or 'Done' :")
    
print (f"Combined kilometers per liters is {total_kilo_per_lit} KM per liter")