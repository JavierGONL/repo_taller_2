<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## Taller 2

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
- luego cree una funcion que segun la cantidad de digitos cae en un if que era especifico para la cantidad de digitos y el maximo era 6 , pero vi que era muy ineficiente asi que la reduci reducirla
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
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```python



```
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. **Pista:** Puede ser de utilidad chequear el [Algoritmo de Euclides](https://es.wikipedia.org/wiki/Algoritmo_de_Euclides) para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.
### 7. Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
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

### 9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.

### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?

## Bono
### 11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

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
