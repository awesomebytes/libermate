function rossler_ex0
%ROSSLER_EX0  Run Rossler example.
% This is the recommended approach for MATLAB 6.5 and earlier.
% ROSSLER_EX0 runs in MATLAB 7, but ROSSLER_EX1 illustrates the style of
% coding now recommended for MATLAB 7.

tspan = [0 100]; yzero = [1;1;1];
options = odeset('AbsTol',1e-7,'RelTol',1e-4);

a = 0.2; b = 0.2; c = 2.5;
[t,y] = ode45(@rossler,tspan,yzero,options,a,b,c);
subplot(221), plot3(y(:,1),y(:,2),y(:,3)), mytitle(c), zlabel y_3(t), grid
subplot(223), plot(y(:,1),y(:,2)), mytitle(c)

c = 5;
[t,y] = ode45(@rossler,tspan,yzero,options,a,b,c);
subplot(222), plot3(y(:,1),y(:,2),y(:,3)), mytitle(c), zlabel y_3(t), grid
subplot(224), plot(y(:,1),y(:,2)), mytitle(c)

function yprime = rossler(t,y,a,b,c)
%ROSSLER    Rossler system, parameterized.
yprime = [-y(2)-y(3); y(1)+a*y(2); b+y(3)*(y(1)-c)];

function mytitle(c)
title(sprintf('c = %2.1f',c),'FontSize',14)
xlabel y_1(t), ylabel y_2(t)
