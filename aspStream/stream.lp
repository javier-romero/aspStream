% constants
#const jobs=2.
#const length=2.
#const machines=2.
#const horizon=4.

% assign to exactly one job J
% every element job(M,D) at window time WT in position P
{ assign(P,WT,J) : J=1..jobs } = 1 :- window(elem(P,request(M,D)),WT), extended!=1.

% different pairs (P1,WT1), (P2,WT2) cannot be assigned to the same job J
:- assign(P1,WT1,J), assign(P2,WT2,J), (P1,WT1) < (P2,WT2).

% for each element job(M,D) at window time WT in position P that is assigned to J,
% there is a job J for machine M with duration D
job(J,M,D) :- assign(P,WT,J), window(elem(P,request(M,D)),WT).

% window terms definition
wterm(elem(P,request(M,D))) :- P=1..length, M=1..machines, D=1..horizon.

% display
#show assign/3.
