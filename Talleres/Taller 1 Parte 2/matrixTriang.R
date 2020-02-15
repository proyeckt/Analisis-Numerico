##Funcion de Suma Matrix Triangular

#Datos Entrada
n=5;
minN=1;
maxN=100;
for(i in 0:20){
  matriz <- matrix(minN:maxN,n,n)
  #matriz
  matrizCopy <- matriz
  
  #Calculo Matrices Triangulares
  matriz[lower.tri(matriz,diag=TRUE)] <- 0
  matrizUPT <- matriz
  #matrizUPT
  matrizCopy[upper.tri(matrizCopy,diag=TRUE)] <- 0
  matrizDWT <- matrizCopy
  #matrizDWT
  
  #Sumas Matrices Triangulares
  sumUPT=sum(matrizUPT)
  #cat("\r n=",n,"Sumatoria Matriz Triangular Superior:",sumUPT)
  sumDWT=sum(matrizDWT)
  #cat("\r n=",n,"Sumatoria Matriz Triangular Inferior:",sumDWT)
  # crear dataframe de vectores
  tabla <- data.frame(n, sumUPT, sumDWT)
  n=n+1;
  print(tabla)
}

########################################
#Orden de Convergencia
#a=0.5;b=1.1;n=12;                           % Datos
#x=biseccion5(f,a,b,n);                      % Aplicamos la función
#p=1;                                        % Ahora x es un vector
#lambda=abs((x(2:end)-1)./(x(1:end-1)-1).^p) % Calculamos la expresión (1)
#figure;plot(lambda,'*-')
#xlabel('Iteración'),ylabel('lambda')        % Vemos que tiende a una constante

