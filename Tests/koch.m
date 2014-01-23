function koch(pl,pr,level)
%KOCH   Recursively generated Koch curve.
%       KOCH(PL, PR, LEVEL) recursively generates a Koch curve,
%       where PL and PR are the current left and right endpoints and
%       LEVEL is the level of recursion.

if level == 0
  plot([pl(1),pr(1)],[pl(2),pr(2)]); % Join pl and pr.
  hold on
else
  A = (sqrt(3)/6)*[0 1; -1 0];       % Rotate/scale matrix.

  pmidl = (2*pl + pr)/3;
  koch(pl,pmidl,level-1)             % Left branch.

  ptop = (pl + pr)/2 + A*(pl-pr);
  koch(pmidl,ptop,level-1)           % Left mid branch.

  pmidr = (pl + 2*pr)/3;
  koch(ptop,pmidr,level-1)           % Right mid branch.

  koch(pmidr,pr,level-1)             % Right branch.

end
