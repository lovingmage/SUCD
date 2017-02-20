% A is our matrix
flag = 0;
[n,m] = size(A);
if (any(eig(A)) <= 0)
    % Then A is not an M-matrix
    flag = 1;
    disp 'negative eigenvalue; not M-matrix!';
else
    idx = find(A > 0);
    [I,J] = ind2sub([n,m],idx);
    % I and J are the row/col subscript indices for positive entries.
    % We should only have this when i = j. If i =/= j, then i-j =/= 0,
    % so we look for non-zero entries in I-J
    if (any(I-J) ~= 0)
        % Then A is not an M-matrix
        flag = 1;
        disp 'not M-matrix!';
    else
        disp 'M-matrix!';
    end
end