#Metodo de la Distancia con Errores
def distancia(vel,tiempo,errorV,errorT):
  distancia = vel * tiempo
  error_abs = (vel * errorV) + (tiempo * errorT)
  error_rel = ((errorV / vel) + (errorT / tiempo)) * 100
  print("La distancia recorrida es de: " + str(distancia))
  print("Con un error absoluto de: " + str(error_abs))
  print("Por lo cual la distancia tiene un rango de variacion: ")
  print("   " + str(distancia - error_abs) + " <= d <= " + str(distancia + error_abs))
  print("\nEl error relativo es de: " + str(error_rel) + "%")

distancia(5,4,0.1,0.1)
