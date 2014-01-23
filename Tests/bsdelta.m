%BSDELTA  Black--Scholes delta surface with three asset paths superimposed.

randn('state',51)
E = 1; r = 0.05; sigma = 0.6; mu =0.05; T = 1;
N1 = 50; Dt = T/N1; N2 = 60;

tvals = [0:Dt:T-Dt];                           % Avoid division by zero.
Svals = linspace(.01,2.5,N2);
[Sgrid,tgrid] = meshgrid(Svals,tvals);

d1grid = (log(Sgrid/E) + ...
         (r+0.5*sigma^2)*(T-tgrid))./(sigma*sqrt(T-tgrid));
Ngrid = 0.5*(1+erf(d1grid/sqrt(2)));

tvals = [0:Dt:T];                              % Add expiry date.
[Sgrid,tgrid] = meshgrid(Svals,tvals);         % Extend the grid.
Ngrid(end+1,:) = 0.5*(sign(Svals - E) + 1);    % Append final time values.

surf(Sgrid,tgrid,Ngrid)
xlabel('S','FontWeight','Bold','FontSize',16)
ylabel('t','FontWeight','Bold','FontSize',16)
zlabel('delta','FontWeight','Bold','FontSize',16,...
       'Rotation',0,'HorizontalAlignment','right')
ylim([0 T]), xlim([0 2.5])
set(gca,'ZTick',[])
set(gca,'YTick',[0,T]), set(gca,'YTickLabel','0|T','FontSize',12)
set(gca,'XTick',E), set(gca,'XTickLabel','E','FontSize',12)

% Superimpose asset paths.
hold on
L = 200; Dt = T/L;
tpath = [0:Dt:T-Dt]';
Szero = [1.5;0.95;0.7];
for k = 1:3
   factors = exp((mu-0.5*sigma^2)*Dt+sigma*sqrt(Dt)*randn(L,1));
   Spath = [Szero(k);Szero(k)*cumprod(factors)];
   dpath = (log(Spath(1:end-1)/E) + ...
           (r+0.5*sigma^2)*(T-tpath))./(sigma*sqrt(T-tpath));
   Npath = 0.5*(1+erf(dpath/sqrt(2)));
   Npath = [Npath;0.5*(sign(Spath(end)-E)+1)];
   deltaN = 0.1;
   Npath(2:end) = Npath(2:end)+deltaN;
   plot3(Spath,[tpath;T],Npath,'w-','Linewidth',2)
end
hold off, view(-60,35)
