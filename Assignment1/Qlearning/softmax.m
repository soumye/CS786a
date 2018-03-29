%Function to calcuate softmax on a vector for soft-sampling
function ans = softmax(n)
	ans = exp(n)/sum(exp(n));
return;
