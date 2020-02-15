#Error Redondeo en 4 Cifras
errorRedondeo <- function (num, m, n){
  numero<- abs(num)
  
  while(num>1){
    num<-num/10
    n=n+1
  }
  E<-(num-trunc(num*10^4)/10^4)
  izq<-1*10^(n-m)
  der<-1*10^(n-m)
  cat("E se encuentra en el intervalo: ",izq,"<",E,"<",der)
}
errorRedondeo(536.78,4, 0)



