function yprime = fox1(t,y)
%FOX1   Fox-rabbit pursuit simulation.
%       YPRIME = FOX1(T,Y).

k = 0.75;
r = sqrt(1+t)*[cos(t); sin(t)];
r_p =(0.5/sqrt(1+t))*[cos(t)-2*(1+t)*sin(t);sin(t)+2*(1+t)*cos(t)];
dist = norm(r-y);
if dist > 1e-4
   factor = k*norm(r_p)/dist;
   yprime = factor*(r-y);
else
   error('ODE model ill-defined.')
end
