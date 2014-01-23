function gasket(Pa,Pb,Pc,level)
%GASKET  Recursively generated Sierpinski gasket.
%        GASKET(PA, PB, PC, LEVEL) generates an approximation to
%        the Sierpinski gasket, where the 2-vectors PA, PB, and PC
%        define the triangle vertices.
%        LEVEL is the level of recursion.

if level == 0
  % Fill the triangle with vertices Pa, Pb, Pc.
  fill([Pa(1),Pb(1),Pc(1)],[Pa(2),Pb(2),Pc(2)],[0.5 0.5 0.5]);
  hold on
else
  % Recursive calls for the three subtriangles.
  gasket(Pa,(Pa+Pb)/2,(Pa+Pc)/2,level-1)
  gasket(Pb,(Pb+Pa)/2,(Pb+Pc)/2,level-1)
  gasket(Pc,(Pc+Pa)/2,(Pc+Pb)/2,level-1)
end
