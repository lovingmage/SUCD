function [ log_tmp, temp, e, t] = evfinder(V_s, V_step) %
% A = csvread('matrix.csv');
load 'matlab.mat';
%A = full(out);
tic();
%n = size(A,1);
%A = randn(60)
V_times = V_s/V_step;
% c_max = 250;
% f_s = 0;
temp = V_s;
mm = 0;
log_tmp = zeros(V_times, 1)

for k =1:V_times
    x = evb(A, temp);
    log_tmp(k) = sum(x)/norm(x)
%     if (m>mm)
%         mm = m;
%         %if (mm >= c_max)
%             %f_s = 1;
%         %end
%     else
%         %if(f_s == 1)
%         %vec = x;
%         break;
%         %end
%    end
    temp = temp - V_step;
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


