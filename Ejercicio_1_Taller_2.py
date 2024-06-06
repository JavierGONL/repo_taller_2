import math
def contar_digitos(numero : int )-> int:
    if numero == 0: # Si el número es 0 igualmente tiene un dígito
        return 1
    else:
        return int(math.log10(numero)) + 1 # Se calcula el logaritmo en base 10 del número y se le suma 1 para obtener la cantidad de dígitos
def separador_digitos(numero: int = 0): # esta funcion la hice despues de crear la otra re larga
    digitos = [] # creo la lista en la que iran los digitos
    for i in range(contar_digitos(numero),0,-1): # en el for voy desde la cantidad de digitos hasta 0
        if i % 2 == 1: # si el numero es impar osea i%2 == 1
            digitos.append(numero // 10**(i-1)%10) # se aplica esta funcion que recorre los numeros desde la izquierda hasta el digito i y luego desde la derecha hasta el numero i
        else:# si es par
            digitos.append((numero % 10**(i)) // 10**(i-1)) #se aplica esta funcoin que recorre los numeros desde la derecha hasta i y luego desde la izquierda hasta i
    string_digitos = str
    for i in digitos:
        string_digitos = ' '.join(i)
    return print(f"El numero {numero} tiene {len(digitos)} digitos y son: {string_digitos}") 
if __name__ == "__main__": 
    # se pide que se ingrese un numero y luego se llama a la funcion separador_digitos y se ingrese el numero
    numero = int(input("Ingrese un numero: "))
    separador_digitos(numero)