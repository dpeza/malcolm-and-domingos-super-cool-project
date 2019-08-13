#dimitri this is a program that runs inputs for quadratic functions, im testing it.
cofX2 = input(float("Input coefficent for X^2 value: "))
cofX1 = input(float("Input coefficent for X value:  "))
integer = input(float("Input constant: "))
xVal = input(float("Input value being run: "))
yVal = cofX2*xVal*xVal+cofX1*xVal+integer
print(yVal)