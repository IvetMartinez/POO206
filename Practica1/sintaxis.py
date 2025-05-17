
#1. Comentarios
#Comentarios de una sola linea
""""
Aquí se hace un comentario de varias
lineas  en python
"""
#2. strings
print("Hola soy una cadena") #1. forma
print('Hola soy la otra  cadena') #2. forma

variable1= "Hola soy la otra  cadena"
print(len(variable1)) #len 
print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

#3. Variables en python solicitud de datos

#No se podran iniciar el nombre de una variable con un número
#Python reconoce el tipo de 
#ejemplo
#x= "ivet"
#x=4
#x= 5.78

#x= int (3)
#y= float (3)
#z= str (3)
#print(x,y,z)
#print(type(x)) #función  type, arroga el ultimo tipo de dato al que corresponde
#print(type(y)) 
#print(type(z)) 

#4.Solicitud de datos
#a=input("Introduce cualquier dato:")
#b= int(input("introduce un numero entero"))
#c= float(input("Introduce un numero decimal:"))

#print(a,b,c)

#4. Booleanos, comparación y lógicos
print(10>9)
print(10<9)
print(10==9)
print(10>=9)
print(10<=9)
x=1
print (x<5 and x<10)
print (x<5 or x<10)
print (not(x<5 and x<10))
