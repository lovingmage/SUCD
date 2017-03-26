function [ eigenvs, temp, e, t] = eivecfinder( V_s, V_step )
%EIVECFINDER Summary of this function goes here
%   Detailed explanation goes here
% A = csvread('matrix.csv');
load 'matlab.mat'; 
%A = full(out);
%format long e
N = size(A,1);
V_times = 2*V_s/V_step;
% c_max = 250;
% f_s = 0;

log_tmp = zeros(V_times, 1);
temp = V_s;
mm = 0;
eigenvs = [];
eindex = 1;
tic();
for k =1:V_times
    x = evb(A, temp);
    %m = max(max(x), abs(min(x))); 
    m = max(x); 
    log_tmp(k) = m;
    
    if k>2
        if (log_tmp(k-1) >= log_tmp(k))&&(log_tmp(k-1) >= log_tmp(k-2))
            eigenvs(eindex) = V_s - (k-1)*V_step;
            eindex = eindex + 1;
        end
    end
    
%     if (m > 0)
%         break;
%     end

    temp = temp - V_step;
end
t = toc();

e= max(eig(A));
%disp(e);
% Ph = A - diag(ones(N,1) * temp);
% tempv = linsolve(Ph, zeros(N,1));
% 
% Ps = A - diag(ones(N,1) * e);
% ev = linsolve(Ps, zeros(N,1));


end

