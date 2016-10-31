function x = evb( A,lamda ) %find eigen value
load 'primeb.mat';
n= size(A,1);
A2 =  A;
b = zeros(n,1);
for i=1:n
    b(i,1) = primeb(i,1);
    A2(i,i) = A(i,i) - lamda;  %A2=A-lamda
end
x= linsolve(A2, b);
%b2 = A2*x;
end