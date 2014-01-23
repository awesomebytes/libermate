%SMALL_WORLD  Small-world network example.
%             Display ring and small-world adjacency matrices.
%             Then compute average pathlengths.

rand('state',100)

N = 40; k = 4; short_ave = 10; p = short_ave/N;
r = zeros(1,N); r(2:k+1) = 1; r(N-k+1:N) = 1;
A = toeplitz(r);
subplot(2,2,1), spy(A)
title(sprintf('Ring Network, N = %2.0f, k = %2.0f',N, k),'FontSize',12)

subplot(2,2,2)
v = find(rand(N,1)<p);
Ashort = sparse(v,ceil(N*rand(size(v))),ones(size(v)),N,N);
spy(A+Ashort+Ashort')
title(sprintf('Add shortcuts: N*p = %2.0f',N*p),'FontSize',12)
h = waitbar(0,'Computing average pathlengths');

%%%%%% Average pathlength as a function of N*p %%%%%

N = 150; k = 4; M = 20; Smax = 150; Np = logspace(-2,2,M);
r = zeros(1,N); r(2:k+1) = 1; r(N-k+1:N) = 1;
B = toeplitz(r);
lmean = zeros(M,1);
for i = 1:M
    waitbar(i/M)
    p = Np(i)/N;
    smean = zeros(Smax,1);
    for s = 1:Smax
        v = find(rand(N,1)<p);
        Bshort = sparse(v,ceil(N*rand(size(v))),ones(size(v)),N,N);
        Bnetwork = B + Bshort + Bshort' + eye(N);  % Full array.
        L = sign(Bnetwork);  % Convert to matrix of 0s and 1s.
        power = 1;
        Bnew = Bnetwork;
        while any(any(Bnew==0))
           power = power + 1;
           Bold = Bnew;
           Bnew = Bnew*Bnetwork;
           L = L + ( (L == 0) & (Bnew > 0) )*power;
        end
        smean(s) = mean(mean(L-diag(diag(L))))*N/(N-1);
    end
    lmean(i) = mean(smean);
end
close(h)

subplot(2,2,3:4)
semilogx(Np,lmean,'ro')
xlabel('Shortcuts','FontSize',12), ylabel('Pathlength','FontSize',12)
title(sprintf('N = %2.0f, k = %2.0f',N, k),'FontSize',12)
