from termcolor import colored
def menu():
  print(colored("Deseas visualizar las tablas de multiplicar? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def tabla():
  tabla=int(input(colored("Ingrese hasta cual tabla desea visualizar\n","yellow")))
  espacio=len(str(tabla*tabla))+1 #encontramos cuantas casillas ocupa el numero maximo y le agregamos una casilla extra
  for i in range(1,tabla+1):
    casilla=''
    for j in range(1,tabla+1):
      libres=espacio-len(str(i*j))#encontramos cunatas casillas ocupa el numero y se lo restamos al espacio total
      casilla=casilla+((' '*libres)+str(i*j)) #rellenamos la casilla
    print(casilla) 

  

def finalizar():
  print(colored("Programa finalizado","red") )

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      tabla()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
        finalizar()
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()