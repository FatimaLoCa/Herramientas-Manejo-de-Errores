import os
import re

def ejemplo1(): #Ejemplo try except

    print("...Este programa suma dos numeros reales...")
    try:
        numero1 = float(input('Ingresa un numero: '))
        numero2 = float(input('Ingresa otro numero: '))
    except:
        print("Por favor ingresa solo numeros validos")
    else:
        suma = numero1 + numero2
        print("La suma de los numeros es: ",suma)
    
def ejemplo2(): #Ejemplo validación
    print("...Este programa valida la entrada correcta de un correo electronico...")
    incorrecto = True
    exp_correo = re.compile(r'^[\w]+(.[\w]+)[^()]*@[\D]*(.[a-z]{2,4})$')

    while(incorrecto):
        correo = input('Ingresa el correo a validar: ')

        if exp_correo.search(correo):
            print("Correo valido")
            incorrecto = False
        else:
            print("Correo invalido... intentalo de nuevo")
            
            
    

def main():
    ejemplo2()

if __name__ == "__main__":
    main()