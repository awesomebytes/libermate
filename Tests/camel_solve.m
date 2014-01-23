%CAMEL_SOLVE  Find stationary points of the camel function.
%             This script requires the Symbolic Math Toolbox.

format short e
syms x y
f = 4*x^2 - 3*x^4 + x^6/3 + x*y - 4*y^2 + 4*y^4;

fx = diff(f,x), fy = diff(f,y)
disp('Original solutions:')
s = solve(fx,fy)

H = maple('hessian', f, '[x,y]')
n = length(s.x); j = 1; minx = []; maxx = []; saddlex = [];

for i = 1:n  % Loop over stationary points.
    fprintf('Point %2.0f:  ',i)
    xi = s.x(i); yi = s.y(i);
    pointi = double([xi yi]);
    gi = double([subs(fx,{x,y},{xi,yi}) subs(fy,{x,y},{xi,yi})]);
    % Filter out nonreal points and points where gradient not zero.
    if norm(gi) > eps
       fprintf('gradient is nonzero!\n')
    elseif ~isreal(pointi)
       fprintf('is nonreal!\n')
    else
       fprintf('(%10.2e,%10.2e)  ', pointi)
       Hi = double(subs(H,{x,y},{xi,yi}));
       eig_Hi = eig(Hi);
       if all(eig_Hi > 0)
          minx = [minx; pointi]; fprintf('minimum\n')
       elseif all(eig_Hi < 0)
          maxx = [maxx; pointi]; fprintf('maximum\n')
       elseif prod(eig_Hi) < 0
          saddlex = [saddlex; pointi]; fprintf('saddle point\n')
       else
          fprintf('nature of stationary point unclear\n')
       end
    end
end
minx, maxx, saddlex

plot(minx(:,1),minx(:,2),'*',...
     maxx(:,1),maxx(:,2),'o',...
     saddlex(:,1),saddlex(:,2),'x','MarkerSize',8)
hold on
a = axis;
[x,y] = meshgrid(linspace(a(1),a(2),200),linspace(a(3),a(4),200));
z = subs(f);  % Replaces symbolic x and y with numeric values from workspace.
contour(x,y,z,30)
xlim([-2.5 2.5]) % Fine tuning.
legend('Min', 'Max', 'Saddle')
g = findall(gca,'type','axes'); set(g,'Fontsize',14)
hold off
