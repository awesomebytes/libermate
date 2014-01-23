%HIST_EX

randn('state',1)   % To make histogram reproducible.
y = randn(10000,1);

hist(y,min(y):0.1:max(y))

h = findobj(gca,'Type','patch');
set(h,'EdgeColor','k','Facecolor',[1 1 1]/2)
set(gca,'TickDir','out')
xlim([min(y) max(y)])

set(gca,'FontSize',14)
