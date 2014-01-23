function [x,y] = badfu(a,b,c)
%BADFUN   Function on which to illustrate MLINT.

if nargin < 3 | isempty(c), c = 1; end

x = sqrt(a^2+b^2)
