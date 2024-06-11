from Punto_6 import adicionlistanoarreglo
#Importamos la funcion del punto 6
if __name__ == "__main__":
    o:list=[]
    q:list=["A","E","I","O","U","a","e","i","o","u"]
    #Declaramos la lista a evaluar y otra con las posibles vocales
    adicionlistanoarreglo(o,False)
    #aplicamos la funcion
    for i in o:
        l:int=0
        #un for para recorrer los valores de la lista y declaramos una variable que regrese a cero a pasar al siguiente valor
        for j in i:
            #otro for para recorrer la cadena
            if j in q: 
                #si el valor pertenece a la lista de vocales se lesuma 1 a l
                l=l+1
            #ya con toda la cadena recorrida evaluamos el valor resultante de l antes de pasar a la siguiente cadena
        if l==1: print("La palabra "+i+" tiene "+str(l)+" vocal")
        elif l>1: print("La palabra "+i+" tiene "+str(l)+" vocales")
        else: print("En "+i+" no existen vocales o no es una cadena")

                
