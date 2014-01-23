function  B = land(A)
%LAND     Fractal landscape.
%         B = LAND(A) generates a random fractal landscape
%         represented by B, where A is a square matrix of
%         dimension N = 2^n + 1 whose four corner elements
%         are used as input parameters.

N = size(A,1);
d = (N+1)/2;
level = log2(N-1);
scalef = 0.05*(2^(0.9*level));

B = A;

B(d,d) = mean([A(1,1),A(1,N),A(N,1),A(N,N)]) + scalef*randn;
B(1,d) = mean([A(1,1),A(1,N)]) + scalef*randn;
B(d,1) = mean([A(1,1),A(N,1)]) + scalef*randn;
B(d,N) = mean([A(1,N),A(N,N)]) + scalef*randn;
B(N,d) = mean([A(N,1),A(N,N)]) + scalef*randn;

if N > 3
   B(1:d,1:d) = land(B(1:d,1:d));
   B(1:d,d:N) = land(B(1:d,d:N));
   B(d:N,1:d) = land(B(d:N,1:d));
   B(d:N,d:N) = land(B(d:N,d:N));
end
