function [x_sort,x_mean,x_med,x_std] = marks2(x)
%MARKS2  Statistical analysis of marks vector.
%        Given a vector of marks X,
%        [X_SORT,X_MEAN,X_MED,X_STD] = MARKS2(X) computes a
%        sorted marks list and the mean, median, and standard deviation
%        of the marks.

x_sort = sort(x);
if nargout > 1, x_mean = mean(x); end
if nargout > 2, x_med  = median(x); end
if nargout > 3, x_std  = std(x); end
