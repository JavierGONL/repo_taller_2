#Desarrollar un algoritmo que determine si una matriz es mágica. 
#Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
#matriz_mágica_de_prueba=[[1,1,1],[1,1,1],[1,1,1]] # #1
matriz_mágica_de_prueba=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]] # #2
#matriz_mágica_de_prueba=[[8, 1, 6],[3, 5, 7],[4, 9, 2]] #3 *generada por chatgpt

#Tras considerar la situación, me di cuenta que para que una matriz sea mágica, debe ser cuadrada
verificador=[]
resultados_filas=[]#resultados sumas filas
resultados_columnas=[]
verificación_filas_columnas=[]
def verificacion_cuadradez(matriz_mágica_de_prueba:list,verificador:list):
    for f in matriz_mágica_de_prueba:
        if len(f)==len(matriz_mágica_de_prueba):
            verificador.append(1)
        else:
            verificador.append(0)
    if not(0 in verificador): #este pedazo verifica si la matriz es cuadrada
        return True
    else:
        return False
def operador_filas(matriz_mágica_de_prueba:list,resultados_filas:list):
    for f in matriz_mágica_de_prueba:
        suma_f_in=0
        for g in f:
            suma_f_in+=g
        resultados_filas.append(suma_f_in)
    #el siguiente pedazo verifica que la matriz cumpla la condición de las filas
    if resultados_filas.count(resultados_filas[0])==len(resultados_filas): #parece que esto funciona para todas las matrices mágicas
        return True
    else:
        return False
# el siguiente pedazo de código debería sumar las columnas
def operador_columnas(verificacion_filas,verificación_filas_columnas:list):
    for f in range(len(matriz_mágica_de_prueba)):
        suma_columnas=0
        for g in range(len(matriz_mágica_de_prueba)):
            suma_columnas+=matriz_mágica_de_prueba[g][f]
        resultados_columnas.append(suma_columnas)
    if verificacion_filas==True:
        for i in range(len(resultados_filas)):
            if resultados_filas[i]==resultados_columnas[i]:
                verificación_filas_columnas.append(1)
            else:
                verificación_filas_columnas.append(0)
    if not(0 in verificación_filas_columnas) and (not(verificacion_filas==False)):
        return True
    else:
        return False
def diagonales(matriz_mágica_de_prueba:list):
    #diagonales sentido izquierda->derecha
    suma_diagonal_izquierda_derecha=0
    for f in range(len(matriz_mágica_de_prueba)): # este pedazo debería servir para verificar que las diagonales sean mágicas
            suma_diagonal_izquierda_derecha+=matriz_mágica_de_prueba[f][f]
    #diagonales sentido derecha->izquierda
    suma_diagonal_derecha_izquierda=0
    for f in range(len(matriz_mágica_de_prueba)): # este pedazo debería servir para verificar que las diagonales sean mágicas
        g=-f-1 #descubriendo que este pedazo funcionaba me volví el ser humano más feliz del mundo
        suma_diagonal_derecha_izquierda+=matriz_mágica_de_prueba[f][g]
    if suma_diagonal_derecha_izquierda==suma_diagonal_izquierda_derecha:
        return True
    else:
        return False
def juzgador_final(condicion_diagonales,verificador_filas_columnas):
    if (verificador_filas_columnas and condicion_diagonales)==True:
        return True
    else:
        return False
if __name__=="__main__":
    verificador_inicio=verificacion_cuadradez(matriz_mágica_de_prueba,verificador)
    if verificador_inicio==True:
        verificacion_filas=operador_filas(matriz_mágica_de_prueba,resultados_filas)
        verificador_filas_columnas=operador_columnas(verificacion_filas,verificación_filas_columnas)
        condicion_diagonales=diagonales(matriz_mágica_de_prueba)
        juicio=juzgador_final(condicion_diagonales,verificador_filas_columnas)
        if juicio==True:
            print("Felicidades, la matriz ",matriz_mágica_de_prueba," es una matriz mágica")
        else:           
            print("Lastimosamente, la matriz ",matriz_mágica_de_prueba," no es mágica")
    else:
        print("no se ha ingresado una matriz que tenga los requisitos para ser candidata a mágica")
