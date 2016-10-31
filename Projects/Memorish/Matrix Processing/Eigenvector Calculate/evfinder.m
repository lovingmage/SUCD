function [temp, e,t] = evfinder(V_s, V_step) %
% A = csvread('matrix.csv');
load 'matlab.mat';
% N = size(A,1);
%A = randn(60)
V_times = 2*V_s/V_step;
% c_max = 250;
% f_s = 0;
temp = V_s;
mm = 0;
for k =1:V_times
    x = evb(A, temp);
    m = max(max(x), abs(min(x))); 
    if (m>mm)
        mm = m;
        %if (mm >= c_max)
            %f_s = 1;
        %end
    else
        %if(f_s == 1)
            break;
        %end
    end
    temp = temp - V_step;
end
tic();
e= max(eig(A));
t = toc();

