#Operators
#30 Days Of Python: Day 3

#1-3
""" 
age = 19
heigth = 1.72
complex_number = complex

#4. Area of triangle
base_triangle = float(input("introduce la base: "))
heigth_triangle = float(input("introduce la altura: "))

area_triangle = base_triangle * heigth_triangle * 0.5

print("El área de un triángulo con base de",base_triangle,"y altura de",heigth_triangle,"es",area_triangle)

#5. Perimeter of triangle
sidea_triangle = float(input("introduce el lado a: "))
sideb_triangle = float(input("introduce el lado b: "))
sidec_triangle = float(input("introduce eñ lado c: "))

perimeter_triangle = sidea_triangle + sideb_triangle +sidec_triangle

print("El perímetro de un triangulo cuyos lados miden",sidea_triangle,sideb_triangle,sidec_triangle,"es",perimeter_triangle)

#6. Area and perimeter of a rectangle 
base_rectangle = 20
heigth_rectangle = 10

a_rectangle = base_rectangle * heigth_rectangle 
p_rectangle = 2 * (base_rectangle + heigth_rectangle)

print("El área de un rectángulo con base de",base_rectangle,"y altura de",heigth_rectangle,"es",a_rectangle,"y su perímetro es de",p_rectangle)

#7. Area and circumference of a circle
pi = 3.14
radius = 3

a_circle = pi * radius * radius 
circum = 2 * pi * radius

print("El área del círculo es de",a_circle,"y su circunferencia es de",circum, "cuando tiene un radio de",radius)

#8. Slope and Euclidian distance

x = float(input("introduce el valor de X"))
y = (2*x) - 2

print("El punto en el eje x es: ", x ,"y el punto en el eje Y es: ")


# Punto 9 slope...

y1 = float(input("introduce el valor de y1: "))
y2 = float(input("introduce el valor de y2: "))
x1 = float(input("introduce el valor de x1: "))
x2 = float(input("introduce el valor de x2: "))

slope = (y2-y1)/(x1-x2)

print("la cordenada es: ", slope)

#9 Euclidean distance

x1, y1 = 2, 2
x2, y2 = 6, 10

# Calcular la pendiente (slope)
m = (y2 - y1) / (x2 - x1)

# Calcular la distancia euclidiana
ED = 0.5**((x2 - x1)**2 + (y2 - y1)**2)


print("Pendiente (m):", m)
print("Distancia Euclidiana:", ED)

#10 comparative 

if (m>ED): 
    print("True")
else:
    print("False")

#punto 11 

x1_ej11 = 1
x2_ej11 = 2
x3_ej11 = -3
y1 = x1_ej11**2 + 6*x1_ej11 + 9
y2 = x2_ej11**2 + 6*x2_ej11 + 9
y3 = x3_ej11**2 + 6*x3_ej11 + 9

print("El valor con 1, 3 y -3 respectivamente son: ", y1, y2, y3)
"""
#punto 12

palabra1 = 'python'
palabra2 = 'dragon'

len1 = len(palabra1)
len2 = len(palabra2)

print("Length of 'python':", len1)
print("Length of 'dragon':", len2)

if (len1>len2): 
    print("True")
elif(len1==len2):
    print("They are the same length ")
else:
    print("False")
