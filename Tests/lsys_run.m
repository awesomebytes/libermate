%LSYS_RUN    Runs lsys function to draw L-systems.

subplot(2,2,1)
rule = 'F[+F][-F][++F][--F]';
[c,d] = lsys(rule,[0;0],[0;1],[pi/8;pi/5],0.6,5);
title(rule,'FontWeight','Bold')
axis equal, axis off

subplot(2,2,2)
rule = 'F[+F]F[-F][F]';
[c,d] = lsys(rule,[0;0],[0;1],[pi/6;pi/6],1,5);
title(rule,'FontWeight','Bold')
axis equal, axis off

subplot(2,2,3)
rule = 'F[+F][-F][++F]F[+F][-F]';
[c,d] = lsys(rule,[0;0],[0;1],[pi/5;pi/6],0.8,4);
title(rule,'FontWeight','Bold')
axis equal, axis off

subplot(2,2,4)
rule = 'FF-[-F+F+F]+[+F-F-F]';
[c,d] = lsys(rule,[0;0],[0;1],[pi/6;pi/6],0.7,4);
title(rule,'FontWeight','Bold')
axis equal, axis off
