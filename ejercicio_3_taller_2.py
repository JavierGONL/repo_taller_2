#tras analizar el problema, me di cuenta de que esto es una condición bidireccional, en otras palabras, no hay casos especiales
#en casi lenguaje matemático sería:
# P<->Q, -> P->Q ^ Q->P
# Optaré por la opción que es hacer menos trampa, que es convertir los números a strings
#luego poner estos carácteres en una lista, para a en sentido izquierda->derecha, y b en sentido derecha->izquierda
#luego comparar las listas usando ==
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