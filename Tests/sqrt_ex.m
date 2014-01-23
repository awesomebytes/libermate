%SQRT_EX
% Script plotting a point on the unit circle and its two square roots,
% with the right half-plane shaded.

clear i                                % Ensure i is function, not variable.
z = -1+i; z = z/abs(z);                % Point z on unit circle.
s = sqrt(z);

h = axes('XLim',[-2 2],'YLim',[-2 2]); % Create Axes with specified range.

fill([0 2 2 0],[-2 -2 2 2],[.8 .8 .8]) % Shade right half-plane.
hold on

plot(z,'s','MarkerSize',8), line([0 real(z)],[0 imag(z)])
plot(s,'d','MarkerSize',8), line([0 real(s)],[0 imag(s)])
plot(-s,'d','MarkerSize',8), line([0 -real(s)],[0 -imag(s)],'LineStyle',':')

% Unit circle.
rectangle('Position',[-1,-1,2,2],'Curvature',[1,1],'LineStyle','--')
axis square

% Draw x- and y-axes through origin.
plot([-2 2], [0 0], '-'), plot([0 0], [-2 2], '-')
set(h,'XTick',[],'YTick',[])

xlabel('Re \lambda')
ylabel('Im \lambda','Rotation',0,'HorizontalAlignment','right')

text(real(z),imag(z)+0.2,'\lambda','HorizontalAlignment','center')
text(0,0,'0','HorizontalAlignment','right','VerticalAlignment','top')
text(real(s),imag(s)+0.2,'\lambda^{1/2}')
text(-real(s),-imag(s)-0.2,'-\lambda^{1/2}','HorizontalAlignment','right')
hold off

% Reset FontSize for all text.
g = findall(gcf,'type','text'); set(g,'Fontsize',16)
