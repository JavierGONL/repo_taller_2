"""
hice los algoritmos de MCD para entender mejor como hacer el MCM
y los uso para resolver el mcm de varias formas
"""
def maximo_comun_divisor_recursivo_resta(numeroA,numeroB)->int: # utiliza el algoritmo original de euclides
    # verifico cual es el mayor de ambos para que el algoritmo funcione
    if numeroA < numeroB:
        numeroA, numeroB = numeroB , numeroA
    elif numeroA == numeroB: # cuando son iguales es que el mcm es cualquiera de los dos
        return print(f"el maximo comun divisor es {numeroA}")
    numeroC = numeroA - numeroB # se va restando y el resultado se coloca de nuevo en la funcion
    maximo_comun_divisor_recursivo_resta(numeroC,numeroB)# calcula todo lo anterior hasta que numeroA y B sean iguales 
def maximo_comun_divisor_recursivo_division(numeroA,numeroB): # usa el algoritmo del teorema de Lamé
    # verifico cual es el mayor de ambos para que el algoritmo funcione
    if numeroA < numeroB:
        numeroA, numeroB = numeroB , numeroA
    if numeroA % numeroB == 0: # cuando el resuduo es igual a 0 cae en el return y retorna el numeroB 
        return print(f"el maximo comun divisor es {numeroB}")
    maximo_comun_divisor_recursivo_division(numeroB,numeroA % numeroB) # se invoca la funcion pasando los valores de B y el residuo de A / B
""" el algoritmo para sacar mcm del algoritmo para sacar mcd de euclides es 
    simplemente usar la formula mcm = ( A * B ) / mcd
"""
def minimo_comun_multiplo_recursivo(numeroA,numeroB)->int:
    return
def minimo_comun_multiplo_formula(numeroA,numeroB)->int:# en este uso la formula mcm = (AxB )/ mcd
    mcm = (numeroA*numeroB)/maximo_comun_divisor_recursivo_division(numeroA,numeroB)
    return mcm
def minimo_comun_multiplo_iterativo(numeroA,numeroB)->int:
    # verifico cual es el numero mayor para verificar si ese es mcm de ambos
    if numeroA > numeroB:
        numeroC = numeroA
    else:
        numeroC = numeroB
    while True:
        # se revisa que el mayor de ambos dividido entre a y b el residuo sea 0 
        if  numeroC%numeroA == 0 and numeroC % numeroB == 0:
            break
        # no se encontro el mcm entonces se suma 1 al mayor hasta que sea el mcm de ambos
        numeroC += 1
    return print(f"el mcm entre {numeroA} y el numero {numeroB}, es {numeroC}")

if __name__ == "__main__":
    numeroA = int(input("ingrese un numero: "))
    numeroB = int(input("ingrese un numero: "))
    maximo_comun_divisor_recursivo_division(numeroA,numeroB)