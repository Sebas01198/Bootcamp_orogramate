# print("hola mundo")

print("me encanta aprender python")
print(555)

# strings

print("Hola" + " " + 'sebas')
print("me encanta \"aprender\" python")
print("esta es una linea \ny esta otra nueva linea")  # \n es para generar una nueva linea
print("\ty esta es la tercera linea")  # el \t es para tabular
print('this isn\'t a number')
print('esta es \\ una barra invertida')

print('A\tB\tC')
print('Barra Normal: /');

#Proyecto numero 1



#input
"""print(input("Ingrese su nombre: "))
print(input("ingrese su apellido: "))"""

print("Tu nombre es: " + input("ingresa tu nombre: ")+ " " + input("Ingresa tu apellido: "));

"""edad = int(input("ingrese la edad: "))

if(edad >= 65):
    print("es viejo, puede ingresar")
elif(edad >= 18):
    print("es joven, puede ingresar")
else:
    print("demasiado joven, no puede ingresar")

total = 0
while True:
    entrada = input("ingrese un numero o escriba \"Salir\" para salir del programa: ")
    if(entrada == "salir"):
        print("Programa Finalizado")
        break
    else:
        total =+ int(entrada)

for i in range(10,0,-1):
    print(i);"""

# ejercicios

# Pedir un numero y mostrar si es par o impar.

"""numero = int(input("ingrese un numero: "))
if(numero % 2 == 0):
    print("Es par")
else:
    print("es impar")"""

# Solicitar dos números y mostrar cual es el número mayor y menor.
"""numero1 = int(input("ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if(numero1 > numero2):
    print(f"el numero mayor es: {numero1}")
else:
    print(f"El numero mayor es: {numero2}")"""

"""Pedir un usuario y un password, verificar si estos son “admin” y “12345” respectivamente, 
si esto ocurre mostrar un mensaje de “Bienvenido” en caso contrario “Acceso denegado”."""

"""usuario = input("Ingrese un usuario: ")
password = input("ingrese una contraseña: ")

if(usuario == "admin" and password == "12345"):
    print("Bienvenido")
else:
    print("Acceso denegado, revisa tu usuario o contraseña")"""
