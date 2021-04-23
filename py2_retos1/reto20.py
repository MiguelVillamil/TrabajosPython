from termcolor import colored
def menu():
  print(colored("Deseas buscar un año bisiesto? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def año_bi():
  ano=int(input(colored("ingrese el año a buscar\n","yellow")))
  if(ano%4==0 and (ano%100!=0 or ano%400==0)):
    print(colored("el año es bisiesto\n","green") )
  else:
   print(colored("el año","green"),colored( "No","red"), colored("es bisiesto \n","green") )

def finalizar():
  print(colored("Programa finalizado","red") )

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      año_bi()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
        finalizar()
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()