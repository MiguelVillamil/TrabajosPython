from termcolor import colored 

def media(x,y):
  return (x+y)/2


def finalizar():
  print(colored("Programa finalizado","red") )

def depuraNum():
  nValido=False
  while (nValido==False):
    try:
      n= float (input(colored("ingrese el numero deseado: \n","yellow")))
      nValido=True
    except ValueError:
      print(colored("el cararcter ingresado no es un numero ingrese el valor nuevamente \n","red"))
      nValido=False
  return n 
    


def menu():
  print(colored("Ejercicio media\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. hallar la media entre 2 numeros","green"))
  
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
      print(colored("ingresa tus 2 numeros \n","yellow"))
      
      
      print(colored("la media es :"+str(media(depuraNum(),depuraNum())) ,"green"))
      continuar()

    elif(opcion=="2"):   
      salida=True
      print(colored("Gracias por usar el programa\n","red") )
      
      finalizar()

    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        