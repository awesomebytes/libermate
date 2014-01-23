%CHEB3PLOT

y = linspace(-1,1,1500)';
Z = cheby(y,61);

k = [0 2 4 10 20 40 60];
z = Z(:,k+1);

for j = 1:length(k)
    plot3(j*ones(size(y)),y,z(:,j),'LineWidth',1.5);
    hold on
end
hold off
box on
set(gca,'DataAspectRatio',[1 0.75 4])  % Change shape of box.
view(-72,28)
set(gca,'XTickLabel',k)

% Labels, with adjustment of position.
xlabel('k','FontSize',14)
h = get(gca,'Xlabel'); set(h,'Position',get(h,'Position') + [1.5 0.1 0])
ylabel('x','FontSize',14)
h = get(gca,'Ylabel'); set(h,'Position',get(h,'Position') + [0 0.25 0])
set(gca,'FontSize',14)
