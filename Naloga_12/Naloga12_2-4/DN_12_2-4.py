from funct import cube_function, steps_counter, absolute_difference

print("These function calculate the cube of the entered number!")

x = int(input("Enter the number: "))
cube = cube_function(x)
print("The cube of number " + str(x) + " is " + str(cube))

print('\n')

print("This function calculate the number of steps!")

dist = int(input("Please enter the distance in centimeters: "))

step_leng = int(input("Please enter the length of your step in centimeters: "))
steps = round((steps_counter(dist, step_leng)), 2)

dist_m = dist/100

print("You made " + str(steps) + " steps, while walking " + str(dist_m) + " meters.")

print('\n')

print("The next function shows the absolute deference between two numbers.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

abs_dif = absolute_difference(num1, num2)

print("Absolute difference between " + str(num1) + " and " + str(num2) + " is: " + str(abs_dif))

