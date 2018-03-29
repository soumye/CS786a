%The function legal_moves returns an array of available 
%positions for the agent to move given the current position on the matrix. 
function moves = legal_moves(curr,mat)

moves= [];
%Since the matrix is flattened out and curr is in range 1 to length(mat)^2,
%we can do the following valid legal moves

%Since indexing starts from 0, so if at a valid index then can move one step back.
if(curr-1>0); moves = [moves curr-1]; end;
%If not in the last row, then can move a step forward
if(rem(curr,length(mat))~=0); moves = [moves curr+1]; end;
%One step above is equivalent to subtracting curr by length(mat)
if(curr-length(mat)>0); moves = [moves curr-length(mat)]; end;
%One step below is equivalent to adding curr by length(mat)
if(curr+length(mat)<length(mat)^2); moves = [moves curr+length(mat)]; end;

return;
