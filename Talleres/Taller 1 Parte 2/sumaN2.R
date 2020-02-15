##Funcion de Suma (n2)2

#Datos Entrada
n=2;
first=1

for(i in 0:23){
  suma=0
  for(i in first:n^2){
    iCuadrado=i^2;
    suma= suma + iCuadrado;
  }
  tabla <- data.frame(n, suma)
  n=n+1;
  print(tabla)
}

