function fisher
%FISHER     Displays solutions to Fisher PDE.

m = 0; a = -50; b = 50; t0 = 0; tf = 20;
xvals = linspace(a,b,101); tvals = linspace(t0,tf,51);
[xmesh, tmesh] = meshgrid(xvals,tvals);

figure(1), subplot(2,2,1)
sol = pdepe(m,@fpde,@fica,@fbc,xvals,tvals);
ua = sol(:,:,1); mesh(xmesh,tmesh,ua)
xlabel('x'), ylabel('t'), zlabel('u','Rotation',0), title('u(x,t)')
text_set, view(30,30)

subplot(2,2,2), contour(xmesh,tmesh,ua,[0.2:0.2:0.8])
xlabel('x'), ylabel('t','Rotation',0), title('Contour Plot')
text_set, hold on
plot([10,20,20,10],[8,13,8,8],'r--'), text(0,6,'Ref. slope = 2')
hold off

subplot(2,2,3), sol = pdepe(m,@fpde,@ficb,@fbc,xvals,tvals);
ub = sol(:,:,1); mesh(xmesh,tmesh,ub)
xlabel('x'), ylabel('t'), zlabel('u','Rotation',0), title('u(x,t)')
text_set, view(30,30)

subplot(2,2,4), contour(xmesh,tmesh,ub,[0.2:0.2:0.8])
xlabel('x'), ylabel('t','Rotation',0), title('Contour Plot')
text_set, hold on
plot([25,35,35,25],[5,10,5,5],'r--'), text(15,3,'Ref. slope = 2')
hold off

figure(2), zmesh = xmesh - 2*diag(tvals)*ones(size(xmesh));
waterfall(zmesh,tmesh,ua)
xlabel('x-2t'), ylabel('t'), zlabel('u','Rotation',0), title('u(x-2t,t)')
zlim([0 1]), text_set, view(15,30)

%-------------------------- Subfunctions ------------------------------%
function [c,f,s] = fpde(x,t,u,DuDx)
%FDE  Fisher PDE.
c = 1; f = DuDx; s = u*(1-u);

function u0 = fica(x)
%FIC  Fisher initial condition: 1st case.
u0 = 0.99*(x<=-20);

function [pa,qa,pb,qb] = fbc(xa,ua,xb,ub,t)
%FBC  Fisher  boundary conditions.
pa = 0; qa = 1; pb = 0; qb = 1;

function u0 = ficb(x)
%FIC2  Fisher initial condition: 2nd case.
u0 = 0.25*(cos(0.1*pi*x).^2).*(abs(x)<=5);

function text_set
h = findall(gca,'type','text'); set(h,'FontSize',12,'FontWeight','Bold')
