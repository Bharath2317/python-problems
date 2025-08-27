year = int(input("Enter a year: "))

if (year%400==0 or year%4 == 0 and year%100 != 0):
  print('{0} is a leap year'.format(year))
else: print("It is not a leap year")  