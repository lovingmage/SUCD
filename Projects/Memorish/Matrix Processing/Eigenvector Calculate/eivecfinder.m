function [ tempv, ev ,temp, e,t ] = eivecfinder( V_s, V_step )
%EIVECFINDER Summary of this function goes here
%   Detailed explanation goes here
% A = csvread('matrix.csv');
load 'matrix.mat';
%format long e
N = size(A,1);
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

Ph = A - diag(ones(N,1) * temp);
tempv = linsolve(Ph, zeros(N,1));

Ps = A - diag(ones(N,1) * e);
ev = linsolve(Ps, zeros(N,1));

t = toc();
end

