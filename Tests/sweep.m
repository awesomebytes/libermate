%SWEEP         Generates a volume-swept 3D object.

N = 10;                   % Number of increments - try increasing.

z  = linspace(-5,5,N)';
radius = sqrt(1+z.^2);    % Try changing SQRT to some other function.
theta = 2*pi*linspace(0,1,N);
X = radius*cos(theta);
Y = radius*sin(theta);
Z = z(:,ones(1,N));

surf(X,Y,Z)
axis equal
