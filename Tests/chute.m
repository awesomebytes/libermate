%CHUTE  Chutes and ladders analysis.
%       Probability of finishing in exactly n moves and in at least n moves.

N = 100;   % Start at square zero, finish at square N.

% "+1" translates square to state.
top = [ 1  4  9 16 21 28 36 47 49 51 56 62 64 71 80  87 93 95 98] + 1;
bot = [38 14 31  6 42 84 44 26 11 67 53 19 60 91 100 24 73 75 78] + 1;

P = toeplitz(zeros(1,N+1),[0 ones(1,6) zeros(1,N-6)]);
for k = N-4:N+1, P(k,k) = k-N+5; end
P = P/6;

for k = 1:length(top)
    r = top(k); s = bot(k);     % Chute or ladder from r to s.
    P(:,s) = P(:,s) + P(:,r);   % Add column r to column s.
end
P(top,:) = [];  P(:,top) = [];  % Remove starts of chutes and ladders.

figure(1)
spy(P)

M = 200;
cumprob = zeros(M,1);
cumprob(1) = P(1,end);
v = P(1,:);
for n = 2:M,
    v = v*P;
    cumprob(n) = v(end);
end

figure(2)
colormap([0.6,0.6,0.6])
subplot(2,1,1)
bar(diff([0;cumprob]))
title('Probability for Game Length','FontSize',12,'FontWeight','Bold')
grid on
xlim([0 M])
subplot(2,1,2)
bar(cumprob)
title('Cumulative Probability for Game Length',...
      'FontSize',12,'FontWeight','Bold')
grid on
xlim([0 M])
