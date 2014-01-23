function varargout = moments(x)
%MOMENTS  Moments of a vector.
%         [m1,m2,...,mk] = MOMENTS(X) returns the first, second, ...,
%         k'th moments of the vector X, where the j'th moment
%         is SUM(X.^j)/LENGTH(X).

for j = 1:nargout, varargout(j) = {sum(x.^j)/length(x)}; end
