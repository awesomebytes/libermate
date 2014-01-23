%OPS   Profile this file to check costs of various elementary ops and funs.

rand('state',1), randn('state',1)
n = 500;
a = 100*rand(n);
b = randn(n);

for i = 1:100
    a+b;
    a-b;
    a.*b;
    a./b;
    sqrt(a);
    exp(a);
    sin(a);
    tan(a);
end
