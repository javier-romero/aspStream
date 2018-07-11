% constants
#const horizon = 4.

% for each job J with duration D, choose one starting point T
{ start(J,T) : T=1..horizon+1-D } = 1 :- job(J,_,D).

% for each job J for machine M with duration D,
% if J starts at T, then J occupies M for D steps at T
occupies(J,M,  D,T) :- start(J,T), job(J,M,D).

% if J occupies M for D steps (with D>1) at T-1,
% then J occupies M for D-1 steps at T
occupies(J,M,D-1,T) :- occupies( J,M,D,T-1), D> 1.

% it cannot be the case that
% J1 occupies M at T and J2 (with J1<J2) also occupies M at T
:- occupies(J1,M,_,T), occupies(J2,M,_,T), J1<J2.

% display
#show.
%#show start/2.
