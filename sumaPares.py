#Hacer un funcion que Lea dos número enteros de dos digitos(+) y que 
# la funcion retorne
#la suma de los digitos pares.
#Ej : #1 -> 25 #2 -> 46  ..debe retornar 2 + 4 + 6  = 12 "

def sumaPares (a:int, b:int) -> int:
    suma = 0
    if (a >= 10 and a <= 99) and (b >= 10 and b <= 99) :
        digit1 = a // 10
        digit2 = a % 10
        
        digit3 = b // 10
        digit4 = b % 10
        if digit1 % 2 == 0 :
            suma = digit1
        if digit2 % 2 == 0 :
            suma = suma + digit2
        if digit3 % 2 == 0 :
            suma = suma + digit3
        if digit4 % 2 == 0 :
            suma = suma + digit4
    else:
        print("El número no es de 2 cifras.")
        
    return suma
    
a = int(input("Ingresa un numero de 2 cifras: "))
b = int(input("Ingresa otro numero de 2 cifras: "))

print("El resultdo de la suma de los digitos pares es: ", sumaPares(a,b))


            
            
