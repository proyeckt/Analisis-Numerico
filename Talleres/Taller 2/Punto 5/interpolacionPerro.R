#Interpolacion Perro
library(polynom)
library(PolynomF)

yy=c(3,3.7,3.9,4.5,5.7,6.69,7.12,6.7,4.45,7,6.1,5.6,5.87,5.15,4.1,4.3,4.1,3,2,2.3,2,3.2,3,3)                                    
xx=c(1,2,5,6,7.5,8.1,10,13,17.6,20,23.5,24.5,25,26.5,27.5,28,29,30,25,20,10,9.7,7,1)
plot(xx,yy, pch=19, cex=0.9, col = "White", asp=1,xlab="XX", ylab="YY", main="Perro Interpolado ")
n=24
pint<-function(xx,yy){
  t = 1:length(xx)
  sx = spline(t,xx)
  sy = spline(t,yy)
  lines(sx[[2]],sy[[2]],type='l', col="BLUE")
}
pint(xx,yy)

