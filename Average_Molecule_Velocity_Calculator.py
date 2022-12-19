from decimal import Decimal
import math as m
print('Average Molecule Velocity Calculator:')
temp = int(input('To calculate the average velocity of a molecule in a sample of oxygen,\nEnter Temperature in Celsius: '))
absolute_temp = temp + 273
root_meant = Decimal(m.sqrt((3 * 8.3145)*absolute_temp/3.2E-2))
print('The average velocity or root mean square velocity of a molecule in a sample\nof oxygen at', temp,'degrees Celsius is',root_meant.quantize(Decimal('1.000')),'m/sec')

