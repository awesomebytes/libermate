function rosy(a, b)
%ROSY   "Rose" figures.
%        ROSY(A, B) plots the curve
%           X = R*COS(A*theta), Y = R*SIN(A*theta), where
%           R = SIN(A*B*theta) and 0 <= theta <= 2*PI (360 values).
%        Suggestions: ROSY(97, 5); ROSY(43, 4); ROSY(79, n9), n a digit.

%        P. M. Maurer, A rose is a rose..., Amer. Math. Monthly, 94 (1987),
%        pp. 631-645.

if nargin < 2, b = 1; end
if nargin < 1, a = 1; end

c = 0; d = 1; p = a*b;
[x, y] = spiro(a, a, c, d, p, .5);

plot(x,y)
axis square, axis off

% Subfunction.
function [x, y] = spiro(a, b, c, d, p, k)
h = k*2*pi/180;
t = (0:h:2*pi)';
r = c + d*sin(t*p);
x = r.*cos(a*t);
y = r.*sin(b*t);
