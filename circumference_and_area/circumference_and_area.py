import math

import datetime as dt

def getInput():
   
   radius = float(input("Enter the radius of the circle: "))

   precision = input("Enter the number of decimal places fo calculation: ")
   
   return radius, precision

def showCalculations(circumference, area, precision):
    
    # outputs to user
    # print("Circumference: ", circumference)
    # print("Area: ", area)

    # Interpolation (via f-string)
    # specifying what is run in the {} 10 means allocating ten character spaces 
    # 3 means round to the 3rd decimal place f means float while d mean integer
    # print(f"{'Circumference:':>15s} {circumference:>10.3f}")
    # print(f"{'Area:':>15s} {area:>10.3f}")
    
    print(f"{'Circumference:':>15s} {circumference:>10.{precision}f}")
    print(f"{'Area:':>15s} {area:>10.{precision}f}")

    timestamp = dt.datetime.today()
    print("Calculations made on", timestamp)

def main():
   
    # get the radius from the user
    radius, precision = getInput()

    # calculate the circumference
    circumference = 2 * math.pi * radius

    # calculate the area
    area = math.pi * math.pow(radius, 2)

    showCalculations(circumference, area, precision)


main()