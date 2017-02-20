function [ temp ] = fdx( s )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

load 'matlab.mat'

Vtimes = 200/s;
temp = zeros(Vtimes, 1);

x1n = 200;
fx1n_temp = evb(A, x1n);
fx1n = max(fx1n_temp);
fdx1n = 0;

for k = 1:Vtimes
    x = x1n - s;
    fx_tmp = evb(A, x);
    fx = max(fx_tmp);
    
    fdx = (fx - fx1n)/(x - x1n);
    temp(k) = fdx;
    if (fdx1n*fdx < 0)
        disp(200 - x)
    end
    
    fx1n = fx;
    x1n = x;
    fdx1n = fdx;
    
end

