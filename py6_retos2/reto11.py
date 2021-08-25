
from termcolor import colored 




def finalizar():
  print(colored("Programa finalizado","red") )

def unirListas(a,b):
  l1=a.copy()
  l2=b.copy()
  l1.extend(l2)  
  return l1

def crearlista(a,b):
  l=list(range(a,b+1))

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
  print(colored("Ejercicio unir listas\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. listas personalizadas","green"))
  print(colored("2. listas ejemplo","green"))
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
      print(colored("ingrese el valor minimo de la lista 1: ","yellow") )  
      a=depuraNum()
      print(colored("ingrese el valor maximo de la lista 1: ","yellow") )  
      b=depuraNum()
      l1=crearlista(a,b)
      print(colored("ingrese el valor minimo de la lista 2: ","yellow") )  
      c=depuraNum()
      print(colored("ingrese el valor maximo de la lista 2: ","yellow") )  
      d=depuraNum()
      l2=crearlista(c,d)
      l3=unirListas(l1,l2)
      print(colored("la lista 1 seria: ","yellow") )
      print(colored(str(l1) + "\n","green") )
      print(colored("la lista 2 seria: ","yellow") )
      print(colored(str(l2) + "\n","green") )
      print(colored("la lista total es:\n ","yellow") )
      print(colored(str(l3) + "\n","green") )

      continuar()
      
    elif(opcion=="2"):   
      
      l1=crearlista(1,10)
      l2=crearlista(11,20)
      l3 = unirListas(l1,l2)
      print(colored("la lista 1 seria: ","yellow") )
      print(colored(str(l1) + "\n","green") )
      print(colored("la lista 2 seria: ","yellow") )
      print(colored(str(l2) + "\n","green") )
      print(colored("la lista total es:\n ","yellow") )
      print(colored(str(l3) + "\n","green") )
      continuar()
    elif(opcion=="3"):   
      salida=True
      print(colored("Gracias por usar el programa\n","red") )
      
      finalizar()

    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        