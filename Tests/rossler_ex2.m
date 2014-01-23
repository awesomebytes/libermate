function rossler_ex2
%ROSSLER_EX2     Attractor reconstruction for Rossler system.

tspan = [0 100]; yzero = [1;1;1];
options = odeset('AbsTol',1e-7,'RelTol',1e-4);

a = 0.2; b = 0.2; c = 2.5;
sol = ode45(@rossler,tspan,yzero,options);
tau = 1.5;
t = linspace(tau,100,1000);
y = deval(sol,t,1);
ylag = deval(sol,t-tau,1);
plot(y,ylag), title('\tau = 1.5','FontSize',14)
xlabel('y_1(t)','FontSize',14)
ylabel('y_1(t-\tau)','FontSize',14,'Rotation',0,...
       'HorizontalAlignment','right')

     function yprime = rossler(t,y)
     %ROSSLER    Rossler system, parametrized.
     yprime = [-y(2)-y(3); y(1)+a*y(2); b+y(3)*(y(1)-c)];
     end

end
