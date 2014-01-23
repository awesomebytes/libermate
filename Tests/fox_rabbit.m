function fox_rabbit
%FOX_RABBIT  Fox-rabbit pursuit simulation.
%            Uses relative speed parameter, K.

k = 1.1;
tspan = [0 10]; yzero = [3;0];
options = odeset('RelTol',1e-6,'AbsTol',1e-6,'Events',@events);
[tfox,yfox,te,ye,ie] = ode45(@fox2,tspan,yzero,options);
plot(yfox(:,1),yfox(:,2)), hold on
plot(sqrt(1+tfox).*cos(tfox),sqrt(1+tfox).*sin(tfox),'--')
plot([3 1],[0 0],'o'), plot(yfox(end,1),yfox(end,2),'*')
axis equal, axis([-3.5 3.5 -2.5 3.1])
legend('Fox','Rabbit'), hold off

    function yprime = fox2(t,y)
    %FOX2   Fox-rabbit pursuit simulation ODE.

    r = sqrt(1+t)*[cos(t); sin(t)];
    r_p = (0.5/sqrt(1+t)) * [cos(t)-2*(1+t)*sin(t); sin(t)+2*(1+t)*cos(t)];
    dist = max(norm(r-y),1e-6);
    factor = k*norm(r_p)/dist;
    yprime = factor*(r-y);

    end

end

function [value,isterminal,direction] = events(t,y)
%EVENTS    Events function for FOX2.
%          Locate when fox is close to rabbit.

r = sqrt(1+t)*[cos(t); sin(t)];
value = norm(r-y) - 1e-4;     % Fox close to rabbit.
isterminal = 1;               % Stop integration.
direction = -1;               % Value must be decreasing through zero.

end
