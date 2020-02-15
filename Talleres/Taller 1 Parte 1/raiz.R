#Metodo Raiz (caso: raiz de 7)
raiz <- function(n, E, x)
{
  y <- 0.5*( x + n / x);
  k<-abs(x-y)
 
  while(k > E){
    x <- y
    y <- (1/2)*(x+(n/x))
    k <- abs(x-y)
  }
  return(cat("El resultado es: ", y, " con error de ", E))
}
raiz(7,0.00000001, 100)

