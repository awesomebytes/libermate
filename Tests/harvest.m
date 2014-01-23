function harvest
%HARVEST   Predator-prey model with delay and harvesting.

tau = 9;
ic = [35;10];
tspan = [0 250];

h = 10;
sol = dde23(@f,tau,ic,tspan);
subplot(2,1,1)
plot(sol.x,sol.y(1,:),'r-', sol.x,sol.y(2,:),'g--', 'LineWidth',2)
legend('y_1','y_2','Location','East')
title('h = 10','FontSize',12), xlabel t, ylabel('y','Rotation',0)

h = 15;
sol = dde23(@f,tau,ic,tspan);
subplot(2,1,2)
plot(sol.x,sol.y(1,:),'r-', sol.x,sol.y(2,:),'g--', 'LineWidth',2)
legend('y_1','y_2','Location','East')
title('h = 15','FontSize',12), xlabel t, ylabel('y','Rotation',0)

    function v = f(t,y,Z)
    %F           Harvest differential equation.
    v = [y(1)*(2*(1-y(1)/50) - y(2)/(y(1)+40)) - h
         y(2)*(-3 + 6*Z(1)/(Z(1)+40))];
    end

end
