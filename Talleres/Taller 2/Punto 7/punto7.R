library(Matrix)
library(PolynomF)
f<- function(x){exp(x)}
x<-c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
plot(x,f(x),pch=19, cex=1, col = "pink", asp=1)
curve(f(x),add=T,from=0, to=21)
print(f(x))
#Funccion lagrange
lagrange = function(x,y,a){
  n = length(x)
  if(a < min(x) || max(x) < a) stop("No está interpolando")
  X  = matrix(rep(x, times=n), n, n, byrow=T)
  mN = a - X;    diag(mN) = 1
  mD = X - t(X); diag(mD) = 1
  Lnk = apply(mN, 1, prod)/apply(mD, 2, prod)
  sum(y*Lnk)
}
x<-c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
#print(f(x))
y<-c(1.000000, 1.105171, 1.221403, 1.349859, 1.491825, 1.648721, 1.822119, 2.013753, 2.225541, 2.459603, 2.718282)
datox=x[1:11]
datoy=y[1:11]
polyAjuste = poly.calc(datox,datoy)
polyAjuste
#0.997597 + 1.024583*x + 0.417*x^2 + 0.2761667*x^3, polinomio interpolante con método de Lagrange
plot(datox,datoy, pch=19, cex=1, col = "red", asp=1) 
curve(polyAjuste,add=T,from=0, to=21)
print("Lagrange para 1 (valor más alto del vector escojido)")
print(lagrange(x,y,1)) 
#Error
tamx<-11
derivadaf<-function(x){exp(x)}
factorial<-tamx+1
cotaError<-function(x1){
  res=derivadaf(x1)/factorial
  multi=1
  for(i in tamx)
    multi=multi*(x1-x[i])
  final=multi*res
  print(final) # Paso necesario en nodos igualmente espaciados para error máximo de 10^-6, utilizando la ecuación demostrada en el punto 5
}
