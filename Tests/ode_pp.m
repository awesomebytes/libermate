function T = ode_pp
%ODE_PP    Performance profile of three ODE solvers.

solvers = {@ode23, @ode45, @ode113};  nsolvers = length(solvers);
nproblems = 6;
nruns = 5;  % Number of times to run solver to get more reliable timing.

for j = 1:nsolvers
    code = solvers{j}
    for i = 1:nproblems

        options = [];
        switch i
           case 1
               fun = @fox1; tspan = [0 10]; yzero = [3;0];
           case 2
               fun = @rossler; tspan = [0 100]; yzero = [1;1;1];
               options = odeset('AbsTol',1e-7,'RelTol',1e-4);
           case 3
               fun = @fvdpol; tspan = [0 20]; yzero = [2;1]; mu = 10;
           case 4
               fun = @fvdpol; tspan = [0 20]; yzero = [2;1]; mu = 1000;
           case 5
               fun = @drug_transport; tspan = [0 6]; yzero = [0;0];
           case 6
               fun = @knee; tspan = [0 2]; yzero = 1;
        end

        t0 = clock;
        for k = 1:nruns
            [t,y] = code(fun,tspan,yzero,options);
        end
        T(i,j) = etime(clock,t0)/nruns;

    end
end

perfprof(T);
ylim([0 1.05]), grid
yvals = 0:1/nproblems:1;
set(gca,'YTick',yvals)
set(gca,'YTickLabel',['   0 ';num2str(yvals(2:end-1)','%4.2f ');'   1 '])
f = findall(gcf,'type','line');       % Handles of the three lines.
legend('ode23','ode45','ode113','Location','SE')
set(f,{'Marker'},{'*','s','o'}')      % Vectorized set.
set(f,'MarkerSize',10)
set(f,'MarkerFaceColor','auto') % Make marker interiors non-transparent.
set(f,{'LineStyle'},{'-',':','--'}')  % Vectorized set.
set(f,'LineWidth',2)
set(gca,'FontSize',14)

      function yprime = fvdpol(x,y)
      %FVDPOL   Van der Pol equation written as first order system.
      %         Parameter MU.
      yprime = [y(2); mu*y(2)*(1-y(1)^2)-y(1)];
      end

end

function yprime = rossler(t,y)
%ROSSLER    Rossler system, parameterized.
a = 0.2; b = 0.2; c = 2.5;
yprime = [-y(2)-y(3); y(1)+a*y(2); b+y(3)*(y(1)-c)];
end

function yprime = drug_transport(t,y)
%DRUG_TRANSPORT  Two-compartment pharmacokinetics example.
%                Reference: Shampine (1994, p. 105).
yprime = [-5.6*y(1) + 48*pulse(t,1/48,0.5); 5.6*y(1) - 0.7*y(2)];

     function pls = pulse(t,w,p)
     %PULSE   Pulse of height 1, width W, period P.
     pls = (rem(t,p) <= w);
     end

end

function yprime = knee(t,y)
%KNEE       Knee problem.
%           Reference: Shampine (1994, p. 115).
epsilon = 1e-4;
yprime = (1/epsilon)*((1-t)*y - y^2);
end
