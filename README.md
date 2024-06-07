<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# Taller 2
----------------------------------

### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. **Pista:** Utilice los operadores módulo (%) y división entera (//).
```python
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
```
#### explicacion:
- primero cree una funcion que contaba la cantidad de digitos de la funcion, esta calcula la cantidad de digitos usando el log en base 10 del numero y a este le sumo 1
- luego cree una funcion que segun la cantidad de digitos cae en un if que era especifico para la cantidad de digitos y el maximo era 6 , pero vi que era muy ineficiente asi que decidi reducirla
```python 
#esta era la funcion original hasta que corregi
def separador_digitos(numero: int = "")-> str: # Se crea una función que separa los dígitos de un número, hay 6 casos, el maximo es 6  osea no soporta numeros mayores a 999999
    if contar_digitos(numero) == 1: # Si el número tiene un dígito el mismo es el primer dígito
        primerDigito = numero
        print(f"El número tiene un dígito y es: {primerDigito}")
    elif contar_digitos(numero) == 2: # Si el número tiene el primero se calcula dividiendo por 10 y usando la división entera, el segundo se calcula con el módulo de 10
        primerDigito = numero // 10
        segundoDigito = numero % 10
        print(f"El número tiene dos dígitos y son: {primerDigito} y {segundoDigito}")
    elif contar_digitos(numero) == 3: # si el numero tiene 3 digitos se calcula dividiendo por 100 y usando la division entera, el segundo se calcula con el modulo de 100 y se divide por 10 y el tercer digito se calcula con el modulo de 10
        primerDigito = numero // 100
        segundoDigito = (numero % 100) // 10
        tercerDigito = numero % 10
        print(f"El número {numero}tiene tres dígitos y son: {primerDigito}, {segundoDigito} y {tercerDigito}")
    elif contar_digitos(numero) == 4: # si el numero tiene 4 digitos se calcula dividiendo por 1000 y usando la division entera, el segundo se calcula con el modulo de 1000 y se divide por 100, el tercer digito se calcula con el modulo de 100 y se divide por 10 y el cuarto digito se calcula con el modulo de 10
        primerDigito = numero // 1000
        segundoDigito = (numero % 1000) // 100
        tercerDigito = (numero % 100) // 10
        cuartoDigito = numero % 10
        print(f"El número {numero} tiene cuatro dígitos y son: {primerDigito}, {segundoDigito}, {tercerDigito} y {cuartoDigito}")
    elif contar_digitos(numero) == 5: # si el numero tiene 5 digitos se calcula dividiendo por 10000 y usando la division entera, el segundo se calcula con el modulo de 10000 y se divide por 1000, el tercer digito se calcula con el modulo de 1000 y se divide por 100, el cuarto digito se calcula con el modulo de 100 y se divide por 10 y el quinto digito se calcula con el modulo de 10
        primerDigito = numero // 10000
        segundoDigito = (numero % 10000) // 1000
        tercerDigito = (numero % 1000) // 100
        cuartoDigito = (numero % 100) // 10
        quintoDigito = numero % 10
        print(f"El número {numero} tiene cinco dígitos y son: {primerDigito}, {segundoDigito}, {tercerDigito}, {cuartoDigito} y {quintoDigito}")
    elif contar_digitos(numero) == 6: # si el numero tiene 6 digitos se calcula dividiendo por 100000 y usando la division entera, el segundo se calcula con el modulo de 100000 y se divide por 10000, el tercer digito se calcula con el modulo de 10000 y se divide por 1000, el cuarto digito se calcula con el modulo de 1000 y se divide por 100, el quinto digito se calcula con el modulo de 100 y se divide por 10 y el sexto digito se calcula con el modulo de 10
        primerDigito = numero // 100000
        segundoDigito = (numero % 100000) // 10000
        tercerDigito = (numero % 10000) // 1000
        cuartoDigito = (numero % 1000) // 100
        quintoDigito = (numero % 100) // 10
        sextoDigito = numero % 10
        print(f"El número {numero} tiene seis dígitos y son: {primerDigito}, {segundoDigito}, {tercerDigito}, {cuartoDigito}, {quintoDigito} y {sextoDigito}")
    # se podria ampliar mas pero dejare asi es suficiente para lo que se pide
```
-  cree la funcion reducida separar_digitos que basandose en si es impar se aplica la funcion (numero // 10**(i-1)%10) que recortaba primero los numeroes desde la izquierda y luego desde la derecha hasta el numero i si la funcion era par utilizaba esta otra funcion ((numero % 10**(i)) // 10**(i-1)) que recortaba la funcion por la derecha hasta el numero i y luego la recortaba por la izquierda hasta el numero i
- luego cree un for que unia en un texto separado por un espacio los digitos que estaban en la lista digitos
-----------------------------------
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```python
def separador_de_digitos(numeroFloat): # reutilice parte del punto anterior
    # se divide el numero racional por la division entera de 1 y devuelve solo la parte entera del numero
    separador_parte_entera = numeroFloat // 1
    # se le resta la parte entera al numero racional y el resultado son los decimales
    separador_parte_decimal = float(numeroFloat - int(separador_parte_entera))
    return print(f"la parte entera es: { separador_parte_entera} y la parte decimal es: {separador_parte_decimal}")
if __name__ == "__main__":
    numeroFloat = float(input("ingrese un numero racional : "))
    separador_de_digitos(numeroFloat)
```
#### explicacion:
- cree la funcion que para la parte entera del numero simplemente hace la division entera del numero entre 1 (n//1) y para la parte decimal le resto al numero original la parte entera y me devuelve solamente la parte decimal
----------------------------------
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
```python
def verificador(a:str,b:str):
    if (a.isdigit() and b.isdigit()): #no existen los números espejo negativos, ya que al leer de derecha a izquierda el símbolo "-" queda de últimas
        return True
    else:
        return False
def operador_a(a:str):
    lista_a=[]
    for d in range(len(a)):
        lista_a.append(a[d])
    return lista_a
def operador_b(b:str):
    b=str(b)
    lista_b=[]
    for c in range(len(b)-1,-1,-1):
        lista_b.append(b[c])
    return lista_b
def juzgador(lista_a:list,lista_b:list):
    if lista_a==lista_b:
        return True
    else:
        return False
if __name__=="__main__":
    a=input("introduzca su primer número")
    b=input("introduzca su segundo número:")
    verificar=verificador(a,b)
    if verificar==True:
        lista_a=operador_a(a)
        lista_b=operador_b(b)
        juicio=juzgador(lista_a,lista_b)
        if juicio==True:
            print("los números ",a," y ",b,"son números espejo")
        else:
            print("los números ingresados",a," y ",b," no son números espejo")
    else:
        print("no se han ingresado datos válidos, por favor intente de nuevo")
```
#### explicacion:
- Tras analizar el problema, me di cuenta de que esto es una condición bidireccional, lo que en casi lenguaje matemático sería: P<->Q, -> P->Q ^ Q->P .
- Opté por la opción que es hacer menos trampa, que es convertir los números a strings, luego añadir estos carácteres a una lista, para `a` en sentido izquierda->derecha, y `b` en sentido derecha->izquierda.
- luego simplemente comparar las listas usando `==`, si ambas listas son iguales, los dos números son números espejo.
----------------------------------
### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
```python
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
```
#### explicacion:
----------------------------------
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. **Pista:** Puede ser de utilidad chequear el [Algoritmo de Euclides](https://es.wikipedia.org/wiki/Algoritmo_de_Euclides) para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
```python
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
```
#### explicacion:
- por hacer
----------------------------------
### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.
```python
```
#### explicacion:
----------------------------------
### 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
```python
```
#### explicacion:
----------------------------------
### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. **Ejemplo:**
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

```python
```
#### explicacion:
----------------------------------
### 9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
```python
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
```
#### explicacion:
- cree las funciones con el (*args) para poder anadir cualquier cantidad de datos e hice la logica de cada funcion trabajando con vectores (el mismo codigo tiene explicacion de cada funcion).
----------------------------------
### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
```python
lista_A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #esta es una lista de prueba
múltiplos_3=[] #aquí se añaden los múltiplos de 3
b=3
def múltiplos_3_list_comprenhension(lista_A:list,b:int):
    múltiplos_3=[a for a in lista_A if ((float(a/b)-(int(a/b)))==0)] #aquí se revisa si la división de un número entre 3 da un resultado decimal, de darse el caso, no es múltiplo de 3
    return múltiplos_3
def múltiplos_3_patrón_acumulación(lista_A:list,b:int): #en esta función, se suma 3 hasta que de el número deseado, si da, se agrega a la lista, si se pasa, no se agrega
    múltiplos_3=[]
    for a in lista_A:
        while b<a:
            (b)+=3
        if b==a:
            múltiplos_3.append(a)
    return múltiplos_3
        
if __name__=="__main__":
    múltiplos_3_l=múltiplos_3_list_comprenhension(lista_A,b)
    print("los múltiplos de 3 obtenidos de la lista usando list comprenhension son: ",múltiplos_3_l)
    múltiplos_3_a=múltiplos_3_patrón_acumulación(lista_A,b)
    print("los múltiplos de 3 obtenidos de la lista usando patrones de acumulación son: ",múltiplos_3_a)
```
#### explicacion:
- Aunque no se emplea la perspectiva sugerida por el docente, tanto la list comprenhension (descartar números haciendo "división entera" sin usar `%`) como los patrones de acumulación (sumar de a 3 hasta que resulte el número deseado y agregarlo a una lista, y si se pasa descartarlo) brindan el mismo resultado.
----------------------------------
## Bono
### 11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
```python
```
#### explicacion:
----------------------------
## Condiciones de entrega:

<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Item</b></th>
    <th><b>Condición</b></th>
	</tr>
	<tr style="text-align: left; vertical-align: middle;" bgcolor="#e4e4ed">
		<td style="color:#141414">Entregables</td>
    <td style="color:#141414">Se debe elaborar un repo donde presente la solución a todos los problemas planteados. Para los puntos impares debe realizar un programa individual con extensión <i>.py</i> y para los pares debe elaborar un notebook <i>.ipynb</i> con las soluciones. El repo debe contener la explicación de la solución de cada punto. Todos los archivos se deben adjuntar al repo.<br>
    El repo debe ir con los integrantes del equipo, el nombre del grupo y un logo genial.
    </td>
	</tr>
  <tr style="text-align: left; vertical-align: middle;" bgcolor="#e4e4ed">
    <td style="color:#141414">Fecha</td>
    <td style="color:#141414">28/10/2023 Max: 22:00<br>Se creará el canal taller 2 con un archivo de Google Sheets donde se debe colocar la dirección del repo, si éste tiene un commit posterior al corte, se toma como referencia el más cercano a la fecha establecida.</td>
	</tr>
  <tr style="text-align: left; vertical-align: middle;" bgcolor="#e4e4ed">
    <td style="color:#141414">Forma de trabajo</td>
    <td style="color:#141414">Grupal</td>
	</tr>
  <tr style="text-align: left; vertical-align: middle;" bgcolor="#e4e4ed">
    <td style="color:#141414">Condiciones Extra</td>
    <td style="color:#141414">
    Los códigos elaborados deben estar apropiadamente comentados.<br>
    Todos los programas deben incorporar el uso de funciones.</td>
	</tr>
</table>
