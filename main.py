# Problem_no 1
# calculate your age based on the current year and yoyr birth year
def agecalculator():
    birth_year:int = int(input("Enter your Birth-Year = ")) 
    current_year:int = int(input("Enter your Current-Year = "))
    print("Your age is = ",(current_year-birth_year))
    return print
output = agecalculator()
print("your age is =", output , "year")


#problem_2
#a program that calculate the area of a rectangle using lenght and width variables
def areacalculator():
   lenght:int = int(input("Enter the lenght of a rectangle = "))
   width:int = int(input("Enter the width of a rectangle = "))
   print("The area of your rectangle is = lenght*width = ",lenght*width,"square unit")
   return print
outputofarea = calculatearea()
print("the area of calculator:", outputofarea,"metersquared")

#Problem_no 3
#a program that calculate the area of a circle
print("Circle area calculator")
radius:int = int(input("enter the radius of = "))
pie_value:float =3.141592653589793238462643383279502884197
print("the area of circle is = value of pie *square of radius = ", pie_value*radius**2,"square unit")


#Problem_no4
#a program that calculates the area of cube
print("cube area calculator")
variable :int = 6
edges:int =int(input("enter number of edges here ="))
print("the area of cube is = 6*square of edges here =",6*edges**2,"meter cube")
#-------------------------------------------------------------------------------
print("\t Temperature Calculator")

print("Temperature Convertor (Celsius -> Fahrenheit)")
temperature = int(input("Enter your temperature in Celsius: "))
print("Temperature in Fahrenheit is: ", ((temperature * 9 / 5) + 32))

print("Temperature Convertor (Fahrenheit -> Celsius)")
temperature = int(input("Enter your temperature in Fahrenheit: "))
print("Temperature in Celsius is: ", ((temperature - 32) * 5 / 9))
#-------------------------------------------------------------------

#Problem_no6
#convert a number in seconds
print("Time Calculator")
time_minutes = int(input("Enter your time in minutes = "))
print("Time in second is = (time minutes*60) = ",(time_minutes*60) ,"sec")
#--------------------------------------------------------------------------------

#Problem_7
print("Percentage Calculator")
percentage = int(input("Enter your percentage: "))
marks = int(input("Enter your marks: "))
print("Percentage is: ", ((percentage / 100) * marks))

#--------------------------------------------------------------------------------

#Problem-no8
print("BMI Calculator")
weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print('Overweight')
else:
    print('Obesity')

 #-----------------------------------------------------------------------------
 # Problem-no9
print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
pie_value = 3.1416
print("Volume of Cylinder is: ", pie_value * (radius ** 2) * height)





