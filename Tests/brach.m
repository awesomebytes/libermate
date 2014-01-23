function brach
%BRACH  Brachistochrone illustration.
%       Computes and plots approximate brachistochrone by optimization,
%       using FMINSEARCH, and exact brachistochrone, using FZERO.

bx = 1; g = 9.81;
byvals = linspace(0.2,2,10);
Nvals = [4 8];
for i = 1:2
   N = Nvals(i);
   subplot(1,2,i)
   for k = 1:length(byvals)

      % Approximate brachistochrone.
      by = byvals(k);
      dy = by/N; dx = bx/N;
      yinit = [dy:dy:by-dy];
      y = fminsearch(@Btime,yinit);

      plot([0:dx:bx],-[0 y by],'ro-')
      hold on

      % True brachistochrone.
      tzero = @(theta)(by*theta-by*sin(theta)+bx*cos(theta)-bx);
      tstar = fzero(tzero,pi);
      R = by/(1-cos(tstar));
      thetavals = linspace(0,tstar,100);
      xcoord = R*(thetavals-sin(thetavals));
      ycoord = R*(1-cos(thetavals));
      plot(xcoord,-ycoord,'g--','Linewidth',2)

   end
   title(sprintf('N = %1.0f',N),'FontSize',14)
   xlim([0,bx]), axis off
end
hold off

  function T = Btime(y)
  %BTIME Travel time for a particle.
  %      Piecewise linear path with equispaced y between (0,0) and (bx,by).

  yvals = [0 y by];        % End points do not vary.
  N = length(y)+1; d = bx/N;
  T = sum(2*sqrt( d^2 + (diff(yvals)).^2 )./( sqrt(2*g*yvals(2:end)) + ...
          sqrt(2*g*yvals(1:end-1) )));
  end

end
