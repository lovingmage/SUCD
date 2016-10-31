
V_s = 48;
N = 3;
rst = zeros(N,4);
rst(1,1) = 0.01;
rst(2,1) = 0.05;
rst(3,1) = 0.1;
%rst(4,1) = 0.5;
%rst(5,1) = 1;
%rst(6,1) = 5;
%rst(7,1) = 10;


for i = 1:N
    [t,e,f] = evfinder(V_s, rst(i,1)); % rst(i,1):step
    rst(i,2) = t;  % time
    rst(i,3) = e;  % maximum eigen value using eig() func.
    rst(i,4) = abs(t-e)/abs(e);  %
    rst(i,5) = f;
end