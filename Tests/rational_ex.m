function rational_ex(x)
%RATIONAL_EX   Illustration of nested function.

a = 1; b = 2; c = 1; d = -1;
fd_deriv(@rational,x)

   function r = rational(x)
   % Rational function.
   r = (a+b*x)/(c+d*x);
   end

end
