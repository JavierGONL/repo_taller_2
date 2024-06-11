def separador_de_digitos(numeroFloat):
    # se divide el numero racional por la division entera de 1 y devuelve solo la parte entera del numero
    separador_parte_entera = numeroFloat // 1
    # se le resta la parte entera al numero racional y el resultado son los decimales
    separador_parte_decimal = float(numeroFloat - int(separador_parte_entera))
    return print(f"la parte entera es: { separador_parte_entera} y la parte decimal es: {separador_parte_decimal}")
if __name__ == "__main__":
    numeroFloat = float(input("ingrese un numero racional : "))
    separador_de_digitos(numeroFloat)