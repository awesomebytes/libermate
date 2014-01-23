function y = fd_deriv2(f,x,h)
%FD_DERIV2  Finite difference approximation to derivative.
%           FD_DERIV2(F,X,H) is a finite difference approximation
%           to the derivative of function F at X with difference
%           parameter H.  H defaults to SQRT(EPS).

if nargin < 3, h = sqrt(eps); end
y = (feval(f,x+h) - feval(f,x))/h;
