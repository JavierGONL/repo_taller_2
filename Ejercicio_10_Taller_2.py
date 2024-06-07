#Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, 
#tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. 
#Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. 
#Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?

# :D
lista_A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #esta es una lista de prueba
múltiplos_3=[] #aquí se añaden los múltiplos de 3
b=3
def múltiplos_3_list_comprenhension(lista_A:list,b:int):
    múltiplos_3=[a for a in lista_A if ((float(a/b)-(int(a/b)))==0)] 
    #aquí se revisa si la división de un número entre 3 da un resultado decimal, de darse el caso, no es múltiplo de 3
    return múltiplos_3
def múltiplos_3_patrón_acumulación(lista_A:list,b:int): 
    #en esta función, se suma 3 hasta que de el número deseado, si da, se agrega a la lista, si se pasa, no se agrega
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