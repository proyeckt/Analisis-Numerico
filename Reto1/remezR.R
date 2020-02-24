f = function(pX){
  sin(x)
}
remez = function (f,n){
  xk = cos(pi*(n+1:-1:0)/(n+1));
  normf = norm(f);
  delta = 1; 
  while (delta/normf > 1e-11){
    A = zeros(n+2,n+1);
    for (j in 1:n+1) {
      t = chebfun((-1)^(j-1:-1:0)); 
      A(1:j) = t(xk);
    }
    A = A (-1).^(0:n+1);
    c = f(xk);
    h = c(end); 
    p = chebfun(chebpolyval(c)); 
    e = f - p; 
    xk= exchange(xk,e,h); 
    delta = norme - abs(h);
  }
}
