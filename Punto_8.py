from Punto_6 import adicionlistanoarreglo
#importamos la funcion de listas
if __name__=="__main__":
    a:list=[]
    b:list=[]
    q:list=[]
    #creamos 3 listas las 2 iniciales y la resultante
    adicionlistanoarreglo(a,True)
    adicionlistanoarreglo(b,False)
    #agreagamos los valroes a las listas
    for i in a:
        #recorremos la primera lista
        if i in b:
            #si el valor de la primera lista esta en la segunda se salta
            continue
        q.append(i)
        #en caso contrario se agrega a la lista resultante
    print("La lista resultante es: "+str(q))
    #se muestra el resultado