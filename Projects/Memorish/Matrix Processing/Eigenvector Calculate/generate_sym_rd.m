%N=500;
 M=randi([-60,-30]*10,[500,500])/10;
 M=0.5*(M+M');
 L=500; %  magnitude
 for n=1:500
        M(n,n)=L*rand;
 end