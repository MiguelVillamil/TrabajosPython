import random
from termcolor import colored 

def NumRand():
  random.seed()
  x=random.randint(0,100)
  
  return x

def NumRandPer(x,y):
  random.seed()
  x=random.randint(x,y)
  
  return x

def depuraNum():
  nValido=False
  while (nValido==False):
    try:
      n= int (input(colored("ingrese el numero deseado: \n","yellow")))
      nValido=True
    except ValueError:
      print(colored("el cararcter ingresado no es un numero ingrese el valor nuevamente \n","red"))
      nValido=False
  return n 

def finalizar():
  print(colored("Programa finalizado","red") )



def menu():
  print(colored("Ejercicio numero aleatorio \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. numero aleatorio entre 0 y 100\n","green"))
  print(colored("2. numero aleatorio valores personalizados\n","green"))
  print(colored("3. salir\n","red"))
  respuesta= input("")
  return respuesta



def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
        print(colored("su numero aleatorio es: ","yellow") )
        print(colored(str(NumRand()) + "\n","green") )
        continuar()
      
    elif(opcion=="2"):
        print(colored("rango minimo\n", "yellow") )
        x = depuraNum()
        print(colored("rango maximo\n", "yellow") )
        y = depuraNum()
        print(colored("su numero aleatorio entre " + str(x) +" y " + str(y) + "es: ","yellow") )
        print(colored(str(NumRandPer(x,y)) + "\n","green") )
        continuar()
    elif(opcion=="3"):   
        salida=True
        print(colored("Gracias por usar el programa\n","red") )
        finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()         