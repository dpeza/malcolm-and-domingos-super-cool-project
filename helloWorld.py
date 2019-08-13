#dimitri this is a program that runs inputs for quadratic functions, im testing it.
cofX2 = input("Input coefficent for X^2 value: "))
cofX1 = input("Input coefficent for X value:  "))
integer = input("Input constant: "))
xVal = input(float("Input value being run: "))
xVal = float(xVal)
cofX2 = float(cofX2)
cofX1 = float(cofX1)
integer = float(integer)
yVal = cofX2*xVal*xVal+cofX1*xVal+integer
print(yVal)