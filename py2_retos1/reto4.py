from termcolor import colored

def menu():
  print(colored("Deseas comparar  2 numeros? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def compara():
  num1= float(input (colored("ingresa el primer numero \n","green")))
  num2= float(input (colored("ingresa el segundo numero \n","green")))
  if(num1==num2):
    print(num1, colored(" es igual a ","green"),num2,"\n")
  else:
    if(num1>num2):
      print(num1, colored(" es mayor a ","green"),num2,"\n")
    else:
      if(num1<num2):
        print(num1, colored(" es menor a ","green"),num2,"\n")
      else:
        print(colored(" no ha ingresado un par de numeros reales \n","green"))

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      compara()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()
