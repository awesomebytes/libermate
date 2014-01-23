function rossler_ex1
%ROSSLER_EX1       Run Rossler example.

tspan = [0 100]; yzero = [1;1;1];
options = odeset('AbsTol',1e-7,'RelTol',1e-4);

a = 0.2; b = 0.2; c = 2.5;
[t,y] = ode45(@rossler,tspan,yzero,options);
subplot(221), plot3(y(:,1),y(:,2),y(:,3)), mytitle, zlabel('y_3(t)'), grid
subplot(223), plot(y(:,1),y(:,2)), mytitle

c = 5;
[t,y] = ode45(@rossler,tspan,yzero,options);
subplot(222), plot3(y(:,1),y(:,2),y(:,3)), mytitle, zlabel('y_3(t)'), grid
subplot(224), plot(y(:,1),y(:,2)), mytitle

     % ------------------------ Nested functions ----------------------
     function yprime = rossler(t,y)
     %ROSSLER    Rossler system, parameterized.
     yprime = [-y(2)-y(3); y(1)+a*y(2); b+y(3)*(y(1)-c)];
     end

     function mytitle
     title(sprintf('c = %2.1f',c),'FontSize',14)
     xlabel('y_1(t)'), ylabel('y_2(t)')
     end

