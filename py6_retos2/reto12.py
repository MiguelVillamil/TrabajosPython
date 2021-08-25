from termcolor import colored 




def finalizar():
  print(colored("Programa finalizado","red") )

def imprimeFrase(f):
  
  L=list(f)
  largo=len(L)
  for i in range (largo):
    print(colored(str(i) +". "+ str(L[i])+"\n","green"))
  return f
    


def menu():
  print(colored("Ejercicio separar frase\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. frase personalizadas","green"))
  print(colored("2. frase ejemplo","green"))
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
      print(colored("ingresa tu frase \n","yellow"))
      frase=imprimeFrase(str(input("")))
      print(colored("la frase es:\n","yellow"))
      print(colored(str(frase)+"\n","green"))
      continuar()
      

    elif(opcion=="2"):   
      print(colored("ingresa tu frase \n","yellow"))
      frase=imprimeFrase("2001: A Space Odyssey")
      print(colored(str(frase)+"\n","green"))
      continuar()

    elif(opcion=="3"):   
      salida=True
      print(colored("Gracias por usar el programa\n","red") )
      
      finalizar()

    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        