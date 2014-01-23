function [x,iter] = sqrtn(a,tol)
%SQRTN    Square root of a scalar by Newton's method.
%         X = SQRTN(A,TOL) computes the square root of the scalar
%         A by Newton's method (also known as Heron's method).
%         A is assumed to be >= 0.
%         TOL is a convergence tolerance (default EPS).
%         [X,ITER] = SQRTN(A,TOL) returns also the number of
%         iterations ITER for convergence.

if nargin < 2, tol = eps; end

x = a;
iter = 0;
xdiff = inf;
fprintf(' k             x_k            rel. change\n')

while xdiff > tol
    iter = iter + 1;
    xold = x;
    x = (x + a/x)/2;
    xdiff = abs(x-xold)/abs(x);
    fprintf('%2.0f:  %20.16e  %9.2e\n', iter, x, xdiff)
    if iter > 50
       error('Not converged after 50 iterations.')
    end
end
