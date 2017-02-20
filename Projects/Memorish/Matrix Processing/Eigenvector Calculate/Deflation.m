tic();
v2 = transpose(v);
M = v*v2
nor = norm(v)
nor_sq = nor*nor
B = A - 6.415*(M/nor_sq);
toc();