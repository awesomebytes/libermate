%LRUN     ODE solving example: Lorenz.

tspan = [0 50];                       % Solve for 0 <= t <= 50.
yzero = [0;1;0];                      % Initial conditions.
[t,y] = ode45(@lorenzde,tspan,yzero);
plot(y(:,1),y(:,3))                   % (y_1,y_3) phase plane.
xlabel('y_1','FontSize',14)
ylabel('y_3 ','FontSize',14,'Rotation',0,'HorizontalAlignment','right')
title('Lorenz equations','FontSize',16)
