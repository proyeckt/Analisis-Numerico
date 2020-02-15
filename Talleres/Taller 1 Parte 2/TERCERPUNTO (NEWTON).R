#Metodo Newton (Convergencia)
expresion <- expression(exp(x)-x-1)
derivada <- D(expresion,"x")

x<-0
aproximacion <- 0.00005

while(x!=aproximacion)
{
  x<-aproximacion
  reemplazarAproximacion <- eval(expresion)
  reemplazarDerivada<- eval(derivada)
  
  aproximacion<- x-(reemplazarAproximacion/reemplazarDerivada)
  print(x)
  
}
