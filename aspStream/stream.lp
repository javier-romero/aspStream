% constants
#const jobs=4.
#const requests=2.
#const machines=2.

% assign every request R at window time WT to exactly one job J
{ assign((R,WT),J) : J=1..jobs } = 1 :- window(request(R,_,_),WT), extended!=1.

% different pairs (R1,WT1), (R2,WT2) cannot be assigned to the same job J
:- assign((R1,WT1),J), assign((R2,WT2),J), (R1,WT1) < (R2,WT2).

% there is a job J for machine M with duration D
% if request R at WT (for machine M with duration D) is assigned to J
job(J,M,D) :- assign((R,WT),J), window(request(R,M,D),WT).

% window terms definition
wterm(request(R,M,D)) :- R=1..requests, M=1..machines, D=1..horizon.

% display
#show wstart(request(R,M,D),WT,T) : window(request(R,M,D),WT), assign((R,WT),J), start(J,T).
