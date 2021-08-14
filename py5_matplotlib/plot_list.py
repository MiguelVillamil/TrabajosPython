from termcolor import colored 
import matplotlib.pyplot as plt

def finalizar():
  print(colored("Programa finalizado","red") )

def menu():
  print(colored("Ejercicio Crear lista \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. crear lista ejemplo 2\n","green"))
  print(colored("2. salir\n","red"))
  respuesta= input("")
  return respuesta

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def creaLista(n):
  lista=[]
  lista.append(n) 
  while (n!=1):
    if (n%2==0):
      n = siPar(n)
    else:
      n = siImpar(n) 
    lista.append(n)
    print(lista)   
  return lista   

def siPar(n):
    return n//2

def siImpar(n):
    return (3*n)+1

def depuraN():
  nValido=False
  while (nValido==False):
    try:
      n= int (input(colored("ingrese el numero deseado: \n","yellow")))
      if (n>0):
        nValido = True

      else:
        print(colored("No ha ingresado un numero valido. \n Ingrese nuevamente un numero natural diferente de 0","red") )
        continuar()
    except ValueError:
      print(colored("el cararcter ingresado no es un numero ingrese el valor nuevamente \n","red"))
      nValido=False
  return n 

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      lista=creaLista(depuraN())
      print(colored("Lista = ","green"),colored(tostring(lista)+"\n","cyan"))
      
      
      
      
    elif (opcion=="2"):   
      salida=True
      print(colored("Gracias por usar el programa","red") )
      finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta","red") )
      continuar()


 


main()