function [f,fprime] = flogist(x,a)
%FLOGIST   Logistic function and its derivative.
%          [F,FPRIME] = FLOGIST(X,A) evaluates the logistic
%          function F(X) = X.*(1-A*X) and its derivative FPRIME
%          at the matrix argument X, where A is a scalar parameter.

f = x.*(1-a*x);
fprime = 1-2*a*x;
