% colon -> array
a=1:5
% colon -> slice (should make a copy of a)
b=a(2:4)
% test copy
b(1)=1
% get end
c=a(1:end)
% set all
c(:)=1
% get all as flat
d=a(:)
% get all but last
f=a(1:end-1)

