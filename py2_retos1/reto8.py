from termcolor import colored
def menu():
  print(colored("Deseas contar los pares de 10 hasta 20? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def cuenta():
  for i in range (10,21,2):
    print(colored(i,"cyan"))

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      cuenta()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()