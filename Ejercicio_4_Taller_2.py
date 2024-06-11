import math
# Se importa la librería math para poder usar la función coseno
def factorial (numeroN = int)->int:
    # Se crea una función que calcula el factorial de un número
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1) # se usa recursividad para calcular el factorial
def rango_de_error(numeroX, numeroN): 
    # Se crea una función que calcula el rango de error de la serie de Maclaurin del coseno con respecto a la función coseno de la librería math 
    maclaurin = funcion_coseno(numeroX, numeroN)
    math_cos = math.cos(numeroX)
    error_relativo = (math_cos - maclaurin) / math_cos # Se calcula el error relativo dividiendo la diferencia entre el coseno de math y el coseno de la serie de Maclaurin entre el coseno de math
    porcentaje_error = round(abs(error_relativo) * 100,5) # Se redondea el valor absoluto del error relativo multiplicado por 100 a 5 decimales
    return porcentaje_error
def funcion_coseno(numeroX , numeroN : int) -> float:
    # Se crea una función que calcula el coseno de un numero usando la serie de Maclaurin con un numero de términos dado
    resultado = 0
    for i in range(numeroN + 1):
        coseno_serie_maclaurin = ((-1) ** i) * ((numeroX) ** (2 * i)) / factorial(2 * i)
        resultado += coseno_serie_maclaurin
    return resultado
def iteraciones(numeroX: float) -> int:
    # se crea una funcion que calcula el numero de iteracion necesacirias para que el rango de error sea mas o nemos 10% , 1% , 0.1% y 0.01% , cuando es menor a 0.001 se detiene
    numeroN = 0
    # Se inicializan las variables que indican si ya se imprimio el resultado para el rango de error correspondiente y asi no imprimir en bucle estas variables
    print_10 = False
    print_1 = False
    print_01 = False
    print_001 = False
    while True:
        # se inicializa el bucle y se calcula el rango de error y el resultado de la funcion coseno con el numero de iteraciones actual 
        numeroN += 1
        error = rango_de_error(numeroX, numeroN)
        resultado = funcion_coseno(numeroX, numeroN)
        # inica el if para imprimir los resultados de los rangos de error segun el % de error que haya en esa iteracion
        if error <= 10 and not print_10:
            print(f"el rango de error es: {error} , el número de términos es: {numeroN} y el resultado es: {resultado}")
            print_10 = True
        elif error <= 1 and not print_1:
            print(f"el rango de error es: {error} , el número de términos es: {numeroN} y el resultado es: {resultado}")
            print_1 = True
        elif error <= 0.1 and not print_01:
            print(f"el rango de error es: {error} , el número de términos es: {numeroN} y el resultado es: {resultado}")
            print_01 = True
        elif error <= 0.01 and not print_001:
            print(f"el rango de error es: {error} , el número de términos es: {numeroN} y el resultado es: {resultado}")
            print_001 = True
        elif error <= 0.001:
            # cuando el % de error esta entre lo que queremos se detiene el bucle 
            break
    # se retorna el numero de iteraciones
    return numeroN
if __name__ == "__main__":
    # se pide que se ingrese un numero y se llama a la funcion iteraciones con el numero ingresado y se imprime el resultado
    numeroX = float(input("ingrese un numero: "))
    numeroN  = iteraciones(numeroX)
    print(f"el resultado aproximado de la funcion coseno es: {funcion_coseno(numeroX,numeroN)}, el verdadero es: {math.cos(numeroX)} y el rango de error es {rango_de_error(numeroX,numeroN)}%")