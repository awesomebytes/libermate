%COLLATZ             Collatz iteration.

n = input('Enter an integer bigger than 2:   ');
narray = n;

count = 1;
while n ~= 1
  if rem(n,2) == 1   % Remainder modulo 2.
     n = 3*n+1;
  else
     n = n/2;
  end
  count = count + 1;
  narray(count) = n; % Store the current iterate.
end

plot(narray,'*-')    % Plot with * marker and solid line style.
title(['Collatz iteration starting at ' int2str(narray(1))],'FontSize',16)
