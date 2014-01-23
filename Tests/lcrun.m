function lcrun
%LCRUN   Liquid crystal BVP.
%        Solves the liquid crystal BVP for four different lambda values.

lambda_vals = [2.4, 2.5, 3, 10];
lambda_vals = lambda_vals(end:-1:1); % Necessary order for continuation.

solinit = bvpinit(linspace(-1,1,20),@lcinit);
lambda = lambda_vals(1); sola = bvp4c(@lc,@lcbc,solinit);
lambda = lambda_vals(2); solb = bvp4c(@lc,@lcbc,sola);
lambda = lambda_vals(3); solc = bvp4c(@lc,@lcbc,solb);
lambda = lambda_vals(4); sold = bvp4c(@lc,@lcbc,solc);
plot(sola.x,sola.y(1,:),'-', 'LineWidth',4), hold on
plot(solb.x,solb.y(1,:),'--','LineWidth',2)
plot(solc.x,solc.y(1,:),'--','LineWidth',4)
plot(sold.x,sold.y(1,:),'--','LineWidth',6), hold off
legend([repmat('\lambda = ',4,1) num2str(lambda_vals')])
xlabel('x','FontSize',16)
ylabel('\theta','Rotation',0,'FontSize',16)
ylim([-0.1 1.5])

    function yprime = lc(x,y)
    %LC       ODE/BVP liquid crystal system.
    yprime = [y(2); -lambda*sin(y(1))*cos(y(1))];
    end

end

function res = lcbc(ya,yb)
%LCBC     ODE/BVP liquid crystal boundary conditions.
res = [ya(1); yb(1)];
end

function yinit = lcinit(x)
%LCINIT   ODE/BVP liquid crystal initial guess.
yinit = [sin(0.5*(x+1)*pi); 0.5*pi*cos(0.5*(x+1)*pi)];
end
