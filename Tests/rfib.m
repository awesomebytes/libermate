%RFIB                    Random Fibonacci sequence.

rand('state',100)        % Set random number state.
m = 1000;                % Number of iterations.

x = [1 2];               % Initial conditions.
for n = 2:m-1            % Main loop.
     x(n+1) = x(n) + sign(rand-0.5)*x(n-1);
end

semilogy(1:m,abs(x))
c = 1.13198824;          % Viswanath's constant.
hold on
semilogy(1:m,c.^(1:m))
hold off
