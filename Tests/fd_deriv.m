function y = fd_deriv(f,x,h)
%FD_DERIV   Finite difference approximation to derivative.
%           FD_DERIV(F,X,H) is a finite difference approximation
%           to the derivative of function F at X with difference
%           parameter H.  H defaults to SQRT(EPS).

if nargin < 3, h = sqrt(eps); end
y = (f(x+h) - f(x))/h;
