from termcolor import colored 
archivo = open('palabras500.csv', encoding="utf-8")
lineas=archivo.readlines()
archivo.close
#print(lineas)
#print(type(lineas))
#c=[1,2,3]
#print(type(c))
A=[palabra[0:-1] for palabra in lineas] #crea uja lista que contiene todos los datos de lista pero sin el "\n"

#print(A)

def busca_rima(rima): #devuelve una lista con las palabras de la lista A con terminacion en el parametro
  
  Pala_rima=[palabra for palabra in A if palabra[-len(rima):]==rima]
  return Pala_rima


def finalizar():
  print(colored("Programa finalizado","red") )


def menu():
  print(colored("Ejercicio Buscar Rima 2 \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. Ver la lista de palabras (A)\n","green"))
  print(colored('2. Buscar rimas con "a" en la lista A\n','green'))
  print(colored("3. Buscar rima personalizada en la lista A\n","green"))
  print(colored("4. salir\n","red"))
  respuesta= input("")
  return respuesta



def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      print(A)
      continuar()
    elif(opcion=="2"):
      pala_riman=str(busca_rima("a"))
      print(colored("las palabras que riman con a son: \n", "green"))
      print(colored(pala_riman, "cyan"))
      continuar()
      
    elif(opcion=="3"):  
      prueba_rima = input(colored("ingrese la terminacion que busca rimar: \n","yellow")) 
      pala_riman=str(busca_rima(prueba_rima))
      print(colored("las palabras que riman con "+prueba_rima+" son: \n", "green"))
      print(colored(pala_riman, "cyan"))
      continuar()
    elif(opcion=="4"):
      salida=True
      print(colored("Gracias por usar el programa","red") )
      finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta","red") )
      continuar()         

main()