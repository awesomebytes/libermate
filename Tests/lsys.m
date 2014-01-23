function [coord,mov] = lsys(rule,coord,mov,angle,scale,gen)
%LSYS    Recursively generated L-system.
%        LSYS(RULE,COORD,MOV,ANGLE,SCALE,GEN) generates the L-system
%        produced by GEN generations of the production rule given
%        in the string RULE.
%        COORD and MOV are the initial (x,y) and (dx,dy) values.
%        ANGLE is a 2-vector, with ANGLE(1) specifying the clockwise
%        rotations and ANGLE(2) the counterclockwise rotations.
%        SCALE is the scale factor for branch length.

%        During recursion, GEN, COORD, and MOV record the current state.

if gen == 0
   % Draw line, then update location.
   plot([coord(1),coord(1)+mov(1)],[coord(2),coord(2)+mov(2)])
   coord = coord + mov;
   hold on
else
   stack = 0;
   for k=1:length(rule)
     switch rule(k)
         case 'F'
                [coord,mov] = lsys(rule,coord,mov,angle,scale,gen-1);
         case '+'
                mov = [cos(angle(1)) sin(angle(1));
                      -sin(angle(1)) cos(angle(1))]*mov;
         case '-'
                mov = [cos(angle(2)) -sin(angle(2));
                       sin(angle(2)) cos(angle(2))]*mov;
         case '['
                stack = stack + 1;
                cstack(1:2,stack) = coord;
                dstack(1:2,stack) = mov;
                mov = scale*mov;
         case ']'
                coord = cstack(1:2,stack);
                mov = dstack(1:2,stack);
                stack = stack - 1;
     end
   end
end
