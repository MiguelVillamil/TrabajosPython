#print ("hola mundo")
archivo = open('palabras500.csv', encoding="utf-8")
lineas=archivo.readlines()
archivo.close

#print(len(lineas))
#print(lineas[0])

def depura_palabra(una_palabra): #esta funcion depura el salto de linea
  pala = una_palabra;
  if "\n" in pala:
    # \n ocupa un solo espacio del str
    pala= pala[0:-1]
    return pala 
  else: 
    return pala  

#print(depura_palabra("hola\n"))

def encuentra_rima (una_palabra, una_rima):#esta funcion verifica si el argumento2 esta al final del argumento1 no admite saltos de linea
  p=depura_palabra(una_palabra)
 
  if una_rima in p[-len(una_rima):]:
    #print(p[-4:])
    return True
  else:
    return False  

#print(encuentra_rima("caminando","ando"))
#print(encuentra_rima("caminano","ando"))

def rima (una_rima):#esta funcion busca los str de  lineas que terminen en el parametro ingresado
  for palabra in lineas:
    if encuentra_rima(palabra,una_rima) == True:
      print('la palabra "'+ palabra +'" tiene la rima "'+ una_rima +'"' )

rima("an")

def ingrese_rima(): #esta funcion permite ingresar una rima
  prueba_rima = input("ingrese la terminacion que busca rimar: \n") 
  rima(prueba_rima) 

ingrese_rima()