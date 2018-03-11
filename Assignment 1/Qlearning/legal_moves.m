%The function legal_moves returns arrays pos and moves
%pos returns the possibles positions of movement 1=left,2=right,3=up,4=down
%positions for the agent to move given the current position on the matrix. 
function [pos, moves] = legal_moves(curr,mat)

moves= [];
pos = [];
%Since the matrix is flattened out and curr is in range 1 to length(mat)^2,
%we can do the following valid legal moves

%LEFT - Since indexing starts from 0, so if at a valid index then can move one step left.
if(curr-1>0); moves = [moves curr-1]; pos = [pos 1];end;
%RIGHT - If not in the last row, then can move a step forward
if(rem(curr,length(mat))~=0); moves = [moves curr+1];  pos = [pos 2]; end;
%UP - One step above is equivalent to subtracting curr by length(mat)
if(curr-length(mat)>0); moves = [moves curr-length(mat)];  pos = [pos 3]; end;
%Down - One step below is equivalent to adding curr by length(mat)
if(curr+length(mat)<length(mat)^2); moves = [moves curr+length(mat)];  pos = [pos 4];end;

return;
