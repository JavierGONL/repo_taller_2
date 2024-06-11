def adicionlistanoarreglo(l:list,k:bool):
    # Se crea una funcion para agregar listas
    i=1
    while i==1:
        e= input("ingresa un dato para la lista:")
        l.append(e)
        i=int(input("deseas ingresar otro dato? (1, cualquier otro numero para no)"))
    if k==True: print("nuestra primera lista fue: "+ str(l)+ ", la siguiente lista no debe tener mas de "+ str(len(l))+" elementos")
    else: print("nuestra lista fue: "+ str(l)+ ", tiene "+ str(len(l))+" elementos.")
    #2 opciones que solo cambian el mensaje de salida, para que tenga coherencia si se usa en ejercicos que necesiten 2 listas
if __name__=="__main__":
    p:bool=False
    lista1=[]
    lista2=[]
    adicionlistanoarreglo(lista1,False)
    for i in lista1:
        #para los valores de la lista evaluamos cuantas veces se repiten en la propia lista con el metodo count
        if lista1.count(i)!=1 and i in lista2!=True:
            print("Hay valores repetidos, siendo el numero "+str(i)+" el cual se repite "+str(lista1.count(i))+" veces")
            lista2.append(i)
            p=True
        #usamos un booleando para informar si hay o no valores repetidos ademas de agregar a los valores que pasen por una lista auxiliar para evitar que se repita el mensaje
    if p==True: 
        print("en la lista hay valores repetidos")
    else:
        print("No hay valores repetidos")
