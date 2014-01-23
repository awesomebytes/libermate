function neural
%NEURAL     Neural network model with delays.

tspan = [0 40];
sol = dde23(@f,[0.2,0.5],@history,tspan);
subplot(2,2,1)
plot(sol.x,sol.y(1,:),'r-', sol.x,sol.y(2,:),'g--', 'LineWidth',2)
legend('y_1','y_2')
title('\tau_1 = 0.2, \tau_2 = 0.5','FontSize',12)
xlabel t, ylabel('y','Rotation',0), ylim([-0.2,0.2])

subplot(2,2,3)
plot(sol.y(1,:),sol.y(2,:),'r-')
xlabel y_1, ylabel('y_2','Rotation',0)
xlim([-0.2,0.2]), ylim([-0.1,0.1])

sol = dde23(@f,[0.325,0.525],@history,tspan);
subplot(2,2,2)
plot(sol.x,sol.y(1,:),'r-', sol.x,sol.y(2,:),'g--', 'LineWidth',2)
legend('y_1','y_2')
title('\tau_1 = 0.325, \tau_2 = 0.525','FontSize',12)
xlabel t,  ylabel('y','Rotation',0), ylim([-0.2,0.2])

subplot(2,2,4)
plot(sol.y(1,:),sol.y(2,:),'r-')
xlabel y_1, ylabel('y_2','Rotation',0)
xlim([-0.2,0.2]), ylim([-0.1,0.1])

function v = f(t,y,Z)
%F       Neural network differential equation.
ylag1 = Z(:,1);
ylag2 = Z(:,2);
v = [-y(1) + 2*tanh(ylag2(2))
     -y(2) - 1.5*tanh(ylag1(1))];

function v = history(t)
%HISTORY   Initial function for neural network model
v = 0.1*[sin(t/10);cos(t/10)];
