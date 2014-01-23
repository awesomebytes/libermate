function C = companb(varargin)
%COMPANB     Block companion matrix.
%            C = COMPANB(A_1,A_2,...,A_m) is the block companion matrix
%            corresponding to the n-by-n matrices A_1,A_2,...,A_m.

m = nargin;
n = length(varargin{1});

C = diag(ones(n*(m-1),1),-n);
for j = 1:m
    Aj = varargin{j};
    C(1:n,(j-1)*n+1:j*n) = -Aj;
end
