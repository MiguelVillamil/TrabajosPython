
from termcolor import colored 




def finalizar():
  print(colored("Programa finalizado","red") )

def ajedrez():
  casillas=[]
  fila=[]
  trigo=1 
  for i in range(1,8):
    
    fila=[]
    for j in range (1,8):
      fila.append(trigo) 
      trigo=trigo*2 
    casillas.append(fila)  
    
  return casillas

def trigo(casilla):
  tablero=casilla
  total=0
  
  for i in range(0,7):
    
    for j in range (0,7):
    
      total= total + tablero[i][j]
  return total
    

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
  print(colored("Ejercicio ajedrez\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. cuanto trigo hay en el tablero","green"))
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
        
        a=ajedrez()
        print(colored("en trigo en su tablero seria: ","yellow") )
        print(colored(str(a) + "\n","green") )
        print(colored("el trigo total es:\n ","yellow") )
        print(colored(str(trigo(a)) + "\n","green") )

        continuar()
      
    
    elif(opcion=="2"):   
        salida=True
        print(colored("Gracias por usar el programa\n","red") )
        finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        