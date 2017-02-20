function [ temp, e, t ] = binevfinder( V_s, V_error )
%BINEVFINDER Summary of this function goes here
%   Detailed explanation goes here

load 'matlab.mat';
UPPER_BOUND = V_s;
LOWER_BOUND = 0;
ERRORs = UPPER_BOUND - LOWER_BOUND;

while ERRORs > V_error
    x = evb(A, (UPPER_BOUND - LOWER_BOUND));
    m = max(x); 
    midValue = (UPPER_BOUND + LOWER_BOUND)/2;
    
    if m > 0
        LOWER_BOUND = midValue;
    end
    
    if m < 0
        UPPER_BOUND = midValue;
    end
    ERRORs = UPPER_BOUND - LOWER_BOUND; 
end

temp = (UPPER_BOUND + LOWER_BOUND)/2;
tic();
e= max(eig(A));
t = toc();

end

