%set the environment variables
alpha = 0.2;
%load the matrix
environment_design;
%linearize the matrix
vec = reshape(mat,1,length(mat)^2);
V_Exp = reshape(mat,1,length(mat)^2);
%Initialize the quality function for state-action pair
Q = zeros(4,length(vec));
%Randomly select an initial current position
curr = ceil(rand*length(mat)^2);
%Load possible moves
[pos, moves] = legal_moves(curr,mat);
%set init value for epsilon
epsilon = 0.95;
% vidObj = VideoWriter('sample.avi');
% open(vidObj);

%Iterate 1000 times
for time = 1:4000
    %Reward at the current position
    R = vec(curr);
    %a = action chosen greedily
    rand_action = pos(randi(columns(pos))); 
    greedy_action = pos(find(moves == max(moves))); 
    if rand <= epsilon             % (epsilon) times
         a = rand_action;    % explore all 
     else                                % (1 - epsilon) times
         a = greedy_action;  % exploit the best 
    end 
    %V_exp is the expectation of the Quality Function on taking an action
    V_Exp(curr) = epsilon*(Q(rand_action,curr)) + (1-epsilon)*(Q(greedy_action,curr));
    %new = new state
    new = moves(find(pos == a));
    %Q-Learning Update equation
    Q(a, curr) = Q(a, curr) + alpha*(R + max(Q(:,new)) - Q(a, curr));
    %Update the state   
    curr = new;
    %Load new possible moves
    [pos, moves] = legal_moves(curr,mat);
    Vmat = reshape(V_Exp,length(mat), length(mat));
    %Take a time-snapshot for error
    error(time) = sqrt(sum((mat(mat~=0) - Vmat(mat~=0)).^2));    
    cumR(time) = R;
        % imagesc(Vmat);
        % currFrame = getframe(gcf);
        % writeVideo(vidObj,currFrame);
end;    
plot(error);
% plot(cumR);
imagesc(Vmat);    
% close(vidObj);
