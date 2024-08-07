#tras analizar el problema, me di cuenta de que esto es una condición bidireccional, en otras palabras, no hay casos especiales
#en casi lenguaje matemático sería:
# P<->Q, -> P->Q ^ Q->P
# Lo que procede aquí es extraer las cifras de los números, sin usar strings(porque se supone que no lo hemos visto ;) )
#Este proceso se hace para a en sentido izquierda->derecha, y b en sentido derecha->izquierda
#luego comparar las listas usando ==

#la siguiente función se basa en algo que se supone que no hemos visto, pero nos dejaron usar en el taller 1, y ayuda a que al programa no le hagan trampita, así que ahí va
def verificador(a:str,b:str):
    if (a.isdigit() and b.isdigit()): #no existen los números espejo negativos, ya que al leer de derecha a izquierda el símbolo "-" queda de últimas
        return True
    else:
        return False
#la parte del código que viene a continuación es un derivado de los ejercicios que se hicieron en clase para puntos extra en el examen
#yo no los logré hacer en clase
#pero ahora sí en casita y con más calma lo logré, entonces haré el código decentemente
def operador_a(a:int):
    lista_a=[]
    entrada=a
    longitud=0
    entrada_1=entrada
    while entrada_1>0:
        entrada_1//=10
        longitud+=1
    while longitud>0:
        cifra=entrada//10**(longitud-1)
        cifra=cifra%10
        longitud-=1
        lista_a.append(cifra)
    return lista_a
#la siguiente función es parecida a la anterior, solo que el proceso de sacar cifras se invierte
def operador_b(b:int):
    lista_b=[]
    entrada=b
    longitud=0
    entrada_1=entrada
    while entrada_1>0:
        entrada_1//=10
        longitud+=1
    longitud_1=0
    while longitud_1<longitud:
        cifra_2=entrada//10**(longitud_1)
        cifra_2=cifra_2%10
        longitud_1+=1
        lista_b.append(cifra_2)
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
        a=int(a)
        b=int(b)
        print(a+b)
        lista_a=operador_a(a)
        lista_b=operador_b(b)
        juicio=juzgador(lista_a,lista_b)
        if juicio==True:
            print("los números ",a," y ",b,"son números espejo")
        else:
            print("los números ingresados",a," y ",b," no son números espejo")
    else:
        print("no se han ingresado datos válidos, por favor intente de nuevo")