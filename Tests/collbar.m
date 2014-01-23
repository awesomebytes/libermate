%COLLBAR             Collatz iteration bar graph.

N = 29;              % Use starting values 1,2,...,N.
niter = zeros(N,1);  % Preallocate array.
for i = 1:N
    count = 0;
    n = i;
    while n ~= 1
        if rem(n,2) == 1
           n = 3*n+1;
        else
           n = n/2;
        end
        count = count + 1;
    end
    niter(i) = count;
end
bar(niter)   % Bar graph.
grid         % Add horizontal and vertical grid lines.
title('Collatz iteration counts','FontSize',16)
xlabel('Starting value','FontSize',16)        % Label x-axis.
ylabel('Number of iterations','FontSize',16)  % Label y-axis.
