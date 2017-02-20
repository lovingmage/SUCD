function [ temp, e, t, k ] = gdeivfinder( V_s, V_step, dis )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
load 'BAedges.mat';
A = out;
A = full(A);
tic();
temp = V_s;
flag=1;  %loop flag
k=0; %iteration times

x = evb(A, temp);
m = max(x); 
last_mm = 1/m;

temp = V_s - V_step;
last_temp = V_s;

while(flag)
    dis_x = temp - last_temp;
    x = evb(A, temp);
    m = max(x); 
    mm = 1/m; 
    dis_y = mm - last_mm;
    
    slop = dis_y/dis_x;
    if(dis_y < dis)
        flag = 0;
    end
    
    last_temp = temp;
    last_mm = mm;
    temp = temp - ((-slop) * V_step);
    k = k+1;
end
t = toc();
e= max(eig(A));
% [V,D] = eig(A);
% tmp = D(1,1);
% tmp_count = 1;
% for i = 1:n
%     if (D(i,i) >= tmp)
%         tmp = D(i,i);
%         tmp_count = i;
%     end
% end
% e = tmp;
% disp(e);
% evig = V(:,i);
% dist = norm(evig - vec);
% disp(dist);




end

