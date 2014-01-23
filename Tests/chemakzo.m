function chemakzo
%CHEMAKZO     Chemical Akzo Nobel problem.
%             Index 1 DAE describing a chemical process.

M = eye(6); M(6,6) = 0;
options = odeset('Mass',M,'MassSingular','yes');

tspan = [0 180];
Ks = 115.83;
y0 = [0.444; 0.00123; 0; 0.007; 0; Ks*0.444*0.007];
[t,y] = ode15s(@chem_rhs,tspan,y0,options);

for i = 1:6
   subplot(2,3,i)
   plot(t,y(:,i),'LineWidth',2), grid on
   title(['y_',int2str(i)]), xlabel('t'), xlim([0 180])
end

% Reference solution at t = 180
yref = [0.1150794920661702;    0.1203831471567715e-2
        0.1611562887407974;    0.3656156421249283e-3
        0.1708010885264404e-1; 0.4873531310307455e-2]';

yerr = norm(y(end,:) - yref)

    % ------------------- Nested function -------------------
    function rhs = chem_rhs(t,y)
    %CHEM_RHS      Right-hand side of DAE

    if y(2) < 0, error('Negative y(2) in DAE function.'), end

    k1 = 18.7; k2 = 0.58; k3 = 0.09; k4 = 0.42;
    K = 34.4; klA = 3.3; pCO2 = 0.9; H = 737;

    r1 = k1*(y(1)^4)*sqrt(y(2));
    r2 = k2*y(3)*y(4);
    r3 = k2*y(1)*y(5)/K;
    r4 = k3*y(1)*(y(4)^2);
    r5 = k4*(y(6)^2)*sqrt(y(2));
    Fin = klA*(pCO2/H - y(2));

    rhs = [-2*r1 + r2 - r3 - r4;
           -0.5*r1 - r4 - 0.5*r5 + Fin;
           r1 - r2 + r3;
           -r2 + r3 - 2*r4;
           r2 - r3 + r5;
           Ks*y(1)*y(4)-y(6)];
    end

end
