%BIF2 Bifurcation diagram for modified Euler/logistic map.
%     Computes a numerical bifurcation diagram for a map of the form
%     y_k = F(y_{k-1}) arising from the modified Euler method
%     applied to a logistic ODE.
%
%     Fast, vectorized version.

h = (1:0.005:4)';
iv = 0.2:0.5:2.7;
hvals = repmat(h,length(iv),1);
Ydata = zeros((length(hvals)),20);
y = kron(iv',ones(size(h)));

for k=2:500
   y = y + hvals.*(y+0.5*hvals.*y.*(1-y)).*(1-y-0.5*hvals.*y.*(1-y));
end
for k=1:20
   y = y + hvals.*(y+0.5*hvals.*y.*(1-y)).*(1-y-0.5*hvals.*y.*(1-y));
   Ydata(:,k) = y;
end

plot(hvals,Ydata,'.')
title('Modified Euler/Logistic Map','FontSize',14)
xlabel('h'), ylabel('last 20 y'), grid on
