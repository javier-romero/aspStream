% only works with the extended encoding
% all requests can always be scheduled
request(1,1,4) request(2,2,2)
request(1,2,3) submitted(1,-1) submitted(2,-1) occupied(1,1) occupied(1,2) occupied(1,3) occupied(2,1)
request(1,1,2) request(2,2,1) submitted(1,-2) submitted(2,-2) submitted(1,-1) occupied(1,1) occupied(1,2) occupied(2,1) occupied(2,2) occupied(2,3)
