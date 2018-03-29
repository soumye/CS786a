%set the environment variables
alpha = 0.3;
gamma = 0.9;
%load the matrix
environment_design;
%linearize the matrix
vec = reshape(mat,1,length(mat)^2);
%Initialize the Value vector
V = zeros(1,length(vec));
%Randomly select an initial current position
curr = ceil(rand*length(mat)^2);
%Load possible moves
moves= legal_moves(curr,mat);

vidObj = VideoWriter('sample.avi');
open(vidObj);

%Iterate 1000 times
for time = 1:1000
    R = vec(curr);
    %Choose a new move randomly from possible moves
    new = moves(ceil(rand*length(moves)));
    % TD Algorithm update from V Values. Update the V(curr) from Reward for new move and V(new).
    V(curr) = V(curr) + alpha*(R + gamma*V(new) - V(curr));        
    curr = new;
    %Load new possible moves
    moves= legal_moves(curr,mat);
    Vmat = reshape(V,length(mat), length(mat));
    %Take a time-snapshot for error
    error(time) = sqrt(sum((mat(mat~=0) - Vmat(mat~=0)).^2));    
    cumR(time) = R;
        imagesc(Vmat);
        currFrame = getframe(gcf);
        writeVideo(vidObj,currFrame);
end;    
plot(error);
plot(cumR);
imagesc(Vmat);    
close(vidObj);
