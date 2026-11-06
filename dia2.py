#Ejercicio 1 Par o impar

entrada = input("Introduce un número entero: ")
numero = int(entrada)

if numero % 2 == 0:
    print ("Es par")
else:
    print ("Es impar")

#Ejercico 2 Validador de edad

entrada = input("Cuál es tu edad: ")
edad = int(entrada)

if edad < 18:
   print("menor de edad")
elif edad <= 64:
    print("adulto")
else:
    print("adulto mayor")

#Ejercicio 3 Tabla de resultados

for numero in range (1,21):
    if numero % 3 == 0:
        print(numero, "PASS")
   else:
       print(numero, "FAIL")


#Ejercicio 4 Contador de fallos

resultados = ["PASS", "FAIL", "PASS", "PASS", "FAIL"]
contador_pass = 0
contador_fail = 0

if len(resultados) == 0:
   print("No hay pruebas para evaluar")
else:    
    for result in resultados:
        if result=="PASS":
            contador_pass +=1
        else:
            contador_fail +=1

    print(contador_pass,"pruebas exitosas")
    print(contador_fail, "pruebas fallidas")

    porcentaje = contador_pass / len(resultados) * 100
    print("El porcentaje de éxito es: ", porcentaje)


#Ejercicio 5 Reintentos

import random
contador =0

while contador <3:
    resultado = random.choice([True, False])
    contador +=1
    if resultado:
        print("La prueba pasó en el intento", contador)
        break        
else:
    print("La prueba agotó los reintentos")