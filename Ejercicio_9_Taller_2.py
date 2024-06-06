def promedio(*promedio_args)-> float:
    # utilizo una variable para ir sumando cada numero del arreglo
    suma = 0
    for i in promedio_args:
        suma += i
    return suma / len(promedio_args) # se retorna la suma dividida por la longitud del arreglo
def mediana(*mediana_args)->float:
    sorted(mediana_args)
    if len(mediana_args) % 2 != 0:#si la mediana no es par
        mediana = len(mediana_args) // 2
        return mediana_args[mediana]
    else: # si la mediana es par 
        mediana = len(mediana_args) // 2
        return (mediana_args[mediana - 1] + mediana[mediana])/2
def promedio_multiplicativo(*promedio_m_args)->float:
    multiplicacion = 0 #creo una variable para ir acomulando la multiplicacion de cada numero del arreglo
    for i in (promedio_m_args):
        multiplicacion *= i
    return multiplicacion ** (1/len(promedio_m_args)) # devuelvo la raiz n (n=longitud del arreglo)de la multiplicacion 
def ordenar_mayor_menor(*ordenar_M_m):
    return sorted(ordenar_M_m , reverse=True) # aca simplemente ordeno el arreglo y le coloco que sea de mayor a menor
def ordenar_menor_mayor(*ordenar_m_M):
    return sorted(ordenar_m_M) # aca un sorted normal y de una lo ordena de menor a mayor
def potencia_mayor_elevado_menor(*potencia_args)->int:
    potencia_args = sorted(potencia_args) # ordeno el arreglo
    return potencia_args[-1]**potencia_args[0] # retorno el mayor que estando ordenado es el indice[-1] elevado al indice[0] que es el menor
def raiz_cubica_menor_numero(*raiz_args):
    raiz = sorted(raiz_args) # primero ordeno para saber que el menor esta en el indice [0]
    return raiz[0]**(1/3) # retorno el indice [0] elevado al 1/3 que es lo equivalente a raiz cubica 
if __name__ == "__main__":
    # el codigo que use para verificar que funcione cada uno
    numeroA = int(input(" ingrese un numero: "))
    numeroB = int(input(" ingrese un numero: "))
    numeroC = int(input(" ingrese un numero: "))
    numeroD = int(input(" ingrese un numero: "))
    numeroE = int(input(" ingrese un numero: "))
   
    print(f"el promedio de {numeroA,numeroB,numeroC,numeroD,numeroE}, es {promedio(numeroA,numeroB,numeroC,numeroD,numeroE)} ")
    print(f"la mediana de {numeroA,numeroB,numeroC,numeroD,numeroE} es {mediana(numeroA,numeroB,numeroC,numeroD,numeroE)}")
    print(f"el promedio multiplicativo de {numeroA,numeroB,numeroC,numeroD,numeroE} es {promedio_multiplicativo(numeroA,numeroB,numeroC,numeroD,numeroE)}")
    print(f"los numeros {numeroA,numeroB,numeroC,numeroD,numeroE} ordenados de mayor a menor es {ordenar_mayor_menor(numeroA,numeroB,numeroC,numeroD,numeroE)} ")
    print(f"los numeros {numeroA,numeroB,numeroC,numeroD,numeroE} ordenados de menor a mayor es {ordenar_menor_mayor(numeroA,numeroB,numeroC,numeroD,numeroE)} ")
    print(f"la potencia del mayor elevado al menor es {potencia_mayor_elevado_menor(numeroA,numeroB,numeroC,numeroD,numeroE)} ")
    print(f"la raiz cubica del menor numero es {raiz_cubica_menor_numero(numeroA,numeroB,numeroC,numeroD,numeroE)} ")