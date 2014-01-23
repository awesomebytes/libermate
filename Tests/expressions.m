% initial
b=0
c=0
d=0
f=0
% for
for i=1:5
    b=b+i
end
% for break
for i=1:5
    b=b+i
    if i==3
        break
    end
end
% for continue
for i=1:5
    if i==2
        continue
    end
    b=b+i
end

% if
if b==1
    c=1
end
% if else
if b==2
    c=1
else
    c=3
end
% if elseif else
if b==4
    d=1
elseif b==7
    d=2
elseif b==5
    d=3
else
    d=4
end

% switch
switch d
case 1
    f=1
end
% switch, otherwise
switch d
case 1
    g=1
case 2
    g=2
otherwise
    g=3
end

