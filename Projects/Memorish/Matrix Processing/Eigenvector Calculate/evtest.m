
V_s = 50;
N = 7;
rst = zeros(N,5);
rst(1,1) = 0.01;
rst(2,1) = 0.05;
rst(3,1) = 0.1;
rst(4,1) = 0.5;
rst(5,1) = 1;
rst(6,1) = 5;
rst(7,1) = 10;


for i = 1:N
    [t,e,f] = eivecfinder(V_s, rst(i,1)); % rst(i,1):step
    rst(i,2) = t;  % time
    rst(i,3) = e;  % maximum eigen value using eig() func.
    rst(i,4) = abs(t-e)/abs(e);  %
    rst(i,5) = f;
    %rst(i,6) = dist;
end