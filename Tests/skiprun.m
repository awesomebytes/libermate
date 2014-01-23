function sol = skiprun
%SKIPRUN  Skipping rope BVP/eigenvalue example.

solinit = bvpinit(linspace(0,1,10),@skipinit,5);
sol = bvp4c(@skip,@skipbc,solinit);
plot(sol.x,sol.y(1,:),'-', sol.x,sol.yp(1,:),'--', 'LineWidth',4)
xlabel('x','FontSize',12)
legend('y_1','y_2')

% ------------------------ Subfunctions ------------------------
function yprime = skip(x,y,mu)
%SKIP     ODE/BVP skipping rope example.
%         YPRIME = SKIP(X,Y,MU) evaluates derivative.
yprime = [y(2); -mu*y(1)];

function res = skipbc(ya,yb,mu)
%SKIPBC   ODE/BVP skipping rope boundary conditions.
%         RES = SKIPBC(YA,YB,MU) evaluates residual.
res = [ya(1); ya(2)-1; yb(1)+yb(2)];

function yinit = skipinit(x)
%SKIPINIT ODE/BVP skipping rope initial guess.
%         YINIT = SKIPINIT(X) evaluates initial guess at X.
yinit = [sin(x); cos(x)];
