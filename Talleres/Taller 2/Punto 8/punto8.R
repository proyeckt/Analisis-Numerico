require(pracma)

library(PolynomF)

# Punto A
temp=c(100,200,300,400,500,600) #Tam 6
B=c(-160,-35,-4.2,9,16.9,21.3)  #Tam 5

# Se interpolan los puntos posteriores al punto requerido obteniendo un  polinomio de grado 3.
polyAjuste=poly.calc(temp[3:6],B[3:6])
print(polyAjuste)

# Punto B
Coeficiente450k=polyAjuste(450) #Se evalua el coeficiente viral a 450K
Coeficiente450k

xi=seq(0,min(temp)+max(temp),0.1)
yi=polyAjuste(xi)

#Grafica del polinomio
plot(temp[3:6],B[3:6],cex=1,pch=19,col="black")
lines(xi,yi,col="blue",cex=2)

#Valor del coeficiente viral 450k con interpolacion de lagrange
barylag (temp,B,c(450))