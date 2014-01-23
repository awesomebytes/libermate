%GARDEN

% Cols: Carrots|Broccoli|Green Beans|Cucumbers|Chard.  Rows are months.
Y = [0.4 0.3 0.0 0.0 0.9
     0.6 0.4 0.0 0.0 1.0
     0.7 0.8 0.3 0.2 1.2
     0.6 0.5 0.9 0.4 1.1
     0.4 0.4 0.7 0.6 0.9];

t = [13 15 22 24 18]; % Temperature.

b = bar(Y,'stacked');
ylabel('Yield (kg)'), ylim([0 4])

h1 = gca; % Handle of first axis.
set(h1,'XTickLabel','May|June|July|August|September')

% Create a second axis at same location as first and plot to it.
h2 = axes('Position',get(h1,'Position'));
p = plot(t,'Marker','square','MarkerSize',12,'LineStyle','-',...
           'LineWidth',2,'MarkerFaceColor',[.6 .6 .6]);
ylabel('Degrees (Celsius)')
title('Fran''s vegetable garden','FontSize',14)

% Align second x-axis with first and remove tick marks and tick labels.
set(h2,'Xlim',get(h1,'XLim'),'XTick',[],'XTickLabel',[])
% Locate second y-axis on right, make background transparent.
set(h2,'YAxisLocation','right','Color','none')

% Make second y-axis tick marks line up with those of first.
ylimits = get(h2,'YLim');
yinc = (ylimits(2)-ylimits(1))/4;
set(h2,'Ytick',[ylimits(1):yinc:ylimits(2)])

% Give legend the Axes handles and place top left.
legend([b,p],'Carrots','Broccoli','Green Beans','Cucumbers',...
       'Swiss Chard','Temperature','Location','NW')
