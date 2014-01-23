%BIF1 Bifurcation diagram for modified Euler/logistic map.
%     Computes a numerical bifurcation diagram for a map of the form
%     y_k = F(y_{k-1}) arising from the modified Euler method
%     applied to a logistic ODE.
%
%     Slower version using multiple for loops.

for h = 1:0.005:4
    for iv = 0.2:0.5:2.7
       y(1) = iv;
       for k = 2:520
          y(k) = y(k-1) + h*(y(k-1)+0.5*h*y(k-1)*(1-y(k-1)))*...
                 (1-y(k-1)-0.5*h*y(k-1)*(1-y(k-1)));
       end
       plot(h*ones(20,1),y(501:520),'.'), hold on
    end
end

title('Modified Euler/logistic map','FontSize',14)
xlabel('h'), ylabel('last 20 y')
grid on, hold off
