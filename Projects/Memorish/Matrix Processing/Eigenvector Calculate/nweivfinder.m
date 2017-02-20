function [ x, e, t, k ] = nweivfinder( V_s, V_step, dis )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%   Load the external datasets
load 'Matlab.mat';
% A = out;
% A = full(A);


tic();
temp = V_s;
k=0; %iteration times

x2n = V_s;
x1n = V_s + V_step;
x = x1n + V_step;

fx2n_tmp = evb(A, x2n);
fx2n = 1/max(fx2n_tmp);
fx1n_tmp = evb(A, x1n);
fx1n = 1/max(fx1n_tmp);
fx_tmp = evb(A, x);
fx = 1/max(fx_tmp);

fdx1n = (fx2n - fx1n)/(x2n - x1n);
fdx = (fx1n - fx)/(x1n - x);
fddx = (fdx1n - fdx)/(x1n - x);

k = 2


while(abs(fdx) > dis)
    k = k + 1;
    x2n = x1n;
    x1n = x;
    fx1n = fx;
    fdx1n = fdx;
    
    x = x - (fx/fdx);
    
    if (abs((fx/fdx)) < 0.0001)
        break;
    end
    
    
    fx_tmp = evb(A, x);
    fx = 1/max(fx_tmp); 
    

    fdx = (fx1n - fx)/(x1n - x);
    fddx = (fdx1n - fdx)/(x1n - x);
    

    end

t = toc();
e= eig(A);



end

