from termcolor import colored
def menu():
  print(colored("Deseas consultar si una palabra es palindroma? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def esPalindromo():  
  palabra=input(colored("ingrese la palabra\n","yellow"))
  for i in range(0,int(len(palabra)/2)): #Es suficiente con analizar la mitad  
    if palabra[i]!=palabra[-i-1]:
     return False
  return True
        
def muestrapalindroma():
  if(esPalindromo()==True):
    print(colored("la palabra es palindroma\n","green"))
  else:
    print(colored("la palabra No es palindroma\n","green"))


def finalizar():
  print(colored("Programa finalizado","red") )

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      muestrapalindroma()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
        finalizar()
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()