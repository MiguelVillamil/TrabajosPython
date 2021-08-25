import random
from termcolor import colored 




def finalizar():
  print(colored("Programa finalizado","red") )

def series(i,f,s):
  l=[]
  total=0 
  for i in range(i,f,s):
    total+=i 
    l.append(i)
  l.append(total)
  return l  

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


def menu():
  print(colored("Ejercicio series\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. series con intervalos ","green"))
  print(colored("2. salir\n","red"))
  respuesta= input("")
  return respuesta



def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
        print(colored("Ingrese numero Minimo: ","yellow") )
        x=depuraNum()
        print(colored("Ingrese Numero Maximo: ","yellow") )
        y=depuraNum()+1
        print(colored("Ingrese el intervalo: ","yellow") )
        z=depuraNum()
        a=series(x,y,z)
        print(colored("su serie es: ","yellow") )
        print(colored(str(a[0:-1]) + "\n","green") )
        print(colored("la suma de su numero serie:\n ","yellow") )
        print(colored(str(a[-1]) + "\n","green") )

        continuar()
      
    
    elif(opcion=="2"):   
        salida=True
        print(colored("Gracias por usar el programa\n","red") )
        finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        