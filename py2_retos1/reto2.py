from termcolor import colored

salida=False
while(salida==False):
  print(colored("El mundo te esta saludando, quieres saludarlo de vuelta? \n","cyan"))
  print(colored("1. si ","green"),colored(" 2. no\n", "red"))
  respuesta = input("")
  if (respuesta == "1"):
    print(colored("si \n","red"))
    print (colored("hola mundo c:","red"))
  else:
    if (respuesta=="2"):
        print(colored("no \n","red"))
        print (colored("no? que mala persona! >:c","cyan"))
        salida=True
    else:
          print (colored("no he entendido .-. esa respuesta no esta disponible","cyan"))


