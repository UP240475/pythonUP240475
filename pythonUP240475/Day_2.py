#variables 
#Day 2: 30 Days of python programming

#puntos1-13
firstname= "patricio"
lastname= "romo"
fullname= "Patricio A. Romo Romero"
country= "Mexico"
city="Ags"
age= "19"
year= "2025"
is_married= False
is_true= False
is_light_on= False
skills= "cooking", "drive", "python"

#level 2

#puntos 1-3

print(type((firstname)))
print(len(firstname))
print(len(lastname)) 

if (firstname>lastname): 
    print("True")
else:
    print("False")
#puntos 4-11
num_one=5
num_two=4

resta= num_one-num_two

product= num_one*num_two
division= num_one/num_two
remainder= num_one%num_two
exp=num_one**num_two
floor_division=num_one//num_two

#punto 12

radio=30
pi=3.1416
area_of_circle= (pi*(radio**2))
print(area_of_circle)
circum_of_circle= (2*pi*radio)
print("area with 30 in radio: ", circum_of_circle)

radio_input = float(input("put the radio: "))

area_of_circle= (pi*(radio_input ** 2))
print(area_of_circle)
circum_of_circle= (2*pi*radio_input)
print(circum_of_circle)


# punto 13 con "_13" como separador de variables
first_name = input("nombre(s): ")
last_name = input("apellido(s): ")
country_13 = input("pais: ")
age_13 = input("edad: ")

print(first_name)
print(last_name)
print(country_13)
print(age_13)

#punto 14

help("keywords")

