% extended encoding
#const extended=1.

% assign to at most one job J
% every element job(M,D) at window time WT in position P
{ assign(P,WT,J) : J=1..jobs } <= 1 :- window(elem(P,request(M,D)),WT).

% maximize the jobs assigned,
% giving higher priority to the latest requests
#maximize{ 1@-WT,P : assign(P,WT,J) }.

% if occupied(M,T) appears in the latest position of the stream (0),
% then M cannot be occupied at T
:- window(occupied(M,T),0), occupies(_,M,_,T).

% if done(P,WT) appears in the latest position of the stream (0),
% then P,WT cannot be assigned
:- window(done(WT,P),0), assign(P,WT,_).

% new window terms definition
wterm(occupied(M,T)) :-        M=1..machines, T=1..horizon.
wterm(   done(WT,P)) :- WT=1-window_size..-1,  P=1..length.
