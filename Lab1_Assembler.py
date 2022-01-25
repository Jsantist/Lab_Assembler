'''
Organización de Computadoras y Assembler
Programa para calcular numeros binarios
Autores: José Pablo Santisteban Vargas, Brandon Sicay

'''

def CA2(lista):
    print("-------------------------------")
    #inicia conla lista ingresada por el usuario hola 
    print("lista ingresada: ")
    print("".join(lista))
    #busca todos los 1 y los convierte a 0, y vicebersa

    for i in range(len(lista)):

        number = int(lista[i])
        if number == 1 :
            lista[i] = '0'
        elif number == 0:
            lista[i] = '1'
    #junto todos los elementos de la nueva lista

    newLista="".join(lista)

#se realiza la suma de binarios (lista nueva +1)
    a = newLista
    b = "1"
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    resultado = ''

    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        resultado = ('1' if r % 2 == 1 else '0') + resultado

        carry = 0 if r < 2 else 1

    if carry != 0:
        resultado = '1' + resultado

    print("el complemento a 2 del número ingresado es: ")

    print(resultado.zfill(max_len))





def bin_a_dec(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal


incorrecto = True

#Verificación de ingreso de datos
while incorrecto:
    contador = 0
    print("-----------------------------------------------------------")
    numero = input('ingrese un número binario de 8 bits por favor ')
    listaBin = list(numero)
    if int(len(listaBin) == 8):
        try :
            for i in range(len(listaBin)):

                number = int(listaBin[i])
                if number == 1 or number == 0 :
                    print("verificado")

                elif number != 1 or number != 0:
                    print("el dígito: ",number,
                  " no es 0 o 1, por favor intentelo de nuevo ")
                    contador = contador +1

            if contador == 0 :
                incorrecto = False
        except Exception as e :
            print("error en el ciclo for", e)
    else:
        print("los bits ingresados no coinciden con la cantidad requerida (7)")

print("------------------------------------------------------")
print("el numero ingresado en decimales es:",bin_a_dec(numero))
print( CA2(listaBin))